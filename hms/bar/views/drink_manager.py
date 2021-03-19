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
from options.models.options import OptionModel
from staff.models.staff import StaffModel
from utils.randstr import get_token
from utils.api_helper import response_maker, request_data_normalizer, getlistWrapper
from staff.permission import (
    use_permission, 
    has_permission, 
    CAN_ADD_DRINK, 
    CAN_VIEW_DRINK, 
    CAN_EDIT_DRINK, 
    CAN_PLACE_DRINK_ORDER, 
    CAN_VIEW_DRINK_ORDER,
    CAN_CANCEL_ORDER
    )
from django.db import transaction
from hms.settings import ROWS_PER_PAGE
from django.db.models import Q, F
from reservation.models import ReservationModel, OrderModel
from reservation.models.reservation import STATUS_OPTIONS
from datetime import date, datetime, timedelta
from django.utils import timezone, datetime_safe
from bar.models import DrinkModel, DrinkOrderModel
from bar.serializers import DrinkSerializer, DrinkOrderSerializer
from decimal import Decimal
from reservation.models import PaymentModel

"""
    Add New Room
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_ADD_DRINK) #Only staff that can add new food
def add_drink(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new food to database
    try:
        drink = DrinkModel(
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price'),
            metric=data.get('metric'),
            available=data.get('available'),
            group= OptionModel.manage.get(pk=data.get('group')),
        )
        drink.save()
        drink_serializer = DrinkSerializer(drink)
        return Response(response_maker(response_type='success',message="Drink added successfully",data=drink_serializer.data),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)


"""
    List Drink: Can also apply filters
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept get request
@use_permission(CAN_VIEW_DRINK)
def list_drink(request, page):
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
        food_filter = DrinkModel.manage.filter(
            (
                Q(name__icontains=data.get("keyword",None)) &
                Q(price__range=(min,max))
            )
        ).order_by("name")
        total_food = food_filter.count()
        food_list = food_filter[offset:limit]

    else:
        food_filter = DrinkModel.manage.filter(
            (
                Q(price__range=(min,max))
            )
        ).order_by("name")
        total_food = food_filter.count()
        food_list = food_filter[offset:limit]
    food_serializer = DrinkSerializer(food_list, many=True)
    return Response(response_maker(response_type='success',message='All Drinks',
        count=total_food,data=food_serializer.data),status=HTTP_200_OK)


