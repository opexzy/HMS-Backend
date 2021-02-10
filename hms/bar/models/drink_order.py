"""
    This model defines Drink Table
"""
from django.db import models
from .drink import DrinkModel
from reservation.models import ReservationModel
from decimal import Decimal
from staff.models import StaffModel


STATUS_OPTIONS = ["active","closed"]


#Drink Order Model Manager
class DrinkOrderModelManager(models.Manager):

    def c_get(self, **Kwargs):
        try:
            account = super().get(**Kwargs)
            return account
        except Exception:
            return None
    
    
# Food Order Model
class DrinkOrderModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Reservation Id")
    reservation = models.ForeignKey(ReservationModel, on_delete=models.DO_NOTHING, verbose_name="Reservation")
    drink = models.ForeignKey(DrinkModel, on_delete=models.DO_NOTHING, verbose_name="Drink")
    amount =  models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Amount")
    quantity = models.IntegerField(verbose_name="Quantity")
    registered_by = models.ForeignKey(StaffModel, on_delete=models.DO_NOTHING, verbose_name="Registered By")
    status = models.CharField(max_length=15, verbose_name="Status")
    timestamp = models.DateTimeField(auto_now=True, verbose_name='Timestamp')

    manage = DrinkOrderModelManager()

    class Status:
        PENDING = "pending"
        COMPLETED = "completed"
        CANCELED = "canceled"
        options = [PENDING, COMPLETED, CANCELED]


    class Meta:
        db_table = "hms_drink_order"
    
        def __str__(self):
            return self.id
            
    def __str__(self):
            return self.id