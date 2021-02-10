"""
    This model defines Room Table
"""
from django.db import models, transaction
from staff.models import StaffModel
from decimal import Decimal


STATUS_OPTIONS = ["active","closed"]


#Room Model Manager
class RoomModelManager(models.Manager):

    def c_get(self, **Kwargs):
        try:
            account = super().get(**Kwargs)
            return account
        except Exception:
            return None
    
    
#Room Model
class RoomModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Reservation Id")
    name = models.CharField(max_length=255, unique=True, verbose_name="Room")
    description = models.CharField(max_length=255, verbose_name="Description")
    price =  models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Room Price")
    start_no = models.IntegerField(verbose_name="Room Start No")
    end_no = models.IntegerField(verbose_name="Room End No")
    available = models.IntegerField(verbose_name="Available Room")

    manage = RoomModelManager()

    class Status:
        ACTIVE = "active"
        CLOSED = "closed"

    class Meta:
        db_table = "hms_room"
    
        def __str__(self):
            return self.id
            
    def __str__(self):
            return self.id