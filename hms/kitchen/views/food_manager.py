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
from staff.models.staff import StaffModel
from staff.permission.list import CAN_CANCEL_RESERVATION
from utils.randstr import get_token
from utils.api_helper import response_maker, request_data_normalizer, getlistWrapper
from staff.permission import (
    use_permission, 
    has_permission, 
    CAN_ADD_FOOD, 
    CAN_VIEW_FOOD, 
    CAN_EDIT_FOOD, 
    CAN_PLACE_FOOD_ORDER, 
    CAN_VIEW_FOOD_ORDER,
    CAN_CANCEL_ORDER)
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
from reservation.models import PaymentModel

"""
    Add New Room
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_ADD_FOOD) #Only staff that can add new food
def add_food(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new food to database
    try:
        food = FoodModel(
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price'),
            metric=data.get('metric'),
            available=data.get('available')
        )
        food.save()
        food_serializer = FoodSerializer(food)
        return Response(response_maker(response_type='success',message="Food added successfully",data=food_serializer.data),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)


"""
    List food: Can also apply filters
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept get request
@use_permission(CAN_VIEW_FOOD)
def list_food(request, page):
    #Copy dict data
    data = request._POST
    total_food = 0
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
        food_filter = FoodModel.manage.filter(
            (
                Q(name__icontains=data.get("keyword",None)) &
                Q(price__range=(min,max))
            )
        ).order_by("name")
        total_food = food_filter.count()
        food_list = food_filter[offset:limit]

    else:
        food_filter = FoodModel.manage.filter(
            (
                Q(price__range=(min,max))
            )
        ).order_by("name")
        total_food = food_filter.count()
        food_list = food_filter[offset:limit]
    food_serializer = FoodSerializer(food_list, many=True)
    return Response(response_maker(response_type='success',message='All Foods',
        count=total_food,data=food_serializer.data),status=HTTP_200_OK)


