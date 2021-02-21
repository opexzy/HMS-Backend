"""
    This model defines Food Table
"""
from django.db import models, transaction
from decimal import Decimal

from options.models.options import OptionModel


STATUS_OPTIONS = ["active","closed"]


#Room Model Manager
class DrinkModelManager(models.Manager):

    def c_get(self, **Kwargs):
        try:
            account = super().get(**Kwargs)
            return account
        except Exception:
            return None
    
    
#Food Model
class DrinkModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Drink Id")
    name = models.CharField(max_length=255, unique=True, verbose_name="Food Name")
    description = models.CharField(max_length=255, verbose_name="Description")
    price =  models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Drink Price")
    metric = models.CharField(max_length=255, verbose_name="Metric")
    available = models.IntegerField(verbose_name="Available Drink")
    group = models.ForeignKey(OptionModel, null=True, default=None, on_delete=models.DO_NOTHING, verbose_name="Drink Group")

    manage = DrinkModelManager()

    class Status:
        ACTIVE = "active"
        CLOSED = "closed"

    class Meta:
        db_table = "hms_drink"
    
        def __str__(self):
            return self.id
            
    def __str__(self):
            return self.id