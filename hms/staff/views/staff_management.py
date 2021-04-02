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
from staff.permission import use_permission, CAN_ADD_STAFF, CAN_VIEW_STAFF, CAN_EDIT_STAFF, CAN_VIEW_STAFF_SALES
from hms_auth.models import AuthModel
from staff.models import StaffModel
from django.db import transaction
from staff.serializers import StaffSerializer
from hms.settings import ROWS_PER_PAGE
from django.db.models import Q, F
from hms_auth.models.auth import IS_ACTIVE_OPTIONS

"""
    Register new staff
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_ADD_STAFF) #Only staff that can add/register a new staff
def register_staff(request): 
    #Copy dict data
    data = dict(request._POST)
    if data.get('email',False) and data.get('password',False):
        #Check if email already exist in authentication table.
        if AuthModel.manage.is_valid_new_auth(data.get('email',None)):
            #Email does not exist let's create a new authentication data
            try:
                password = data.get('password')
                with transaction.atomic():
                    #create auth revord
                    auth = AuthModel(
                        email=data.get('email'),
                        is_staff=True
                    )
                    auth.set_password(password)
                    auth.save()
                    #create staff record
                    staff = StaffModel(
                        auth=auth,
                        first_name=data.get('first_name'),
                        last_name=data.get('last_name'),
                        gender=data.get('gender'),
                        phone_number=data.get('phone_number'),
                        position=data.get('position')
                    )
                    staff.save()
            except Exception as e:
                return Response(response_maker(response_type='error',message="An unknown error has occured, please try again"),status=HTTP_400_BAD_REQUEST)
            staff_serializer = StaffSerializer(staff)
            #TODO: Send an email containing the password and user infomation to the registered mail
            return Response(response_maker(response_type='success',message="Staff added successfully; Give staff some permissions",data=staff_serializer.data),status=HTTP_200_OK)
        else:
            return Response(response_maker(response_type='error',message='An account with this email already exists'),status=HTTP_400_BAD_REQUEST)
    else:
        return Response(response_maker(response_type='error',message='Email is required!'),status=HTTP_400_BAD_REQUEST)


"""
    List staffs: Can also apply filters
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept get request
@use_permission(CAN_VIEW_STAFF) #Only staff that can view a new staff
def list_staff(request, page):
    #Copy dict data
    data = request._POST
    total_staff = 0
    if int(page) > 1:
        offset = ROWS_PER_PAGE * (int(page)-1)
        limit =  ROWS_PER_PAGE * int(page)
    else:
        offset = 0
        limit = ROWS_PER_PAGE
    if data.getlist("status"):
        status_query = []
        count = 0
        for status in data.getlist("status"):
            if status == 'active':
                status_query.insert(count,True)
            elif status == 'inactive':
                status_query.insert(count,False)
            else:
                pass
        count=+count
    else:
        status_query = IS_ACTIVE_OPTIONS
            
    #Query was sent
    if data.get("keyword",None)  and data.get("gender",None):
        staff_filter = StaffModel.objects.filter(
            (
                Q(first_name__icontains=data.get("keyword",None)) |
                Q(last_name__icontains=data.get("keyword",None)) |
                Q(auth__email=data.get("keyword",None)) |
                Q(phone_number=data.get("keyword",None)) |
                Q(position__icontains=data.get("keyword",None))
            ) 
            &
            (
                Q(gender=data.get("gender",None)) &
                Q(auth__is_active__in=status_query)
            )
        ).distinct()
        total_staff= staff_filter.count()
        staff_list = staff_filter[offset:limit]
    elif data.get("keyword",None) and not(data.get("gender",None)):
        staff_filter = StaffModel.objects.filter(
            (
                Q(first_name__icontains=data.get("keyword",None)) |
                Q(last_name__icontains=data.get("keyword",None)) |
                Q(auth__email=data.get("keyword",None)) |
                Q(phone_number=data.get("keyword",None)) |
                Q(position__icontains=data.get("keyword",None))
            ) 
            &
            (
                Q(auth__is_active__in=status_query) 
            )
        ).distinct()
        total_staff= staff_filter.count()
        staff_list = staff_filter[offset:limit]
    elif not(data.get("keyword",None)) and data.get("gender",None):
        staff_filter = StaffModel.objects.filter(
            Q(gender=data.get("gender",None)) &
            Q(auth__is_active__in=status_query)
        ).distinct()
        total_staff = staff_filter.count()
        staff_list = staff_filter[offset:limit]
    else:
        staff_filter = StaffModel.objects.filter(
            Q(auth__is_active__in=status_query)
        ).distinct()
        total_staff= staff_filter.count()
        staff_list = staff_filter[offset:limit]
    staff_serializer = StaffSerializer(staff_list, many=True)
    return Response(response_maker(response_type='success',message='All staffs',
        count=total_staff,data=staff_serializer.data),status=HTTP_200_OK)


