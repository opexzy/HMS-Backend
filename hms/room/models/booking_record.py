"""
    This model defines Room Table
"""
from django.db import models
from .room import RoomModel
from reservation.models import ReservationModel
from decimal import Decimal
from utils.randstr import get_token


STATUS_OPTIONS = ["active","closed"]


#Booking Record Model Manager
class BookingRecordModelManager(models.Manager):

    def c_get(self, **Kwargs):
        try:
            account = super().get(**Kwargs)
            return account
        except Exception:
            return None
    
    
#Booking Record Model
class BookingRecordModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Reservation Id")
    reservation = models.ForeignKey(ReservationModel, on_delete=models.DO_NOTHING, verbose_name="Reservation")
    room = models.ForeignKey(RoomModel, on_delete=models.DO_NOTHING, verbose_name="Room")
    amount =  models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Amount")
    quantity = models.IntegerField(verbose_name="Quantity")
    check_in = models.DateField(verbose_name="Checkin Date")
    check_out = models.DateField(verbose_name="Checkout Date")
    status = models.CharField(max_length=15, verbose_name="Status")
    timestamp = models.DateTimeField(auto_now=True, verbose_name='Timestamp')

    manage = BookingRecordModelManager()

    class Status:
        ACTIVE = "active"
        CLOSED = "closed"
        OVERDUE = "overdue"
        options = [ACTIVE, CLOSED, OVERDUE]
    
    def generate_ref(self):
        len = 12
        return  get_token(len).upper()


    class Meta:
        db_table = "hms_booking_record"
    
        def __str__(self):
            return self.id
            
    def __str__(self):
            return self.id