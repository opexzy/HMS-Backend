from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from staff.models import staff
from staff.permission.list import CAN_CLOSE_RESERVATION
from utils.randstr import get_token
from utils.api_helper import response_maker, request_data_normalizer, getlistWrapper
from staff.permission import use_permission, CAN_MAKE_RESERVATION, CAN_VIEW_RESERVATION, CAN_CANCEL_RESERVATION
from hms_auth.models import AuthModel
from staff.models import StaffModel
from django.db import transaction
from reservation.serializers import ReservationSerializer
from hms.settings import ROWS_PER_PAGE
from django.db.models import Q, F
from reservation.models import ReservationModel
from reservation.models.reservation import STATUS_OPTIONS
from datetime import datetime, timedelta
from django.utils import timezone, datetime_safe
from room.models import RoomModel, BookingRecordModel
from room.serializers import RoomSerializer, BookingRecordSerializer
from decimal import Decimal
from reservation.models import PaymentModel


"""
    Make New Reservation
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_MAKE_RESERVATION) #Only staff that can add/register a new staff
def make_reservation(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new Reservation to database
    try:
        with transaction.atomic():
            staff = StaffModel.objects.get(auth=request.user)
            reservation = ReservationModel(
                reservation_type=data.get("reservation_type"),
                corporate_name=data.get("corporate_name"),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                gender=data.get('gender'),
                phone_number=data.get('phone_number'),
                created_by=StaffModel.objects.get(auth=request.user),
                status=ReservationModel.Status.ACTIVE,
                credit_balance=data.get('credit_balance'),
            )
            reservation.save()
            #Add credit balance payment to history
            if Decimal(reservation.credit_balance) > Decimal(0) :
                narration = "Not available"
                if data.get('credit_channel') == "cash":
                    narration = "Cash collected by: {} {}".format(staff.first_name, staff.last_name)
                elif data.get('credit_channel') == "pos":
                    narration = "Payment made with POS using debit/credit card"
                elif data.get('credit_channel') == "transfer":
                    narration = "Customer made bank transfer with reference id/NO: {}".format(request._POST.get("narration"))
                payment = PaymentModel(
                    reservation=reservation,
                    posted_by=staff,
                    channel=data.get('credit_channel'),
                    amount=reservation.credit_balance,
                    status=PaymentModel.Status.COMPLETED,
                    narration=narration    
                )
                payment.save()

            if data.get("book_room") == "true":
                room = RoomModel.manage.get(id=data.get('room'))

                if room.available < int(data.get('quantity')):
                    return Response(response_maker(response_type='error',message='Avaialble Rooms Less Than Quantity'),status=HTTP_400_BAD_REQUEST)
                #Add Payment to history
                channel = request._POST.get("channel")
                narration = "Not available"
                if request._POST.get("channel") == "cash":
                    narration = "Cash collected by: {} {}".format(staff.first_name, staff.last_name)
                elif request._POST.get("channel") == "pos":
                    narration = "Payment made with POS using debit/credit card"
                elif request._POST.get("channel") == "transfer":
                    narration = "Customer made bank transfer with reference id/NO: {}".format(request._POST.get("narration"))
                payment = PaymentModel(
                    reservation=reservation,
                    posted_by=staff,
                    channel=channel,
                    amount=float(request._POST.get("total_price")),
                    status=PaymentModel.Status.COMPLETED,
                    narration=narration    
                )
                payment.save()

                #Add room booking
                booking = BookingRecordModel(
                    reservation=reservation,
                    room=room,
                    amount=Decimal(float(data.get('quantity'))) * Decimal(float(data.get('days'))) * room.price,
                    quantity=data.get('quantity'),
                    check_in=datetime.now().date(),
                    check_out=datetime.now().date() + timedelta(days=int(data.get("days"))),
                    booked_by=staff,
                    payment=payment,
                    status=ReservationModel.Status.ACTIVE
                )
                booking.save()

                #Add cost to reservation amount spent
                reservation.amount_spent = reservation.amount_spent + Decimal(float(booking.amount))
                reservation.save()
                #Update available room
                room.available = room.available - int(booking.quantity)
                room.save()
            res_serializer = ReservationSerializer(reservation)
        return Response(response_maker(response_type='success',message="Reservation made successfully",data=res_serializer.data),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)


"""
    List reservation: Can also apply filters
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept get request
@use_permission(CAN_VIEW_RESERVATION) #Only staff that can view a new staff
def list_reservation(request, page):
    #Copy dict data
    data = request._POST
    total_reservation = 0
    if int(page) > 1:
        offset = ROWS_PER_PAGE * (int(page)-1)
        limit =  ROWS_PER_PAGE * int(page)
    else:
        offset = 0
        limit = ROWS_PER_PAGE
    

    # Set transaction status
    if data.getlist("status"):
        status_query = data.getlist("status")
    else:
        status_query =  ReservationModel.Status.options

    # Set amount range
    if data.get("minAmount"):
        min = data.get("minAmount")
    else:
        min = 0 

    if data.get("maxAmount"):  
        max = data.get("maxAmount")
    else:
        max = 9223372036854775807 #Arbitrary maximum amount    

        # Set timestamp range 
    if data.get("startDate"):
        start_date = data.get("startDate").split("T")[0]
    else:
        start_date = datetime_safe.datetime(year=1999, month=1, day=1) #datetime(year=1999, month=1, day=1) 

    if data.get("endDate"):  
        end_date = datetime.strptime("{} 23:59:59".format(data.get("endDate").split("T")[0]),"%Y-%m-%d %H:%M:%S")
    else:
        end_date = timezone.now()  

    #Query was sent
    if data.get("keyword",None) and data.get("gender",None):
        reservation_filter = ReservationModel.manage.filter(
            (
                Q(reference=data.get("keyword",None)) |
                Q(first_name__icontains=data.get("keyword",None)) |
                Q(last_name__icontains=data.get("keyword",None)) |
                Q(corporate_name__icontains=data.get("keyword",None)) |
                Q(phone_number=data.get("keyword",None))
            ) 
            &
            (
                Q(gender=data.get("gender",None)) &
                Q(timestamp__range=(start_date,end_date)) &
                Q(amount_spent__range=(min,max)) &
                Q(status__in=status_query)
            )
        ).order_by("-timestamp")
        total_reservation = reservation_filter.count()
        reservation_list = reservation_filter[offset:limit]

    elif data.get("keyword",None) and not(data.get("gender",None)):
        reservation_filter = ReservationModel.manage.filter(
            (
                Q(reference=data.get("keyword",None)) |
                Q(first_name__icontains=data.get("keyword",None)) |
                Q(last_name__icontains=data.get("keyword",None)) |
                Q(corporate_name__icontains=data.get("keyword",None)) |
                Q(phone_number=data.get("keyword",None))
            ) 
            &
            (
                Q(timestamp__range=(start_date,end_date)) &
                Q(amount_spent__range=(min,max)) &
                Q(status__in=status_query)
            )
        ).order_by("-timestamp")
        total_reservation = reservation_filter.count()
        reservation_list = reservation_filter[offset:limit]

    elif not(data.get("keyword",None)) and data.get("gender",None):
        reservation_filter = ReservationModel.manage.filter(
            (
                Q(gender=data.get("gender",None)) &
                Q(timestamp__range=(start_date,end_date)) &
                Q(amount_spent__range=(min,max)) &
                Q(status__in=status_query)
            )
        ).order_by("-timestamp")
        total_reservation = reservation_filter.count()
        reservation_list = reservation_filter[offset:limit]
    else:
        transaction_filter = ReservationModel.manage.filter(
            Q(timestamp__range=(start_date,end_date)) &
            Q(amount_spent__range=(min,max)) &
            Q(status__in=status_query)
        ).order_by("-timestamp")
        total_reservation = transaction_filter.count()
        reservation_list = transaction_filter[offset:limit]
    res_serializer = ReservationSerializer(reservation_list, many=True)
    return Response(response_maker(response_type='success',message='All Reservations',
        count=total_reservation,data=res_serializer.data),status=HTTP_200_OK)


