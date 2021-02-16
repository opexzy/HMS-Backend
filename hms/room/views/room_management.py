from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from utils.randstr import get_token
from utils.api_helper import response_maker, request_data_normalizer, getlistWrapper
from staff.permission import use_permission, CAN_ADD_ROOM, CAN_VIEW_ROOM, CAN_BOOK_ROOM, CAN_VIEW_BOOKING
from django.db import transaction
from hms.settings import ROWS_PER_PAGE
from django.db.models import Q, F
from reservation.models import ReservationModel
from reservation.models.reservation import STATUS_OPTIONS
from datetime import date, datetime, timedelta
from django.utils import timezone, datetime_safe
from room.models import RoomModel, BookingRecordModel
from room.serializers import RoomSerializer, BookingRecordSerializer
from decimal import Decimal

"""
    Add New Room
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_ADD_ROOM) #Only staff that can add new room
def add_room(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new Room to database
    try:
        room = RoomModel(
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price'),
            start_no=data.get('start_no'),
            end_no=data.get('end_no'),
            available=int(data.get('end_no')) - int(data.get('start_no')) + 1,
        )
        room.save()
        room_serializer = RoomSerializer(room)
        return Response(response_maker(response_type='success',message="Room added successfully",data=room_serializer.data),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)


"""
    List room: Can also apply filters
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept get request
@use_permission(CAN_VIEW_ROOM) 
def list_room(request, page):
    #Copy dict data
    data = request._POST
    total_room = 0
    if int(page) > 1:
        offset = ROWS_PER_PAGE * (int(page)-1)
        limit =  ROWS_PER_PAGE * int(page)
    else:
        offset = 0
        limit = ROWS_PER_PAGE
    
    # Set amount range
    if data.get("minAmount"):
        min = data.get("minAmount")
    else:
        min = 0 

    if data.get("maxAmount"):  
        max = data.get("maxAmount")
    else:
        max = 9223372036854775807 #Arbitrary maximum amount    

    #Query was sent
    if data.get("keyword",None):
        room_filter = RoomModel.manage.filter(
            (
                Q(name__icontains=data.get("keyword",None)) &
                Q(price__range=(min,max))
            )
        ).order_by("name")
        total_room = room_filter.count()
        room_list = room_filter[offset:limit]

    else:
        room_filter = RoomModel.manage.filter(
            (
                Q(price__range=(min,max))
            )
        ).order_by("name")
        total_room = room_filter.count()
        room_list = room_filter[offset:limit]
    room_serializer = RoomSerializer(room_list, many=True)
    return Response(response_maker(response_type='success',message='All Rooms',
        count=total_room,data=room_serializer.data),status=HTTP_200_OK)


"""
    Update User
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
#@use_permission(CAN_EDIT_STAFF) #Only staff that can view a new staff
def update_room(request): 
    #Copy dict data
    data = dict(request._POST)
    try:
        room = RoomModel.manage.get(pk=data.get("id",None))
        try:
            room.name = data.get("name", None)
            room.description = data.get("description", None)
            room.price = data.get("price", None)
            room.start_no = data.get("start_no", None)
            room.end_no = data.get("end_no", None)
            room.available = data.get("available", None)
            room.save()
            #TODO: Send mail informing staff about new profile updates
            return Response(response_maker(response_type='success',message='Room updated successfully'),status=HTTP_200_OK)
        except Exception as e:
            return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)
    except RoomModel.DoesNotExist as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)

"""
    Book a Room
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_BOOK_ROOM) #Only staff that can add new room
def book_room(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new Room to database
    try:
        with transaction.atomic():
            reservation = ReservationModel.manage.get(reference=data.get('reference'), status=ReservationModel.Status.ACTIVE)
            room = RoomModel.manage.get(id=data.get('id'))

            if room.available < int(data.get('quantity')):
                return Response(response_maker(response_type='error',message='Avaialble Rooms Less Than Quantity'),status=HTTP_400_BAD_REQUEST)
            #Add room booking
            booking = BookingRecordModel(
                reservation=reservation,
                room=room,
                amount=data.get('amount'),
                quantity=data.get('quantity'),
                check_in=datetime.now().date(),
                check_out=datetime.now().date() + timedelta(days=int(data.get("days"))),
                status=ReservationModel.Status.ACTIVE
            )
            booking.save()
            #Add cost to reservation amount spent
            reservation.amount_spent = reservation.amount_spent + Decimal(float(booking.amount))
            reservation.save()
            #Update available room
            room.available = room.available - int(booking.quantity)
            room.save()
        return Response(response_maker(response_type='success',message="Room Booked successfully"),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except ReservationModel.DoesNotExist:
        return Response(response_maker(response_type='error',message="Reservation is not active or does not exist"),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)


"""
    List Room Booking: Can also apply filters
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept get request
@use_permission(CAN_VIEW_BOOKING) #Only staff that can view a new staff
def list_booking(request, page):
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
        status_query =  BookingRecordModel.Status.options

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
        reservation_filter = BookingRecordModel.manage.filter(
            (
                Q(reservation__reference=data.get("keyword",None)) |
                Q(reservation__first_name__icontains=data.get("keyword",None)) |
                Q(reservation__last_name__icontains=data.get("keyword",None)) |
                Q(reservation__phone_number=data.get("keyword",None)) |
                Q(room__name__icontains=data.get("keyword",None))
            ) 
            &
            (
                Q(timestamp__range=(start_date,end_date)) &
                Q(amount__range=(min,max)) &
                Q(status__in=status_query)
            )
        ).order_by("-timestamp")
        total_reservation = reservation_filter.count()
        reservation_list = reservation_filter[offset:limit]
    else:
        transaction_filter = BookingRecordModel.manage.filter(
            Q(timestamp__range=(start_date,end_date)) &
            Q(amount__range=(min,max)) &
            Q(status__in=status_query)
        ).order_by("-timestamp")
        total_reservation = transaction_filter.count()
        reservation_list = transaction_filter[offset:limit]
    res_serializer = BookingRecordSerializer(reservation_list, many=True)
    return Response(response_maker(response_type='success',message='All Rooms',
        count=total_reservation,data=res_serializer.data),status=HTTP_200_OK)


"""
    List All Rooms
"""
@api_view(['GET']) #Only accept get request
def all_rooms(request):
    rooms = RoomModel.manage.all()
    room_serializer = RoomSerializer(rooms, many=True)
    return Response(response_maker(response_type='success',message='All Rooms',data=room_serializer.data),status=HTTP_200_OK)