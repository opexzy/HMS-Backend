from json.encoder import JSONEncoder
from os import name
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
from hms_auth.models import auth
from staff.permission import (use_permission,has_permission)
from utils.api_helper import response_maker, request_data_normalizer, getlistWrapper
from options.models import OptionModel, options
from options.serializer import OptionSerializer
from json import JSONDecoder, decoder

"""
    get foods
"""
@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
def get_options(request): 
    #Copy dict data
    data = dict(request._POST)

@request_data_normalizer #Normalize request POST and GET data
@api_view(['GET']) #Only accept post request
def get_groups(request, name):
    try:
        option = OptionModel.manage.filter(name=name)
        option_serializer = OptionSerializer(option, many=True)
        return Response(response_maker(response_type='success',message='All {} Group'.format(name),
            data=option_serializer.data),status=HTTP_200_OK)
    except Exception:
        return Response(response_maker(response_type='error',message='Unknown Internal Error'),status=HTTP_400_BAD_REQUEST)


@request_data_normalizer #Normalize request POST and GET data
@api_view(['POST']) #Only accept post request
def add_group(request, name):
    data = request._POST
    try:
        option = OptionModel(name=name, value=data.get("group_name"))
        option.save()
        option = OptionModel.manage.filter(name=name)
        option_serializer = OptionSerializer(option, many=True)
        return Response(response_maker(response_type='success',message='Group Saved Successfully',
            data=option_serializer.data),status=HTTP_200_OK)
    except Exception as e:
        return Response(response_maker(response_type='error',message=str(e)),status=HTTP_400_BAD_REQUEST)