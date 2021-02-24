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
from staff.permission.list import CAN_MANAGE_VENDOR
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
from vendor.models import VendorModel, VendorPaymentModel, SupplyModel, vendor
from vendor.serializers import VendorSerializer, VendorPaymentSerializer, SupplySerializer

"""
    Add New Vendor
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_MANAGE_VENDOR) 
def add_vendor(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new food to database
    try:
        vendor = VendorModel(
           name=data.get("name"),
           address=data.get("address")
        )
        vendor.save()
        vendor_serializer = VendorSerializer(vendor)
        return Response(response_maker(response_type='success',message="Vendor added successfully",data=vendor_serializer.data),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)


"""
    Edit Vendor
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_MANAGE_VENDOR) 
def edit_vendor(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new food to database
    try:
        vendor = VendorModel.manage.get(pk=data.get("id"))
        vendor.name = data.get("name")
        vendor.address = data.get("name")
        vendor.save()
        return Response(response_maker(response_type='success',message="Vendor updated successfully"),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)


"""
    List Vendor: Can also apply filters
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept get request
@use_permission(CAN_MANAGE_VENDOR) 
def list_vendor(request, page):
   #Copy dict data
    data = request._POST
    total_reservation = 0
    if int(page) > 1:
        offset = ROWS_PER_PAGE * (int(page)-1)
        limit =  ROWS_PER_PAGE * int(page)
    else:
        offset = 0
        limit = ROWS_PER_PAGE
    

    #Query was sent
    if data.get("keyword",None):
        reservation_filter =VendorModel.manage.filter(Q(name__icontains=data.get("keyword",None))).order_by("name")
        total_reservation = reservation_filter.count()
        reservation_list = reservation_filter[offset:limit]
    else:
        transaction_filter = VendorModel.manage.all().order_by("name")
        total_reservation = transaction_filter.count()
        reservation_list = transaction_filter[offset:limit]
    res_serializer = VendorSerializer(reservation_list, many=True)
    return Response(response_maker(response_type='success',message='All Vendors',
        count=total_reservation,data=res_serializer.data),status=HTTP_200_OK)

"""
    close Reservation
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_MANAGE_VENDOR) 
def add_supply(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new food to database
    try:
        supply = SupplyModel(
           vendor=VendorModel.manage.get(pk=data.get("vendor")),
           description=data.get("description"),
           status=SupplyModel.Status.UNPAID,
           amount=data.get("amount"),
           amount_unpaid=data.get("amount")
        )
        supply.save()
        supply_serializer = SupplySerializer(supply)
        return Response(response_maker(response_type='success',message="Supply History added successfully",data=supply_serializer.data),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)

"""
    Delete Supply History
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_MANAGE_VENDOR) 
def add_payment(request): 
    #Copy dict data
    data = dict(request._POST)
    #Add new food to database
    try:
        supply = SupplyModel.manage.get(pk=data.get("supply_id"))
        if supply.status == SupplyModel.Status.UNPAID:
            if supply.amount_unpaid >= Decimal(data.get("amount")):
                supply.amount_unpaid = supply.amount_unpaid - Decimal(data.get("amount"))
                if supply.amount_unpaid == 0:
                    supply.status = SupplyModel.Status.PAID
                supply.save()
                #Add to payment
                payment = VendorPaymentModel(
                    supply=supply,
                    posted_by = StaffModel.objects.get(auth=request.user),
                    amount = data.get("amount"),
                    status = VendorPaymentModel.Status.COMPLETED
                )
                payment.save()
                return Response(response_maker(response_type='success',message="Payment made successfully"),status=HTTP_200_OK)
            else:
              return Response(response_maker(response_type='error',message='Amount is greater than amount unpaid'),status=HTTP_400_BAD_REQUEST)  
        else:
              return Response(response_maker(response_type='error',message='This vendor has been paid'),status=HTTP_400_BAD_REQUEST)  
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)

"""
    Add Pyament to Supply History
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['GET']) #Only accept post request
@use_permission(CAN_MANAGE_VENDOR) 
def delete_supply(request, id): 

    try:
        supply = SupplyModel.manage.get(pk=id)
        payment = VendorPaymentModel.manage.filter(supply=supply).delete()
        supply.delete()
        return Response(response_maker(response_type='success',message="Supply History removed successfully"),status=HTTP_200_OK)
    except KeyError:
        return Response(response_maker(response_type='error',message='Bad Request Parameter'),status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)


"""
    List Supply: Can also apply filters
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept get request
@use_permission(CAN_MANAGE_VENDOR) 
def list_supply(request, page):
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
        status_query =  SupplyModel.Status.options

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
        reservation_filter = SupplyModel.manage.filter(
            (
                Q(vendor__name__icontains=data.get("keyword",None)) |
                Q(description__icontains=data.get("keyword",None))
            ) 
            &
            (
                Q(date_created__range=(start_date,end_date)) &
                Q(amount__range=(min,max)) &
                Q(status__in=status_query)
            )
        ).order_by("-date_created")
        total_reservation = reservation_filter.count()
        reservation_list = reservation_filter[offset:limit]
    else:
        transaction_filter = SupplyModel.manage.filter(
            Q(date_created__range=(start_date,end_date)) &
            Q(amount__range=(min,max)) &
            Q(status__in=status_query)
        ).order_by("-date_created")
        total_reservation = transaction_filter.count()
        reservation_list = transaction_filter[offset:limit]
    res_serializer = SupplySerializer(reservation_list, many=True)
    return Response(response_maker(response_type='success',message='All Supply Histories',
        count=total_reservation,data=res_serializer.data),status=HTTP_200_OK)

"""
    List Supply Payment: Can also apply filters
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept get request
@use_permission(CAN_MANAGE_VENDOR) 
def list_payment(request, page):
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
        status_query =  VendorPaymentModel.Status.options

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
        reservation_filter = VendorPaymentModel.manage.filter(
            (
                Q(supply__vendor__name__icontains=data.get("keyword",None)) |
                Q(supply__description__icontains=data.get("keyword",None))
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
        reservation_filter = VendorPaymentModel.manage.filter(
                Q(timestamp__range=(start_date,end_date)) &
                Q(amount__range=(min,max)) &
                Q(status__in=status_query)
        ).order_by("-timestamp")
        total_reservation = reservation_filter.count()
        reservation_list = reservation_filter[offset:limit]
    res_serializer = VendorPaymentSerializer(reservation_list, many=True)
    return Response(response_maker(response_type='success',message='All Supply Payment Histories',
        count=total_reservation,data=res_serializer.data),status=HTTP_200_OK)


"""
    List All vendors
"""
@api_view(['GET']) #Only accept get request
def all_vendors(request):
    vendor = VendorModel.manage.all()
    vendor_serializer = VendorSerializer(vendor, many=True)
    return Response(response_maker(response_type='success',message='All Vendors',data=vendor_serializer.data),status=HTTP_200_OK)