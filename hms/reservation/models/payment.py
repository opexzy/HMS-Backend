"""
    This model defines Reservation Table
"""
from django.db import models, transaction
from staff.models import StaffModel
from decimal import Decimal
from reservation.models import ReservationModel


STATUS_OPTIONS = ["active","closed"]


#Payment Model Manager
class PaymentModelManager(models.Manager):

    def c_get(self, **Kwargs):
        try:
            account = super().get(**Kwargs)
            return account
        except Exception:
            return None
    
    
#Payment Model
class PaymentModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Reservation Id")
    reservation = models.ForeignKey(ReservationModel, on_delete=models.DO_NOTHING, verbose_name="Reservation")
    posted_by = models.ForeignKey(StaffModel, on_delete=models.DO_NOTHING, null=True, verbose_name="Registered By")
    channel = models.CharField(max_length=25, verbose_name="Payment Channel")
    amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Amount")
    status = models.CharField(max_length=15, verbose_name="Payment Status")
    narration = models.CharField(max_length=255, verbose_name="Narration")
    timestamp = models.DateTimeField(auto_now=True, verbose_name="Timestamp")

    manage = PaymentModelManager()

    class Status:
        COMPLETED = "completed"
        REVERSED = "reversed"
        options = [COMPLETED, REVERSED]

    class Channel:
        DIRECT = "direct"
        POS = "pos"
        CASH = "cash"
        TRANSFER = "transfer"
        options = [DIRECT, POS, CASH, TRANSFER]

    class Meta:
        db_table = "hms_payment"
    
        def __str__(self):
            return self.id
            
    def __str__(self):
            return self.id