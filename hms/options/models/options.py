"""
    This model defines Option Table
"""
from django.db import models, transaction
from decimal import Decimal
import json


STATUS_OPTIONS = ["active","closed"]


#Option Model Manager
class OptionModelManager(models.Manager):

    def c_get(self, name):
        options = super().filter(name=name)
        temp = []
        for option in options:
            temp.append(option.value)
        return temp

#Food Model
class OptionModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="Option Id")
    name = models.CharField(max_length=255, verbose_name="Option Name")
    value =  models.TextField(verbose_name="Option Value")

    manage = OptionModelManager()

    class Status:
        ACTIVE = "active"
        CLOSED = "closed"

    class Meta:
        db_table = "hms_options"
    
        def __str__(self):
            return self.id