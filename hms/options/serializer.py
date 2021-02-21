"""
    Option Model Serializer
"""

from rest_framework import serializers
from options.models import OptionModel
from json import JSONDecoder

class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = OptionModel
        fields = [
            'id', 
            'name', 
            'value'
        ]