"""
    get Reservation details
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['GET']) #Only accept post request
def get_reservation(request, reference): 

    try:
        reservation = ReservationModel.manage.get(reference=reference, status=ReservationModel.Status.ACTIVE)
        res_serializer = ReservationSerializer(reservation)
        return Response(response_maker(response_type='success',message='Customer Reservations',
            data=res_serializer.data),status=HTTP_200_OK)
    except ReservationModel.DoesNotExist:
        return Response(response_maker(response_type='error',message='Reservation deos not exist or not active'),status=HTTP_400_BAD_REQUEST)
    except Exception:
        return Response(response_maker(response_type='error',message='Unknown internal error'),status=HTTP_400_BAD_REQUEST)

"""
    cancel Reservation
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['GET']) #Only accept post request
@use_permission(CAN_CANCEL_RESERVATION)
def cancel_reservation(request, reference): 
    try:
        with transaction.atomic():
            staff = StaffModel.objects.get(auth=request.user)
            reservation = ReservationModel.manage.get(reference=reference, status=ReservationModel.Status.ACTIVE)
            if (reservation.amount_unpaid <= 0) and (reservation.amount_spent <= 0):
                #Release every room booked on this reservation if possible
                room_bookings = BookingRecordModel.manage.filter(reservation=reservation)
                for booking in room_bookings:
                    if(booking.status == BookingRecordModel.Status.ACTIVE):
                        booking.status = BookingRecordModel.Status.CANCELED
                        booking.save()
                        booking.reservation.amount_spent = booking.reservation.amount_spent - booking.amount
                        booking.reservation.credit_balance = booking.reservation.credit_balance - booking.amount
                        booking.reservation.save()
                        room = RoomModel.manage.get(pk=booking.room.pk)
                        room.available = room.available + int(booking.quantity)
                        room.save()
                reservation = ReservationModel.manage.get(reference=reference)
                reservation.status=ReservationModel.Status.CANCELED
                reservation.save() 
                #Reverse credit balance
                payment = PaymentModel(
                    reservation=reservation,
                    posted_by=staff,
                    channel="direct",
                    amount=reservation.credit_balance,
                    status=PaymentModel.Status.REVERSED,
                    narration="Reversed canceled reservation credit balance"    
                )
                payment.save()
            else:
                return Response(response_maker(response_type='error',message='Can not cancel a reservation with valid orders, use close instead'),status=HTTP_400_BAD_REQUEST)
        return Response(response_maker(response_type='success',message='Customer Reservation Canceled Successfully'),status=HTTP_200_OK)
    except ReservationModel.DoesNotExist:
        return Response(response_maker(response_type='error',message='Reservation deos not exist or not active'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)


"""
    close Reservation
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['GET']) #Only accept post request
@use_permission(CAN_CLOSE_RESERVATION)
def close_reservation(request, reference): 
    try:
        with transaction.atomic():
            staff = StaffModel.objects.get(auth=request.user)
            reservation = ReservationModel.manage.get(reference=reference, status=ReservationModel.Status.ACTIVE)
            if reservation.amount_unpaid <= 0:
                #Release every room booked on this reservation if possible
                room_bookings = BookingRecordModel.manage.filter(reservation=reservation)
                for booking in room_bookings:
                    if(booking.status == BookingRecordModel.Status.ACTIVE):
                        booking.status = BookingRecordModel.Status.CANCELED
                        booking.save()
                        booking.reservation.amount_spent = booking.reservation.amount_spent - booking.amount
                        booking.reservation.credit_balance = booking.reservation.credit_balance - booking.amount
                        booking.reservation.save()
                        room = RoomModel.manage.get(pk=booking.room.pk)
                        room.available = room.available + int(booking.quantity)
                        room.save()
                reservation = ReservationModel.manage.get(reference=reference)
                reservation.status=ReservationModel.Status.CLOSED
                reservation.save() 
                #Reverse credit balance
                if reservation.credit_balance > 0:
                    payment = PaymentModel(
                        reservation=reservation,
                        posted_by=staff,
                        channel="direct",
                        amount=reservation.credit_balance,
                        status=PaymentModel.Status.REVERSED,
                        narration="Reversed closed reservation credit balance"    
                    )
                    payment.save()
                return Response(response_maker(response_type='success',message='Customer Reservation Cloased Successfully'),status=HTTP_200_OK)
            else:
                return Response(response_maker(response_type='error',message='Can not close a reservation with unpaid amount'),status=HTTP_400_BAD_REQUEST)
    except ReservationModel.DoesNotExist:
        return Response(response_maker(response_type='error',message='Reservation deos not exist or not active'),status=HTTP_400_BAD_REQUEST)
    except Exception:
        return Response(response_maker(response_type='error',message='Unknown internal error'),status=HTTP_400_BAD_REQUEST)



"""
    get all active reservation
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['GET']) #Only accept post request
def list_active_reservation(request): 

    try:
        reservation = ReservationModel.manage.filter(status=ReservationModel.Status.ACTIVE)
        res_serializer = ReservationSerializer(reservation, many=True)
        return Response(response_maker(response_type='success',message='Customer Reservations',
            data=res_serializer.data),status=HTTP_200_OK)
    except ReservationModel.DoesNotExist:
        return Response(response_maker(response_type='error',message='Reservation deos not exist or not active'),status=HTTP_400_BAD_REQUEST)
    except Exception:
        return Response(response_maker(response_type='error',message='Unknown internal error'),status=HTTP_400_BAD_REQUEST)
