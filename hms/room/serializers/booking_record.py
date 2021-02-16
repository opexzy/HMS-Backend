"""
    Booking Record Model Serializer
"""

from rest_framework import serializers
from room.models import BookingRecordModel

class BookingRecordSerializer(serializers.ModelSerializer):
    
    reference = serializers.SerializerMethodField("get_reference")
    first_name = serializers.SerializerMethodField("get_first_name")
    last_name = serializers.SerializerMethodField("get_last_name")
    room = serializers.SerializerMethodField("get_room")
    booked_by = serializers.SerializerMethodField("get_booked_by")

    class Meta:
        model = BookingRecordModel
        fields = [
            'id', 
            'reference', 
            'first_name',
            'last_name',
            'room',
            'amount', 
            'quantity', 
            'check_in', 
            'check_out',
            'status',
            'payment',
            'booked_by',
            'timestamp'
        ]

    def get_reference(self, obj):
        if obj.reservation:
            return obj.reservation.reference
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

    def get_room(self, obj):
        if obj.room:
            return obj.room.name
        else:
            return None

    def get_booked_by(self, obj):
        if obj.booked_by:
            return "{} {}".format(obj.booked_by.first_name, obj.booked_by.last_name)
        else:
            return None