"""
    Update User
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_EDIT_DRINK)
def update_drink(request): 
    #Copy dict data
    data = dict(request._POST)
    try:
        room = DrinkModel.manage.get(pk=data.get("id",None))
    
        try:
            room.name = data.get("name", None)
            room.description = data.get("description", None)
            room.price = data.get("price", None)
            room.metric = data.get("metric", None)
            room.available = data.get("available", None)
            room.group = OptionModel.manage.get(pk=data.get('group'))
            room.save()
            return Response(response_maker(response_type='success',message='Drink updated successfully'),status=HTTP_200_OK)
        except Exception as e:
            return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)
    except DrinkModel.DoesNotExist as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)

"""
    Order a Drink
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_PLACE_DRINK_ORDER)
def order_drink(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new Room to database
    try:
        with transaction.atomic():
            reservation = ReservationModel.manage.get(reference=data.get('reference'), status=ReservationModel.Status.ACTIVE)
            drink = DrinkModel.manage.get(id=data.get('id'))

            if drink.available < int(data.get('quantity')):
                return Response(response_maker(response_type='error',message='Avaialble Drinks Less Than Quantity'),status=HTTP_400_BAD_REQUEST)
            #Create Order reference
            order_ref = OrderModel(amount=data.get('amount'))
            order_ref.save()
            #Add Food Order
            if data.get("order_mode") == "direct":
                order = DrinkOrderModel(
                    reservation=reservation,
                    drink=drink,
                    amount=data.get('amount'),
                    quantity=data.get('quantity'),
                    completed_by=StaffModel.objects.get(auth=request.user),
                    order= order_ref,
                    status=DrinkOrderModel.Status.COMPLETED
                )
            else:
                order = DrinkOrderModel(
                    reservation=reservation,
                    drink=drink,
                    amount=data.get('amount'),
                    quantity=data.get('quantity'),
                    registered_by=StaffModel.objects.get(auth=request.user),
                    order= order_ref,
                    status=DrinkOrderModel.Status.PENDING
                )
            order.save()
            #Add cost to reservation amount spent
            reservation.amount_spent = reservation.amount_spent + Decimal(float(order.amount))
            reservation.amount_unpaid = reservation.amount_unpaid + Decimal(float(order.amount))
            reservation.save()
            #Update available room
            drink.available = drink.available - int(order.quantity)
            drink.save()
        return Response(response_maker(response_type='success',message="Drink Order Placed successfully"),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except ReservationModel.DoesNotExist:
        return Response(response_maker(response_type='error',message="Reservation is not active or does not exist"),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)


"""
    List Drink Order: Can also apply filters
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept get request
@use_permission(CAN_VIEW_DRINK_ORDER)
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
        status_query =  DrinkOrderModel.Status.options

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
        reservation_filter = DrinkOrderModel.manage.filter(
            (
                Q(order__order_ref=data.get("keyword",None)) |
                Q(reservation__reference=data.get("keyword",None)) |
                Q(reservation__first_name__icontains=data.get("keyword",None)) |
                Q(reservation__last_name__icontains=data.get("keyword",None)) |
                Q(reservation__phone_number=data.get("keyword",None)) |
                Q(registered_by__auth__email=data.get("keyword",None)) |
                Q(drink__name=data.get("keyword",None))
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
        transaction_filter = DrinkOrderModel.manage.filter(
            Q(timestamp__range=(start_date,end_date)) &
            Q(amount__range=(min,max)) &
            Q(status__in=status_query)
        ).order_by("-timestamp")
        total_reservation = transaction_filter.count()
        reservation_list = transaction_filter[offset:limit]
    res_serializer = DrinkOrderSerializer(reservation_list, many=True)
    return Response(response_maker(response_type='success',message='All Drink Orders',
        count=total_reservation,data=res_serializer.data),status=HTTP_200_OK)

"""
    get all drinks
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['GET']) #Only accept post request
def get_all_drinks(request): 
    try:
        drink = DrinkModel.manage.all()
        drink_serializer = DrinkSerializer(drink, many=True)
        return Response(response_maker(response_type='success',message='All Drink',
            data=drink_serializer.data),status=HTTP_200_OK)
    except Exception:
        return Response(response_maker(response_type='error',message='Unknown Internal Error'),status=HTTP_400_BAD_REQUEST)


"""
    Update drink order status
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_VIEW_DRINK_ORDER)
def update_order(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new Room to database
    try:
        with transaction.atomic():
            drink_order = DrinkOrderModel.manage.get(id=data.get('id'))
            staff = StaffModel.objects.get(auth=request.user)
            if drink_order.status == DrinkOrderModel.Status.PENDING:
                if data.get("status") == DrinkOrderModel.Status.COMPLETED:
                    drink_order.status = DrinkOrderModel.Status.COMPLETED
                    drink_order.completed_by = staff
                    drink_order.save()
                elif data.get("status") == DrinkOrderModel.Status.CANCELED:
                    if has_permission(request.user,CAN_CANCEL_ORDER):
                        drink_order.status = DrinkOrderModel.Status.CANCELED
                        drink_order.completed_by = staff
                        drink_order.save()
                        #Upadte available food in the food model
                        drink_order.drink.available = drink_order.drink.available + drink_order.quantity
                        drink_order.drink.save()
                        #Update amount spent
                        drink_order.reservation.amount_spent = drink_order.reservation.amount_spent - drink_order.amount
                        if drink_order.payment:
                            #Return amount back to credit balance
                            drink_order.reservation.credit_balance = drink_order.reservation.credit_balance + drink_order.amount
                            #Create reversal payment history
                            #payment = PaymentModel(
                                #reservation=drink_order.reservation,
                                #posted_by=staff,
                                #channel='direct',
                                #amount=drink_order.amount,
                                #status=PaymentModel.Status.REVERSED,
                                #narration="Payment reversal for drink order with id: {}".format(drink_order.id) 
                            #)
                            #payment.save()
                        else:
                            drink_order.reservation.amount_unpaid = drink_order.reservation.amount_unpaid - drink_order.amount
                        drink_order.reservation.save()
                    else:
                        return Response(response_maker(response_type='error',message='Permission Denied!'),status=HTTP_400_BAD_REQUEST)
                else:
                    return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
                return Response(response_maker(response_type='success',message="Drink Order Canceled successfully"),status=HTTP_200_OK)
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
        status = DrinkOrderModel.Status.options
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
        orders = DrinkOrderModel.manage.filter(
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
        order_serializer = DrinkOrderSerializer(orders, many=True)
        return Response(response_maker(response_type='success',message='All Drink Orders',
            data={
                "count": count,
                "total_amount": total_amount,
                "data": order_serializer.data,
            }),status=HTTP_200_OK)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)

"""
    Get all pending drink orders count
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['GET']) #Only accept post request
def get_pending_drink_order(request): 
    try:
        count = DrinkOrderModel.manage.filter(status=DrinkOrderModel.Status.PENDING).count()
        return Response(response_maker(response_type='success',message='All Drink Count',
            count=count),status=HTTP_200_OK)
    except Exception:
        return Response(response_maker(response_type='error',message='Unknown Internal Error'),status=HTTP_400_BAD_REQUEST)



"""
    Get all drinks by group
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['GET']) #Only accept post request
def get_drink_by_group(request, group_id): 
    try:
        group = OptionModel.manage.get(pk=group_id)
        foods = DrinkModel.manage.filter(group=group)
        return Response(response_maker(response_type='success',message='All Drink in Group',
            data=DrinkSerializer(foods, many=True).data),status=HTTP_200_OK)
    except Exception:
        return Response(response_maker(response_type='error',message='Unknown Internal Error'),status=HTTP_400_BAD_REQUEST)