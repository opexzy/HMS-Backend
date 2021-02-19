"""
    This model defines Reservation Table
"""
from django.db import models, transaction
from staff.models import StaffModel
from decimal import Decimal
from utils.randstr import get_token


STATUS_OPTIONS = ["active","closed"]


#Reservation Record Model Manager
class ReservationModelManager(models.Manager):

    def c_get(self, **Kwargs):
        try:
            account = super().get(**Kwargs)
            return account
        except Exception:
            return None
    
    
#Reservation Record Model
class ReservationModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Reservation Id")
    reference = models.CharField(max_length=12, unique=True, verbose_name="Reference")
    reservation_type = models.CharField(max_length=50, verbose_name="Reservation Type")
    first_name = models.CharField(max_length=255, null=True, verbose_name="First Name")
    last_name = models.CharField(max_length=255, null=True, verbose_name="Last Name")
    corporate_name = models.CharField(max_length=255, null=True, verbose_name="Corporate")
    gender = models.CharField(max_length=15, null=True, verbose_name="Gender")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    created_by = models.ForeignKey(StaffModel, on_delete=models.DO_NOTHING, verbose_name="Created By", related_name="reservation_created_by", null=True)
    status = models.CharField(max_length=15, verbose_name="Reservation Status")
    credit_balance =  models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Credit Balance")
    amount_spent =  models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name="Amount Spent")
    amount_unpaid =  models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name="Amount Unpaid")
    timestamp = models.DateTimeField(auto_now=True, verbose_name="Timestamp")

    manage = ReservationModelManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    def save(self):
        if not self.reference:
            self.reference = self.generate_ref()
        return super().save()

    class Status:
        ACTIVE = "active"
        CLOSED = "closed"
        CANCELED = "canceled"

        options = [ACTIVE, CLOSED]
    
    def generate_ref(self):
        len = 12
        return  get_token(len).upper()


    class Meta:
        db_table = "hms_reservation"
    
        def __str__(self):
            return self.id
            
    def __str__(self):
            return self.id