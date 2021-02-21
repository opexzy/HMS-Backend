"""
    This model defines Vendor Table
"""
from django.db import models, transaction
from staff.models import StaffModel
from decimal import Decimal


STATUS_OPTIONS = ["active","closed"]


#Room Model Manager
class VendorModelManager(models.Manager):

    def c_get(self, **Kwargs):
        try:
            account = super().get(**Kwargs)
            return account
        except Exception:
            return None
    
    
#Food Model
class VendorModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Food Id")
    name = models.CharField(max_length=255, unique=True, verbose_name="Vendor Name")
    address = models.CharField(max_length=255, verbose_name="Address")

    manage = VendorModelManager()

    class Status:
        ACTIVE = "active"
        CLOSED = "closed"

    class Meta:
        db_table = "hms_vendor"
    
        def __str__(self):
            return self.id
            
    def __str__(self):
            return self.id