"""
    Payment Model Serializer
"""

from rest_framework import serializers
from reservation.models import PaymentModel
from .vendor import VendorSerializer

class VendorPaymentSerializer(serializers.ModelSerializer):
    
    posted_by = serializers.SerializerMethodField("get_posted_by")

    class Meta:
        model = PaymentModel
        fields = [
            'id', 
            'supply', 
            'posted_by',
            'amount', 
            'status',
            'timestamp'
        ]

    def get_posted_by(self, obj):
        if obj.posted_by:
            return "{} {}".format(obj.posted_by.first_name, obj.posted_by.last_name)
        else:
            return None