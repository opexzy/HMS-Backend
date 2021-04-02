from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from utils.randstr import get_otp
import datetime
from hms_auth.models import AuthTokenModel
from staff.models import StaffModel
from staff.serializers import StaffSerializer
from staff.permission import get_staff_permission
from utils.api_helper import request_data_normalizer
from hms.settings import EXPIRING_TOKEN_DURATION, PAYSTACK_SEC_KEY

""" The login function for admin authentication returns an authentication token """

#@request_data_normalizer
@api_view(['POST']) #Only accept post request
@permission_classes((AllowAny,)) #Allow both authenticated and not authenticated request
def login(request):
    data = request.POST
    email = data.get('email', False)
    password = data.get('password', False)
    #check if both email or password is set
    if not email or not password:
        return Response({'message': 'Please provide both email and password'},status=HTTP_400_BAD_REQUEST)
    else:
        user = authenticate(email=email, password=password)
        if not user:
             return Response({'message': 'Incorrect email or password'},status=HTTP_404_NOT_FOUND)
        else:
            #Check if account is active
            if not user.is_active:
                return Response({'message': 'This account has been decativated, contact Administrator'},status=HTTP_404_NOT_FOUND)
            #Delete previous token from this user
            try:
                AuthTokenModel.objects.select_related('user').get(user=user).delete()
            except AuthTokenModel.DoesNotExist:
                pass
            staff = StaffModel.objects.get(auth=user)
            serializer = StaffSerializer(staff)
            token, _ = AuthTokenModel.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user':serializer.data, 'message':'Login successful!'},status=HTTP_200_OK)


""" Validate login token """
@api_view(['GET'])
@permission_classes((IsAuthenticated,)) #Allow only authenticated  request
def validate_token(request):
    #This actually does nothing than to return authenticated user instance, permissions and all office location
    staff = StaffModel.objects.get(auth=request.user)
    serializer = StaffSerializer(staff)
    return Response({
        'user':serializer.data, 
        'permissions':get_staff_permission(staff), 
    }, status=HTTP_200_OK)

"""Update Password"""
@api_view(['POST'])
@permission_classes((IsAuthenticated,)) #Allow only authenticated  request
def update_password(request):
    data = request.POST
    password = data.get('password', False)
    password_verify = data.get('password_verify', False)
    try:
        if (len(password) >= 6) and (password == password_verify):
            request.user.set_password(password)
            request.user.save()
            return Response({'message': 'Password Changed Successfully'},status=HTTP_200_OK)
        else:
            return Response({'message': 'Password must be six characters or more and must match'},status=HTTP_400_BAD_REQUEST)
    except Exception:
         return Response({'message': 'An unknown internal Error occured'},status=HTTP_400_BAD_REQUEST)

