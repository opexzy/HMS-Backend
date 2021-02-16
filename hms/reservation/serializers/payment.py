"""
    Payment Model Serializer
"""

from rest_framework import serializers
from reservation.models import PaymentModel
from .reservation import ReservationSerializer

class PaymentSerializer(serializers.ModelSerializer):
    
    posted_by = serializers.SerializerMethodField("get_posted_by")
    reservation = ReservationSerializer()

    class Meta:
        model = PaymentModel
        fields = [
            'id', 
            'reservation', 
            'posted_by', 
            'channel',
            'amount', 
            'amount_paid', 
            'amount_unpaid', 
            'status',
            'narration',
            'timestamp'
        ]

    def get_posted_by(self, obj):
        if obj.posted_by:
            return "{} {}".format(obj.posted_by.first_name, obj.posted_by.last_name)
        else:
            return None