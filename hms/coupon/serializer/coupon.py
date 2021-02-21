"""
    Coupon Model Serializer
"""

from rest_framework import serializers
from coupon.models import CouponModel

class CouponSerializer(serializers.ModelSerializer):
    
    reference = serializers.SerializerMethodField("get_reference")
    reservation_type = serializers.SerializerMethodField("get_reservation_type")
    corporate_name = serializers.SerializerMethodField("get_corporate_name")
    first_name = serializers.SerializerMethodField("get_first_name")
    last_name = serializers.SerializerMethodField("get_last_name")

    class Meta:
        model = CouponModel
        fields = [
            'id', 
            'reference',
            'reservation_type',
            'corporate_name',  
            'first_name',
            'last_name',
            'code',
            'discount',
            'status',
            'date_created',
            'date_used'
        ]

    def get_reference(self, obj):
        if obj.reservation:
            return obj.reservation.reference
        else:
            return None

    def get_reservation_type(self, obj):
        if obj.reservation:
            return obj.reservation.reservation_type
        else:
            return None
    
    def get_corporate_name(self, obj):
        if obj.reservation:
            return obj.reservation.corporate_name
        else:
            return None

    def get_first_name(self, obj):
        if obj.reservation:
            return obj.reservation.first_name
        else:
            return None

    def get_last_name(self, obj):
        if obj.reservation:
            return obj.reservation.last_name
        else:
            return None