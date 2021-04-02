from re import error
from django.db.models.aggregates import Sum
from django.db.models.query import InstanceCheckMeta
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
from staff.permission.list import CAN_PLACE_DRINK_ORDER
from utils.randstr import get_token
from utils.api_helper import response_maker, request_data_normalizer, getlistWrapper
from staff.permission import use_permission, CAN_ADD_FOOD, CAN_VIEW_FOOD, CAN_EDIT_FOOD, CAN_PLACE_FOOD_ORDER, CAN_VIEW_FOOD_ORDER
from django.db import transaction
from hms.settings import ROWS_PER_PAGE
from django.db.models import Q, F
from reservation.models import ReservationModel, OrderModel
from reservation.models.reservation import STATUS_OPTIONS
from datetime import date, datetime, timedelta
from django.utils import timezone, datetime_safe
from kitchen.models import FoodModel, FoodOrderModel
from bar.models import DrinkModel, DrinkOrderModel
from room.models import BookingRecordModel, RoomModel
from kitchen.serializers import FoodSerializer, FoodOrderSerializer
from bar.serializers import DrinkOrderSerializer
from decimal import Decimal
from reservation.exception import QuantityOutOfRange
from reservation.models import PaymentModel
from options.models import OptionModel
from options.serializer import OptionSerializer

"""
    Make Quick Order
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission([CAN_PLACE_FOOD_ORDER, CAN_PLACE_DRINK_ORDER])
def quick_order(request, reference): 
    #Copy dict data
    data = request._POST.getlist("orders")
    #Add new Order to database
    try:
        with transaction.atomic():
            reservation = ReservationModel.manage.get(reference=reference, status=ReservationModel.Status.ACTIVE)
            staff = StaffModel.objects.get(auth=request.user)

            if(request._POST.get("client", None)):
                client = request._POST.get("client")
            else:
                client = ""
            #Check payment method
            payment_status = False
            channel = ""
            narration = "Not Available"
            if request._POST.get("payment_method") == "credit_balance":
                #Check if credit balance is enough to pay
                if reservation.credit_balance >= Decimal(float(request._POST.get("total_amount"))):
                    reservation.credit_balance = reservation.credit_balance - Decimal(float(request._POST.get("total_amount")))
                    reservation.amount_spent = reservation.amount_spent + Decimal(float(request._POST.get("total_amount")))
                    payment_status = True
                    channel = "direct",
                    narration = "Payment made from available credit balance"
                else:
                    return Response(response_maker(response_type='error',message='Insufficient Credit Balance'),status=HTTP_400_BAD_REQUEST)
            elif request._POST.get("payment_method") == "instant_pay":
                reservation.amount_spent = reservation.amount_spent + Decimal(float(request._POST.get("total_amount")))
                payment_status = True
                channel = request._POST.get("channel")
                if request._POST.get("channel") == "cash":
                    narration = "Cash collected by: {} {}".format(staff.first_name, staff.last_name)
                elif request._POST.get("channel") == "pos":
                    narration = "Payment made with POS using debit/credit card"
                elif request._POST.get("channel") == "transfer":
                    narration = "Customer made bank transfer with reference id/NO: {}".format(request._POST.get("narration"))
            else:
                reservation.amount_spent = reservation.amount_spent + Decimal(float(request._POST.get("total_amount")))
                reservation.amount_unpaid = reservation.amount_unpaid + Decimal(float(request._POST.get("total_amount")))
                payment_status = False
            reservation.save()
            #Add payment to payment history
            if payment_status:
                payment = PaymentModel(
                    reservation=reservation,
                    posted_by=staff,
                    channel=channel,
                    amount=float(request._POST.get("total_amount")),
                    status=PaymentModel.Status.COMPLETED,
                    narration=narration    
                )
                payment.save()
            else:
                payment = None
            order_ref = OrderModel(amount=request._POST.get("total_amount"), client=client)
            order_ref.save()        
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
                        payment=payment,
                        order=order_ref,
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
                        payment=payment,
                        order=order_ref,
                        status=DrinkOrderModel.Status.PENDING
                    ).save()
                    #Deduct qauntity from food model
                    if drink.available < int(order.get("quantity")):
                        raise QuantityOutOfRange
                    drink.available = int(drink.available) - int(order.get("quantity"))
                    drink.save()
            return Response(response_maker(response_type='success',message="Order Placed successfully", data={
                "order_ref":order_ref.order_ref,"order_date":timezone.now()}),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except ReservationModel.DoesNotExist:
        return Response(response_maker(response_type='error',message="Reservation is not active or does not exist"),status=HTTP_400_BAD_REQUEST)
    except QuantityOutOfRange:
        return Response(response_maker(response_type='error',message="Quantity out of available item range"),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)


"""
    List order History: Can also apply filters
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept get request
def get_my_orders(request):
    #Copy dict data
    data = request._POST
    try:
        staff = StaffModel.objects.get(pk=data.get("staff"))
    except StaffModel.DoesNotExist:
        staff = None

    # Set order status
    if data.get("status") == 'all':
        status_query = FoodOrderModel.Status.options
    else:
        status_query = [data.get("status")] 

        # Set timestamp range 
    if data.get("start_date"):
        start_date = data.get("start_date").split("T")[0]
    else:
        start_date = timezone.now().date() #datetime(year=1999, month=1, day=1) 

    if data.get("end_date"):  
        end_date = datetime.strptime("{} 23:59:59".format(data.get("end_date").split("T")[0]),"%Y-%m-%d %H:%M:%S")
    else:
        end_date = timezone.now()  

    food_order_filter = FoodOrderModel.manage.filter(
        (
            Q(registered_by=staff) | 
            Q(completed_by=staff)) 
        &
        (
            Q(timestamp__range=(start_date,end_date)) & 
            Q(status__in=status_query)
        )
    ).order_by("-timestamp")
    
    drink_order_filter = DrinkOrderModel.manage.filter(
        (
            Q(registered_by=staff) | 
            Q(completed_by=staff)
        ) 
        &
        (
            Q(timestamp__range=(start_date,end_date)) & 
            Q(status__in=status_query)
        )
    ).order_by("-timestamp")
    
    total_drink = drink_order_filter.aggregate(total_drink=Sum("amount"))["total_drink"]
    total_food = food_order_filter.aggregate(total_food=Sum("amount"))["total_food"]
    return Response(response_maker(response_type='success',message='All Payment',data={
        "total_drink":total_drink,
        "total_food": total_food,
        "food_orders":FoodOrderSerializer(food_order_filter,many=True).data,
        "drink_orders":DrinkOrderSerializer(drink_order_filter,many=True).data
    }),status=HTTP_200_OK)


"""
    List food and drink group
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['GET']) #Only accept get request
def list_groups(request):
    group = OptionModel.manage.all()
    food_group = group.exclude(name="drink")
    drink_group = group.exclude(name="food")
    return Response(response_maker(response_type='success',message='All Payment',data={
        "food_group": OptionSerializer(food_group, many=True).data,
        "drink_group": OptionSerializer(drink_group, many=True).data
    }),status=HTTP_200_OK)