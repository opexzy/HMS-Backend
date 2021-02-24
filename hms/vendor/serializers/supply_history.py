"""
    Payment Model Serializer
"""

from rest_framework import serializers
from vendor.models import SupplyModel
from .vendor import VendorSerializer

class SupplySerializer(serializers.ModelSerializer):
    
    vendor = VendorSerializer()

    class Meta:
        model = SupplyModel
        fields = [
            'id', 
            'vendor',
            'description',
            'amount', 
            'status',
            'amount_unpaid',
            'date_created'
        ]