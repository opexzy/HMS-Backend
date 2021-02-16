"""
    Auth Model Serializer
"""

from rest_framework import serializers
from reservation.models import ReservationModel

class ReservationSerializer(serializers.ModelSerializer):
    
    created_by = serializers.SerializerMethodField("get_created_by")

    class Meta:
        model = ReservationModel
        fields = [
            'id', 
            'reference',
            'reservation_type',
            'corporate_name',
            'first_name', 
            'last_name',
            'gender', 
            'phone_number', 
            'created_by', 
            'status',
            'credit_balance',
            'amount_spent',
            'amount_unpaid',
            'timestamp'
        ]

    def get_created_by(self, obj):
        if obj.created_by:
            return "{} {}".format(obj.created_by.first_name, obj.created_by.last_name)
        else:
            return None