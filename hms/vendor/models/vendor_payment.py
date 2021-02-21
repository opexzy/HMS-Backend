"""
    This model defines Reservation Table
"""
from django.db import models, transaction
from staff.models import StaffModel
from decimal import Decimal
from vendor.models import SupplyModel


STATUS_OPTIONS = ["active","closed"]


#Payment Model Manager
class VendorPaymentModelManager(models.Manager):

    def c_get(self, **Kwargs):
        try:
            account = super().get(**Kwargs)
            return account
        except Exception:
            return None
    
    
#Payment Model
class VendorPaymentModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Reservation Id")
    supply = models.ForeignKey(SupplyModel, on_delete=models.DO_NOTHING, verbose_name="Reservation")
    posted_by = models.ForeignKey(StaffModel, on_delete=models.DO_NOTHING, null=True, verbose_name="Registered By")
    amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Amount")
    status = models.CharField(max_length=15, verbose_name="Payment Status")
    timestamp = models.DateTimeField(auto_now=True, verbose_name="Timestamp")

    manage = VendorPaymentModelManager()

    class Status:
        COMPLETED = "completed"
        REVERSED = "reversed"
        options = [COMPLETED, REVERSED] 

    class Meta:
        db_table = "hms_vendor_payment"
    
        def __str__(self):
            return self.id
            
    def __str__(self):
            return self.id