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
from reservation.models import reservation
from staff.models.staff import StaffModel
from utils.randstr import get_token
from utils.api_helper import response_maker, request_data_normalizer, getlistWrapper
from staff.permission import (
    use_permission, 
    has_permission, 
    CAN_ADD_COUPON,
    CAN_VIEW_COUPON
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
from coupon.models import CouponModel
from coupon.serializer import CouponSerializer

"""
    Add New Room
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_ADD_COUPON) #Only staff that can add new food
def add_coupon(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new food to database
    try:
        coupon = CouponModel(
           discount=data.get("discount")
        )
        coupon.save()
        coupon_serializer = CouponSerializer(coupon)
        return Response(response_maker(response_type='success',message="Coupon added successfully",data=coupon_serializer.data),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)


"""
    List food: Can also apply filters
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept get request
@use_permission(CAN_VIEW_COUPON)
def list_coupon(request, page):
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
        status_query =  CouponModel.Status.options

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
        reservation_filter = CouponModel.manage.filter(
            (
                Q(code=data.get("keyword",None)) |
                Q(reservation__reference=data.get("keyword",None))
            ) 
            &
            (
                Q(date_created__range=(start_date,end_date)) &
                Q(status__in=status_query)
            )
        ).order_by("-id")
        total_reservation = reservation_filter.count()
        reservation_list = reservation_filter[offset:limit]
    else:
        transaction_filter = CouponModel.manage.filter(
            Q(date_created__range=(start_date,end_date)) &
            Q(status__in=status_query)
        ).order_by("-id")
        total_reservation = transaction_filter.count()
        reservation_list = transaction_filter[offset:limit]
    res_serializer = CouponSerializer(reservation_list, many=True)
    return Response(response_maker(response_type='success',message='All Food Coupons',
        count=total_reservation,data=res_serializer.data),status=HTTP_200_OK)

"""
    close Reservation
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['GET']) #Only accept post request
@use_permission(CAN_VIEW_COUPON)
def delete_coupon(request, code): 
    try:
        coupon = CouponModel.manage.get(code=code, status=CouponModel.Status.ACTIVE)
        coupon.delete()
        return Response(response_maker(response_type='success',message='Coupon Closed Successfully'),status=HTTP_200_OK)
    except ReservationModel.DoesNotExist:
        return Response(response_maker(response_type='error',message='Coupon deos not exist or not active'),status=HTTP_400_BAD_REQUEST)
    except Exception:
        return Response(response_maker(response_type='error',message='Unknown internal error'),status=HTTP_400_BAD_REQUEST)


"""
    close Reservation
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_VIEW_COUPON)
def claim_coupon(request): 
    data = (request._POST)
    try:
        staff = StaffModel.objects.get(auth=request.user)
        coupon = CouponModel.manage.get(code=data.get("coupon_code"), status=CouponModel.Status.ACTIVE)
        reservation = ReservationModel.manage.get(reference=data.get("reference"))
        #Check if reservation has a coupon already
        try:
            CouponModel.manage.get(reservation=reservation)
            return Response(response_maker(response_type='error',message='This Reservation has a coupon already'),status=HTTP_400_BAD_REQUEST)
        except CouponModel.DoesNotExist:
            #Continue
            coupon.reservation = reservation
            coupon.status = CouponModel.Status.USED
            coupon.date_used = timezone.now()
            coupon.save()
            #Apply coupon on reservation
            if reservation.amount_spent > 0:
                discounted_amount = reservation.amount_spent * (coupon.discount/100)
                if reservation.amount_unpaid >= discounted_amount:
                   reservation.amount_unpaid = reservation.amount_unpaid - discounted_amount
                else:
                    reservation.amount_unpaid = 0
                    reservation.credit_balance = discounted_amount - reservation.amount_unpaid
                reservation.save()
                #add to payment history
                payment = PaymentModel(
                    reservation=reservation,
                    posted_by=staff,
                    channel=PaymentModel.Channel.COUPON,
                    amount=discounted_amount,
                    status=PaymentModel.Status.COMPLETED,
                    narration="Coupon payment at {}{} of total amount spent".format(coupon.discount, "%")    
                )
                payment.save()
        return Response(response_maker(response_type='success',message='Coupon applied Successfully'),status=HTTP_200_OK)
    except CouponModel.DoesNotExist:
        return Response(response_maker(response_type='error',message='Coupon deos not exist or not active'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)