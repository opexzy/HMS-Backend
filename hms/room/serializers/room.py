"""
    Room Model Serializer
"""

from rest_framework import serializers
from room.models import RoomModel

class RoomSerializer(serializers.ModelSerializer):
    
    status = serializers.SerializerMethodField("get_status")

    class Meta:
        model = RoomModel
        fields = [
            'id', 
            'name', 
            'description', 
            'price',
            'status', 
            'start_no', 
            'end_no', 
            'available'
        ]

    def get_status(self, obj):
        if obj and obj.available < 1:
            return 'available'
        else:
            return 'unavailable'