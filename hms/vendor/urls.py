from django.conf.urls import url
from .views.vendor_manager import *

urlpatterns = [
    url(r'^add$',add_vendor, name="add"),
    url(r'^all$',all_vendors, name="all"),
    url(r'^supply/add$',add_supply, name="add_supply"),
     url(r'^supply/delete/(?P<id>[0-9]+)$',delete_supply, name="delete_supply"),
    url(r'^payment/add$',add_payment, name="add_payment"),
    url(r'^supply/list$',list_supply, {'page':1}, name="list_supply"),
    url(r'^supply/list/(?P<page>[0-9]+)$', list_supply,  name="list_supply_page"),
    url(r'^payment/list$',list_payment, {'page':1}, name="list_payment"),
    url(r'^payment/list/(?P<page>[0-9]+)$', list_payment,  name="list_payment_page"),
]
