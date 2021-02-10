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
from utils.randstr import get_token
from utils.api_helper import response_maker, request_data_normalizer, getlistWrapper
from staff.permission import use_permission, CAN_ADD_FOOD, CAN_VIEW_FOOD, CAN_EDIT_FOOD, CAN_PLACE_FOOD_ORDER, CAN_VIEW_FOOD_ORDER
from django.db import transaction
from hms.settings import ROWS_PER_PAGE
from django.db.models import Q, F
from reservation.models import ReservationModel
from reservation.serializers import ReservationSerializer
from reservation.models.reservation import STATUS_OPTIONS
from datetime import date, datetime, timedelta
from django.utils import timezone, datetime_safe
from kitchen.models import FoodModel, FoodOrderModel
from kitchen.serializers import FoodSerializer, FoodOrderSerializer
from bar.models import DrinkOrderModel
from kitchen.serializers import FoodOrderSerializer
from room.models import BookingRecordModel
from room.serializers import RoomSerializer
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
        room_bookings = RoomModel.manage.filter(reservation=reservation)

        #Get invoice amounts
        food = food_orders.aggregate(total_food=Sum("amount"))
        drink = drink_orders.aggregate(total_drink=Sum("amount"))
        room = room_bookings.aggregate(total_room=Sum("amount"))

        res_serializer = ReservationSerializer(reservation)
        food_serializer = FoodOrderSerializer(food_orders, many=True)
        drink_serializer = FoodOrderSerializer(drink_orders, many=True)
        room_serializer = FoodOrderSerializer(room_bookings, many=True)

        return Response(response_maker(response_type='success',message='Reservation Invoice',
            data={
                "customer": res_serializer.data,
                "food": food_serializer.data,
                "drink": drink_serializer.data,
                "room": room_serializer.data,
                "total_food":food.total_food,
                "total_drink":drink.total_drink,
                "total_room":room.total_room,
            }),status=HTTP_200_OK)
    except StaffModel.DoesNotExist:
        return Response(response_maker(response_type='error',message='Reservation deos not exist'),status=HTTP_400_BAD_REQUEST)

