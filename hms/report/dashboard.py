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
from bar.models.drink import DrinkModel
from staff.models import staff
from staff.permission.list import CAN_CLOSE_RESERVATION, CAN_OVERRIDE_RESERVATION
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
from kitchen.models import FoodOrderModel, FoodModel
from bar.models import DrinkOrderModel


"""
    Make New Reservation
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['GET']) #Only accept post request
@permission_classes((AllowAny,)) #Allow only authenticated  request
def dashboard(request): 
    start = timezone.now().date()
    end = timezone.now()

    #Total sales today
    food = FoodOrderModel.manage.filter(Q(status=FoodOrderModel.Status.COMPLETED) & Q(timestamp__range=(start,end)))
    total_food_count = food.count()
    total_food_amount = food.aggregate(total_amount=Sum("amount"))["total_amount"]

    drink = DrinkOrderModel.manage.filter(Q(status=DrinkOrderModel.Status.COMPLETED) & Q(timestamp__range=(start,end)))
    total_drink_count = drink.count()
    total_drink_amount = drink.aggregate(total_amount=Sum("amount"))["total_amount"]

    #Total Reservations Today
    total_reservations = ReservationModel.manage.filter(status=ReservationModel.Status.ACTIVE).count()
    
    #Drinks in stock
    drinks_instock = DrinkModel.manage.all().aggregate(total_drinks=Sum("available"))["total_drinks"]

    #Foods in stock
    foods_instock = FoodModel.manage.all().aggregate(total_foods=Sum("available"))["total_foods"]

    #Available Rooms
    rooms_available = RoomModel.manage.all().aggregate(total_available=Sum("available"))["total_available"]

    #Customer balances
    customers_balances = ReservationModel.manage.filter(status=ReservationModel.Status.ACTIVE).aggregate(total_amount=Sum("credit_balance"))["total_amount"]

    return Response(response_maker(response_type='success',message="Dashboard Summary", 
        data={
            "total_food_count":total_food_count,
            "total_food_amount":total_food_amount,
            "total_drink_count":total_drink_count,
            "total_drink_amount":total_drink_amount,
            "total_reservations":total_reservations,
            "drinks_instock":drinks_instock,
            "foods_instock":foods_instock,
            "rooms_available":rooms_available,
            "customers_balances":customers_balances,
        }),status=HTTP_200_OK)
    