"""
    Update User
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_EDIT_FOOD) #Only staff that can view a new staff
def update_food(request): 
    #Copy dict data
    data = dict(request._POST)
    try:
        room = FoodModel.manage.get(pk=data.get("id",None))
        try:
            room.name = data.get("name", None)
            room.description = data.get("description", None)
            room.price = data.get("price", None)
            room.metric = data.get("metric", None)
            room.available = data.get("available", None)
            room.save()
            return Response(response_maker(response_type='success',message='Food updated successfully'),status=HTTP_200_OK)
        except Exception as e:
            return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)
    except FoodModel.DoesNotExist as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)

"""
    Order a Food
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_PLACE_FOOD_ORDER)
def order_food(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new Room to database
    try:
        with transaction.atomic():
            reservation = ReservationModel.manage.get(reference=data.get('reference'), status=ReservationModel.Status.ACTIVE)
            food = FoodModel.manage.get(id=data.get('id'))

            if food.available < int(data.get('quantity')):
                return Response(response_maker(response_type='error',message='Avaialble Food Less Than Quantity'),status=HTTP_400_BAD_REQUEST)
            #Add Food Order
            if data.get("order_mode") == "direct":
                order = FoodOrderModel(
                    reservation=reservation,
                    food=food,
                    amount=data.get('amount'),
                    quantity=data.get('quantity'),
                    completed_by=StaffModel.objects.get(auth=request.user),
                    status=FoodOrderModel.Status.COMPLETED
                )
            else:
                order = FoodOrderModel(
                    reservation=reservation,
                    food=food,
                    amount=data.get('amount'),
                    quantity=data.get('quantity'),
                    registered_by=StaffModel.objects.get(auth=request.user),
                    status=FoodOrderModel.Status.PENDING
                )
            order.save()
            #Add cost to reservation amount spent
            reservation.amount_spent = reservation.amount_spent + Decimal(float(order.amount))
            reservation.amount_unpaid = reservation.amount_unpaid + Decimal(float(order.amount))
            reservation.save()
            #Update available room
            food.available = food.available - int(order.quantity)
            food.save()
        return Response(response_maker(response_type='success',message="Food Order Placed successfully"),status=HTTP_200_OK)
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
@use_permission(CAN_VIEW_FOOD_ORDER) #Only staff that can view a new staff
def list_order(request, page):
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
        status_query =  FoodOrderModel.Status.options

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
        reservation_filter = FoodOrderModel.manage.filter(
            (
                Q(id=data.get("keyword",None)) |
                Q(reservation__reference=data.get("keyword",None)) |
                Q(reservation__first_name__icontains=data.get("keyword",None)) |
                Q(reservation__last_name__icontains=data.get("keyword",None)) |
                Q(reservation__phone_number=data.get("keyword",None)) |
                Q(registered_by__auth__email=data.get("keyword",None)) |
                Q(food__name=data.get("keyword",None))
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
        transaction_filter = FoodOrderModel.manage.filter(
            Q(timestamp__range=(start_date,end_date)) &
            Q(amount__range=(min,max)) &
            Q(status__in=status_query)
        ).order_by("-timestamp")
        total_reservation = transaction_filter.count()
        reservation_list = transaction_filter[offset:limit]
    res_serializer = FoodOrderSerializer(reservation_list, many=True)
    return Response(response_maker(response_type='success',message='All Food Orders',
        count=total_reservation,data=res_serializer.data),status=HTTP_200_OK)


"""
    get all foods
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['GET']) #Only accept post request
def get_all_foods(request): 
    try:
        food = FoodModel.manage.all()
        food_serializer = FoodSerializer(food, many=True)
        return Response(response_maker(response_type='success',message='All Foods',
            data=food_serializer.data),status=HTTP_200_OK)
    except Exception:
        return Response(response_maker(response_type='error',message='Unknown Internal Error'),status=HTTP_400_BAD_REQUEST)

"""
    Update food order status
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_PLACE_FOOD_ORDER)
def update_order(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new Room to database
    try:
        with transaction.atomic():
            food_order = FoodOrderModel.manage.get(id=data.get('id'))
            staff = StaffModel.objects.get(auth=request.user)
            if food_order.status == FoodOrderModel.Status.PENDING:
                if data.get("status") == FoodOrderModel.Status.COMPLETED:
                    food_order.status = FoodOrderModel.Status.COMPLETED
                    food_order.completed_by = staff
                    food_order.save()
                elif data.get("status") == FoodOrderModel.Status.CANCELED:
                    if has_permission(request.user,CAN_CANCEL_ORDER):
                        food_order.status = FoodOrderModel.Status.CANCELED
                        food_order.completed_by = staff
                        food_order.save()
                        #Upadte available food in the food model
                        food_order.food.available = food_order.food.available + food_order.quantity
                        food_order.food.save()
                        #Update amount spent
                        food_order.reservation.amount_spent = food_order.reservation.amount_spent - food_order.amount
                        if food_order.payment:
                            #Return amount back to credit balance
                            food_order.reservation.amount_unpaid = food_order.reservation.amount_unpaid - food_order.amount
                            #Create reversal payment history
                            payment = PaymentModel(
                                reservation=food_order.reservation,
                                posted_by=staff,
                                channel='direct',
                                amount=food_order.amount,
                                status=PaymentModel.Status.REVERSED,
                                narration="Payment reversal for food order with id: {}".format(food_order.id) 
                            )
                            payment.save()
                        else:
                            food_order.reservation.amount_unpaid = food_order.reservation.amount_unpaid - food_order.amount
                        food_order.reservation.save()
                    else:
                        return Response(response_maker(response_type='error',message='Permission Denied!'),status=HTTP_400_BAD_REQUEST)
                else:
                    return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
                return Response(response_maker(response_type='success',message="Food Order Canceled successfully"),status=HTTP_200_OK)
            else:
                return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
            #Add Food Order
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)



"""
    get food order reports
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
def get_order_report(request): 
    #Copy dict data
    data = dict(request._POST)
    if data.get("status") == 'all':
        status = FoodOrderModel.Status.options
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
    
    try:
        orders = FoodOrderModel.manage.filter(
            Q(timestamp__range=(start_date,end_date)) &
            Q(status__in=status)
        )
        if data.get("display") != "all":
            orders = orders.filter(
                Q(registered_by=StaffModel.objects.get(auth=request.user)) |
                Q(completed_by=StaffModel.objects.get(auth=request.user))
            )
        #Get total count & total_amount
        count = orders.count()
        total_amount = orders.aggregate(total_amount=Sum("amount"))["total_amount"]
        order_serializer = FoodOrderSerializer(orders, many=True)
        return Response(response_maker(response_type='success',message='All Food Orders',
            data={
                "count": count,
                "total_amount": total_amount,
                "data": order_serializer.data,
            }),status=HTTP_200_OK)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)