"""
    Update Staff
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_EDIT_STAFF) #Only staff that can view a new staff
def update_staff(request): 
    #Copy dict data
    data = dict(request._POST)
    try:
        staff = StaffModel.objects.get(pk=data.get("id",None))
        try:
            staff.first_name = data.get("first_name", None)
            staff.last_name = data.get("last_name", None)
            staff.gender = data.get("gender", None)
            staff.phone_number = data.get("phone_number", None)
            staff.position = data.get("position", None)
            staff.save()
            #TODO: Send mail informing staff about new profile updates
            return Response(response_maker(response_type='success',message='Staff Profile updated successfully'),status=HTTP_200_OK)
        except Exception:
            return Response(response_maker(response_type='error',message='Request not understood'),status=HTTP_400_BAD_REQUEST)
    except StaffModel.DoesNotExist:
        return Response(response_maker(response_type='error',message='Request not understood'),status=HTTP_400_BAD_REQUEST)

"""
    Update staff password
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_EDIT_STAFF) #Only staff that can view a new staff
def update_password(request): 
    #Copy dict data
    data = dict(request._POST)
    try:
        staff = StaffModel.objects.get(pk=data.get("id",None))
        try:
            if (len(data.get("password")) >= 6) and (data.get("password") == data.get("password_verify")):
                staff.auth.set_password(data.get("password"))
                staff.auth.save()
                #TODO: Send mail informing staff about new profile updates
                return Response(response_maker(response_type='success',message='Staff Password updated successfully'),status=HTTP_200_OK)
            else:
                return Response(response_maker(response_type='error',message='Password must be 6 characters or more and must match'),status=HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(response_maker(response_type='error',message='Request not understood'),status=HTTP_400_BAD_REQUEST)
    except StaffModel.DoesNotExist:
        return Response(response_maker(response_type='error',message='Request not understood'),status=HTTP_400_BAD_REQUEST)


"""
    Update staff status
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
@use_permission(CAN_EDIT_STAFF) #Only staff that can view a new staff
def update_status(request): 
    #Copy dict data
    data = dict(request._POST)
    try:
        auth = AuthModel.manage.get(pk=data.get("auth_id", None))
        if data.get("status", None) == "active":
            auth.is_active = True
            auth.save()
        else:
            auth.is_active = False
            auth.save()
        return Response(response_maker(response_type='success',message='Status updated successfully'),status=HTTP_200_OK)
    except AuthModel.DoesNotExist:
        return Response(response_maker(response_type='error',message='Request not understood'),status=HTTP_400_BAD_REQUEST)


"""
    List All Staffs
"""
@api_view(['GET']) #Only accept get request
@use_permission(CAN_VIEW_STAFF_SALES) #Only staff that can view a new staff
def all_staffs(request):
    staffs = StaffModel.objects.all()
    staff_serializer = StaffSerializer(staffs, many=True)
    return Response(response_maker(response_type='success',message='All Staffs',data=staff_serializer.data),status=HTTP_200_OK)