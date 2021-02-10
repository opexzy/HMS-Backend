from django.conf.urls import url

from reservation.views.invoice import get_invoice
from reservation.views.quick_order import quick_order
from .views.reservation_manager import *

urlpatterns = [
    url(r'^invoice/(?P<reference>[a-zA-Z0-9]+)$', get_invoice, name="invoice"),
    url(r'^create$',make_reservation, name="create"),
    url(r'^list$',list_reservation, {'page':1}, name="list"),
    url(r'^list/(?P<page>[0-9]+)$', list_reservation,  name="list_page"),
    url(r'^get/(?P<reference>[a-zA-Z0-9]+)$', get_reservation,  name="get"),
    url(r'^quick-order/(?P<reference>[a-zA-Z0-9]+)$', quick_order,  name="quick_order"),
]
