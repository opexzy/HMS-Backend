"""
    Drink Model Serializer
"""

from rest_framework import serializers
from bar.models import DrinkModel

class DrinkSerializer(serializers.ModelSerializer):
    
    status = serializers.SerializerMethodField("get_status")

    class Meta:
        model = DrinkModel
        fields = [
            'id', 
            'name', 
            'description', 
            'price',
            'status', 
            'metric', 
            'available',
            'group'
        ]

    def get_status(self, obj):
        if obj and int(obj.available) < 1:
            return 'available'
        else:
            return 'unavailable'