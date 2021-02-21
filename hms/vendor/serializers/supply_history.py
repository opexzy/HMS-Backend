"""
    Payment Model Serializer
"""

from rest_framework import serializers
from reservation.models import PaymentModel
from .vendor import VendorSerializer

class SupplySerializer(serializers.ModelSerializer):
    
    vendor = VendorSerializer()

    class Meta:
        model = PaymentModel
        fields = [
            'id', 
            'vendor', 
            'channel',
            'amount', 
            'status',
            'amount_unpaid',
            'date_created'
        ]