"""
    This model defines batch order Tables
"""
from django.db import models, transaction
from staff.models import StaffModel
from decimal import Decimal
from reservation.models import ReservationModel
from utils.randstr import get_token

ORDER_START = 1024   
  
#Order Model
class OrderModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Order Id")
    order_ref = models.CharField(max_length=8, unique=True, verbose_name="Order Reference")
    amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Amount")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Timestamp")
    client = models.CharField(max_length=25, null=True, verbose_name="Client")

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    def save(self):
        if not self.order_ref:
            count = OrderModel.objects.count()
            prefix = get_token(2).upper()
            self.order_ref = prefix + str(ORDER_START + count)
        return super().save()

    class Meta:
        db_table = "hms_order"
        def __str__(self):
            return self.id
            
    def __str__(self):
            return self.id