from re import error
from django.db.models.aggregates import Sum
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from room.models.room import RoomModel
from staff.models.staff import StaffModel
from staff.permission.list import CAN_VIEW_PAYMENT_HISTORY
from utils.randstr import get_token
from utils.api_helper import response_maker, request_data_normalizer, getlistWrapper
from staff.permission import use_permission, CAN_MAKE_PAYMENT
from django.db import transaction
from hms.settings import ROWS_PER_PAGE
from django.db.models import Q, F
from reservation.models import ReservationModel, PaymentModel
from reservation.serializers import ReservationSerializer, PaymentSerializer
from reservation.models.reservation import STATUS_OPTIONS
from datetime import date, datetime, timedelta
from django.utils import timezone, datetime_safe
from kitchen.models import FoodModel, FoodOrderModel
from kitchen.serializers import FoodSerializer, FoodOrderSerializer
from bar.models import DrinkOrderModel
from bar.serializers import DrinkOrderSerializer
from kitchen.serializers import FoodOrderSerializer
from room.models import BookingRecordModel
from room.serializers import RoomSerializer, BookingRecordSerializer
from decimal import Decimal

"""
    get Reservation details
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['GET']) #Only accept post request
def get_invoice(request, reference): 
    try:
        reservation = ReservationModel.manage.get(reference=reference)
        food_orders = FoodOrderModel.manage.filter(reservation=reservation)
        drink_orders = DrinkOrderModel.manage.filter(reservation=reservation)
        room_bookings = BookingRecordModel.manage.filter(reservation=reservation)

        #Get invoice amounts
        food = food_orders.aggregate(total_food=Sum("amount"))
        drink = drink_orders.aggregate(total_drink=Sum("amount"))
        room = room_bookings.aggregate(total_room=Sum("amount"))

        res_serializer = ReservationSerializer(reservation)
        food_serializer = FoodOrderSerializer(food_orders, many=True)
        drink_serializer = DrinkOrderSerializer(drink_orders, many=True)
        room_serializer = BookingRecordSerializer(room_bookings, many=True)

        return Response(response_maker(response_type='success',message='Reservation Invoice',
            data={
                "customer": res_serializer.data,
                "food": food_serializer.data,
                "drink": drink_serializer.data,
                "room": room_serializer.data,
                "total_food":food['total_food'],
                "total_drink":drink['total_drink'],
                "total_room":room['total_room'],
                "amount_paid": reservation.amount_spent - reservation.amount_unpaid,
                "amount_unpaid":reservation.amount_unpaid,
            }),status=HTTP_200_OK)
    except StaffModel.DoesNotExist:
        return Response(response_maker(response_type='error',message='Reservation deos not exist'),status=HTTP_400_BAD_REQUEST)
    

"""
    Make Payment
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_MAKE_PAYMENT)
def make_payment(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new Reservation to database
    try:
        reservation = ReservationModel.manage.get(reference=data.get("reference"))
        if reservation.status == ReservationModel.Status.CHECKED_OUT:
            return Response(response_maker(response_type='success',message="Reservation has been previously checked out"),status=HTTP_400_BAD_REQUEST)
        if float(data.get('amount')) <= 0:
            return Response(response_maker(response_type='success',message="Amount can not be less than or equal zero"),status=HTTP_400_BAD_REQUEST)
        staff = StaffModel.objects.get(auth=request.user)
        channel = data.get("channel")
        narration = "Not Available"
        if data.get("channel") == "cash":
            narration = "Cash collected by: {} {}".format(staff.first_name, staff.last_name)
        elif data.get("channel") == "pos":
            narration = "Payment made with POS using debit/credit card"
        elif data.get("channel") == "direct":
            narration = "Payment made from available credit balance"
        elif data.get("channel") == "transfer":
            narration = "Customer made bank transfer with reference id/NO: {}".format(data.get("narration"))
        with transaction.atomic(): 
            payment = PaymentModel(
                reservation=reservation,
                posted_by=staff,
                channel=data.get('channel'),
                amount=float(data.get('amount')),
                status=PaymentModel.Status.COMPLETED,  
                narration=narration 
            )
            payment.save()

            if reservation.amount_unpaid < Decimal(float(data.get('amount'))):
                excess_amount = Decimal(float(data.get('amount'))) - reservation.amount_unpaid
                reservation.amount_unpaid = 0
            else:
                excess_amount = 0
                reservation.amount_unpaid = reservation.amount_unpaid - Decimal(float(data.get('amount')))
            if payment.channel == PaymentModel.Channel.DIRECT:
                reservation.credit_balance = 0 + excess_amount
            else:
                reservation.credit_balance = reservation.credit_balance + excess_amount
            if reservation.amount_unpaid <= 0:
                reservation.status = ReservationModel.Status.CHECKED_OUT
                #Relase every room booked on this reservation
                room_bookings = BookingRecordModel.manage.filter(reservation=reservation)
                for booking in room_bookings:
                    room = RoomModel.manage.get(pk=booking.room.pk)
                    room.available = room.available + int(booking.quantity)
                    room.save()
            reservation.save()
        res_serializer = ReservationSerializer(reservation)
        return Response(response_maker(response_type='success',message="Payment made successfully",data=res_serializer.data),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)



"""
    List payment history: Can also apply filters
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept get request
@use_permission(CAN_VIEW_PAYMENT_HISTORY)
def list_payment(request, page):
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
        status_query =  PaymentModel.Status.options

    # Set transaction channel
    if data.getlist("channel"):
        channel_query = data.getlist("channel")
    else:
        channel_query =  PaymentModel.Channel.options
    
    

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
    if data.get("keyword",None):
        reservation_filter = PaymentModel.manage.filter(
            (
                Q(reservation__reference=data.get("keyword",None)) |
                Q(reservation__first_name__icontains=data.get("keyword",None)) |
                Q(reservation__last_name__icontains=data.get("keyword",None)) |
                Q(reservation__phone_number=data.get("keyword",None)) |
                Q(posted_by__auth__email=data.get("keyword",None))
            ) 
            &
            (
                Q(timestamp__range=(start_date,end_date)) &
                Q(amount__range=(min,max)) &
                Q(status__in=status_query) &
                Q(channel__in=channel_query)
            )
        ).order_by("-timestamp")
        total_reservation = reservation_filter.count()
        reservation_list = reservation_filter[offset:limit]
    else:
        transaction_filter = PaymentModel.manage.filter(
            Q(timestamp__range=(start_date,end_date)) &
            Q(amount__range=(min,max)) &
            Q(status__in=status_query) &
            Q(channel__in=channel_query)
        ).order_by("-timestamp")
        total_reservation = transaction_filter.count()
        reservation_list = transaction_filter[offset:limit]
    res_serializer = PaymentSerializer(reservation_list, many=True)
    return Response(response_maker(response_type='success',message='All Payment',
        count=total_reservation,data=res_serializer.data),status=HTTP_200_OK)


"""
    get payment reports
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
def get_payment_report(request): 
    #Copy dict data
    data = dict(request._POST)
    if data.get("status") == 'all':
        status = PaymentModel.Status.options
    else:
        status = [data.get("status")]

    # Set timestamp range 
    if data.get("start_date"):
        start_date = data.get("start_date").split("T")[0]
    else:
        start_date = datetime_safe.datetime(year=1999, month=1, day=1) #datetime(year=1999, month=1, day=1) 

    if data.get("end_date"):  
        end_date = datetime.strptime("{} 23:59:59".format(data.get("end_date").split("T")[0]),"%Y-%m-%d %H:%M:%S")
    else:
        end_date = timezone.now()
    reversed_payments = orders = PaymentModel.manage.filter(
        Q(timestamp__range=(start_date,end_date)) &
        Q(status=PaymentModel.Status.REVERSED)
    )
    total_reversed = reversed_payments.aggregate(total_amount=Sum("amount"))["total_amount"]

    try:
        orders = PaymentModel.manage.filter(
            Q(timestamp__range=(start_date,end_date)) &
            Q(status__in=status)
        )
        if data.get("display") != "all":
            orders = orders.filter(
                Q(posted_by=StaffModel.objects.get(auth=request.user))
            )
        #Get total count & total_amount
        count = orders.count()
        total_amount = orders.aggregate(total_amount=Sum("amount"))["total_amount"]
        order_serializer = PaymentSerializer(orders, many=True)
        return Response(response_maker(response_type='success',message='All Payments',
            data={
                "count": count,
                "total_amount": total_amount,
                "total_reversed": total_reversed,
                "data": order_serializer.data,
            }),status=HTTP_200_OK)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)