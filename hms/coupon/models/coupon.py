"""
    This model defines Food Table
"""
from django.db import models, transaction
from decimal import Decimal
from utils.randstr import get_token
from reservation.models import ReservationModel


#Coupon Model Manager
class CouponModelManager(models.Manager):

    def c_get(self, **Kwargs):
        try:
            account = super().get(**Kwargs)
            return account
        except Exception:
            return None
    
    
#Coupon Model
class CouponModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Coupon Id")
    code = models.CharField(max_length=14, unique=True, verbose_name="Coupon Code")
    status = models.CharField(max_length=15,  default="active", verbose_name="Status")
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Coupon Discount")
    reservation = models.ForeignKey(ReservationModel, null=True, on_delete=models.DO_NOTHING, verbose_name="Reservation")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_used = models.DateTimeField(verbose_name='Date Used', null=True)

    manage = CouponModelManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    def save(self):
        if not self.code:
            self.code = self.generate_ref()
        return super().save()

    class Status:
        ACTIVE = "active"
        USED = "used"
        options = [ACTIVE, USED]

    def generate_ref(self):
        len = 14
        return  get_token(len).upper()


    class Meta:
        db_table = "hms_coupon"
    
        def __str__(self):
            return self.id
            
    def __str__(self):
            return self.id