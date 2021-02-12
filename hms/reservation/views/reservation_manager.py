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
from utils.randstr import get_token
from utils.api_helper import response_maker, request_data_normalizer, getlistWrapper
from staff.permission import use_permission, CAN_MAKE_RESERVATION, CAN_VIEW_RESERVATION
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
        reservation = ReservationModel(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            gender=data.get('gender'),
            phone_number=data.get('phone_number'),
            created_by=StaffModel.objects.get(auth=request.user),
            status=ReservationModel.Status.ACTIVE,
            credit_balance=data.get('credit_balance'),
        )
        reservation.save()
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
        reservation = ReservationModel.manage.get(reference=reference)
        res_serializer = ReservationSerializer(reservation)
        return Response(response_maker(response_type='success',message='Customer Reservations',
            data=res_serializer.data),status=HTTP_200_OK)
    except Exception:
        return Response(response_maker(response_type='error',message='Reservation deos not exist'),status=HTTP_400_BAD_REQUEST)

