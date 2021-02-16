"""
    This model defines Room Table
"""
from django.db import models
from .food import FoodModel
from reservation.models import ReservationModel
from decimal import Decimal
from staff.models import StaffModel
from reservation.models import PaymentModel

STATUS_OPTIONS = ["active","closed"]


#Food Order Model Manager
class FoodOrderModelManager(models.Manager):

    def c_get(self, **Kwargs):
        try:
            account = super().get(**Kwargs)
            return account
        except Exception:
            return None
    
    
# Food Order Model
class FoodOrderModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Reservation Id")
    reservation = models.ForeignKey(ReservationModel, on_delete=models.DO_NOTHING, verbose_name="Reservation")
    food = models.ForeignKey(FoodModel, on_delete=models.DO_NOTHING, verbose_name="Food")
    amount =  models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Amount")
    quantity = models.IntegerField(verbose_name="Quantity")
    registered_by = models.ForeignKey(StaffModel, on_delete=models.DO_NOTHING, null=True, verbose_name="Registered By")
    completed_by = models.ForeignKey(StaffModel, on_delete=models.DO_NOTHING, null=True, related_name="food_order_completed_by", verbose_name="Commpleted By")
    status = models.CharField(max_length=15, verbose_name="Status")
    payment = models.ForeignKey(PaymentModel, null=True, on_delete=models.DO_NOTHING, verbose_name="Payment Id")
    timestamp = models.DateTimeField(auto_now=True, verbose_name='Timestamp')

    manage = FoodOrderModelManager()

    class Status:
        PENDING = "pending"
        COMPLETED = "completed"
        CANCELED = "canceled"
        options = [PENDING, COMPLETED, CANCELED]


    class Meta:
        db_table = "hms_food_order"
    
        def __str__(self):
            return self.id
            
    def __str__(self):
            return self.id