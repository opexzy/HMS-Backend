"""
    This model defines Room Table
"""
from django.db import models
from .room import RoomModel
from reservation.models import ReservationModel
from decimal import Decimal
from staff.models import StaffModel
from reservation.models import PaymentModel


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
    booked_by = models.ForeignKey(StaffModel, on_delete=models.DO_NOTHING, verbose_name="Booked By", null=True)
    payment = models.ForeignKey(PaymentModel, null=True, on_delete=models.DO_NOTHING, verbose_name="Payment Id")
    timestamp = models.DateTimeField(auto_now=True, verbose_name='Timestamp')

    manage = BookingRecordModelManager()

    class Status:
        ACTIVE = "active"
        CHECKED_IN = "checked_in"
        CHECKED_OUT = "checked_out"
        CANCELED = "canceled"

        options = [ACTIVE, CHECKED_IN, CHECKED_OUT, CANCELED]



    class Meta:
        db_table = "hms_booking_record"
    
        def __str__(self):
            return self.id
            
    def __str__(self):
            return self.id