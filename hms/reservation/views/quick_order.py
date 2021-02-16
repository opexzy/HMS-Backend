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
from bar.models import DrinkModel, DrinkOrderModel
from room.models import BookingRecordModel, RoomModel
from kitchen.serializers import FoodSerializer, FoodOrderSerializer
from decimal import Decimal
from reservation.exception import QuantityOutOfRange

"""
    Make Quick Order
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
#@use_permission(CAN_PLACE_FOOD_ORDER)
def quick_order(request, reference): 
    #Copy dict data
    data = request._POST.getlist("orders")
    #Add new Room to database
    try:
        with transaction.atomic():
            reservation = ReservationModel.manage.get(reference=reference, status=ReservationModel.Status.ACTIVE)
            staff = StaffModel.objects.get(auth=request.user)
            #Register order as pending in database
            for order in data:
                if order.get("type") == "foods":
                    food = FoodModel.manage.get(pk=order.get("id"))
                    FoodOrderModel(
                        reservation=reservation,
                        food=food,
                        amount=order.get("price"),
                        quantity=order.get("quantity"),
                        registered_by=staff,
                        status=FoodOrderModel.Status.PENDING
                    ).save()
                    #Deduct qauntity from food model
                    if food.available < int(order.get("quantity")):
                        raise QuantityOutOfRange
                    food.available = int(food.available) - int(order.get("quantity"))
                    food.save()
                elif order.get("type") == "drinks":
                    drink = DrinkModel.manage.get(pk=order.get("id"))
                    DrinkOrderModel(
                        reservation=reservation,
                        drink=drink,
                        amount=order.get("price"),
                        quantity=order.get("quantity"),
                        registered_by=staff,
                        status=DrinkOrderModel.Status.PENDING
                    ).save()
                    #Deduct qauntity from food model
                    if drink.available < int(order.get("quantity")):
                        raise QuantityOutOfRange
                    drink.available = int(drink.available) - int(order.get("quantity"))
                    drink.save()
            reservation.amount_spent = reservation.amount_spent + Decimal(float(request._POST.get("total_amount")))
            reservation.save()
            return Response(response_maker(response_type='success',message="Order Placed successfully"),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except ReservationModel.DoesNotExist:
        return Response(response_maker(response_type='error',message="Reservation is not active or does not exist"),status=HTTP_400_BAD_REQUEST)
    except QuantityOutOfRange:
        return Response(response_maker(response_type='error',message="Quantity out of available item range"),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)