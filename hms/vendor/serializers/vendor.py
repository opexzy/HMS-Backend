"""
    Vendor Model Serializer
"""

from rest_framework import serializers
from vendor.models import VendorModel

class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorModel
        fields = [
            'id', 
            'name', 
            'address'
        ]