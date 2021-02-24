"""
    This model defines supply history Table
"""
from django.db import models, transaction
from staff.models import StaffModel
from decimal import Decimal
from vendor.models import vendor

from vendor.models.vendor import VendorModel


STATUS_OPTIONS = ["active","closed"]


#Room Model Manager
class SupplyModelManager(models.Manager):

    def c_get(self, **Kwargs):
        try:
            account = super().get(**Kwargs)
            return account
        except Exception:
            return None
    
    
#Food Model
class SupplyModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Food Id")
    vendor = models.ForeignKey(VendorModel, on_delete=models.DO_NOTHING, verbose_name="Reservation")
    description = models.CharField(max_length=500, verbose_name="Description")
    status = models.CharField(max_length=20, verbose_name="Status")
    amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Amount")
    amount_unpaid = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Amount")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')

    manage = SupplyModelManager()

    class Status:
        PAID = "paid"
        UNPAID = "unpaid"

        options = [PAID, UNPAID]

    class Meta:
        db_table = "hms_supply"
    
        def __str__(self):
            return self.id
            
    def __str__(self):
            return self.id