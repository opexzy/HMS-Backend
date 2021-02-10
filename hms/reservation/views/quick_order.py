from re import error
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from staff.models.staff import StaffModel
from utils.randstr import get_token
from utils.api_helper import response_maker, request_data_normalizer, getlistWrapper
from staff.permission import use_permission, CAN_ADD_FOOD, CAN_VIEW_FOOD, CAN_EDIT_FOOD, CAN_PLACE_FOOD_ORDER, CAN_VIEW_FOOD_ORDER
from django.db import transaction
from hms.settings import ROWS_PER_PAGE
from django.db.models import Q, F
from reservation.models import ReservationModel
from reservation.models.reservation import STATUS_OPTIONS
from datetime import date, datetime, timedelta
from django.utils import timezone, datetime_safe
from kitchen.models import FoodModel, FoodOrderModel
from kitchen.serializers import FoodSerializer, FoodOrderSerializer
from decimal import Decimal

"""
    Make Quick Order
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
#@use_permission(CAN_PLACE_FOOD_ORDER)
def quick_order(request, reference): 
    #Copy dict data
    data = dict(request._POST)
    print(str(data))
    exit()
    #Add new Room to database
    try:
        with transaction.atomic():
            reservation = ReservationModel.manage.get(reference=data.get('reference'))
            food = FoodModel.manage.get(id=data.get('id'))

            if food.available < int(data.get('quantity')):
                return Response(response_maker(response_type='error',message='Avaialble Food Less Than Quantity'),status=HTTP_400_BAD_REQUEST)
            #Add Food Order
            if data.get("order_mode") == "direct":
                status = FoodOrderModel.Status.COMPLETED
            else:
                status = FoodOrderModel.Status.PENDING
            order = FoodOrderModel(
                reservation=reservation,
                food=food,
                amount=data.get('amount'),
                quantity=data.get('quantity'),
                registered_by=StaffModel.objects.get(auth=request.user),
                status=status
            )
            order.save()
            #Add cost to reservation amount spent
            reservation.amount_spent = reservation.amount_spent + Decimal(float(order.amount))
            reservation.save()
            #Update available room
            food.available = food.available - int(order.quantity)
            food.save()
        return Response(response_maker(response_type='success',message="Food Order Placed successfully"),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)