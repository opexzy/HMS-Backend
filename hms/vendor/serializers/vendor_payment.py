"""
    Payment Model Serializer
"""

from rest_framework import serializers
from vendor.models import VendorPaymentModel
from .supply_history import SupplySerializer

class VendorPaymentSerializer(serializers.ModelSerializer):
    
    posted_by = serializers.SerializerMethodField("get_posted_by")
    supply = SupplySerializer()

    class Meta:
        model = VendorPaymentModel()
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