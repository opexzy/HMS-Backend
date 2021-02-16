"""
    Drink Order Model Serializer
"""

from rest_framework import serializers
from bar.models import DrinkOrderModel

class DrinkOrderSerializer(serializers.ModelSerializer):
    
    reference = serializers.SerializerMethodField("get_reference")
    first_name = serializers.SerializerMethodField("get_first_name")
    last_name = serializers.SerializerMethodField("get_last_name")
    drink = serializers.SerializerMethodField("get_drink")
    placed_by = serializers.SerializerMethodField("get_placed_by")
    finalized_by = serializers.SerializerMethodField("get_finalized_by")

    class Meta:
        model = DrinkOrderModel
        fields = [
            'id', 
            'reference', 
            'first_name',
            'last_name',
            'drink',
            'amount', 
            'quantity', 
            'placed_by',
            'finalized_by',
            'payment',
            'status',
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

    def get_drink(self, obj):
        if obj.drink:
            return obj.drink.name
        else:
            return None

    def get_placed_by(self, obj):
        if obj.registered_by:
            return "{} {}".format(obj.registered_by.first_name, obj.registered_by.last_name)
        else:
            return None

    def get_finalized_by(self, obj):
        if obj.completed_by:
            return "{} {}".format(obj.completed_by.first_name, obj.completed_by.last_name)
        else:
            return None