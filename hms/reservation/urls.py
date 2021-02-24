from django.conf.urls import url

from reservation.views.invoice import get_invoice, get_payment_report, list_payment, make_payment
from reservation.views.quick_order import get_my_orders, quick_order
from .views.reservation_manager import *

urlpatterns = [
    url(r'^create$',make_reservation, name="create"),
    url(r'^active$',list_active_reservation, name="list"),
    url(r'^list$',list_reservation, {'page':1}, name="list"),
    url(r'^list/(?P<page>[0-9]+)$', list_reservation,  name="list_page"),
    url(r'^get/(?P<reference>[a-zA-Z0-9]+)$', get_reservation,  name="get"),
    url(r'^cancel/(?P<reference>[a-zA-Z0-9]+)$', cancel_reservation,  name="cancel"),
    url(r'^override/(?P<reference>[a-zA-Z0-9]+)$', override_reservation,  name="override"),
    url(r'^close/(?P<reference>[a-zA-Z0-9]+)$', close_reservation,  name="close"),
    url(r'^quick-order/(?P<reference>[a-zA-Z0-9]+)$', quick_order,  name="quick_order"),
    url(r'^invoice/(?P<reference>[a-zA-Z0-9]+)$', get_invoice, name="invoice"),
    url(r'^make-payment$', make_payment, name="make_payment"),
    url(r'^payment/list$',list_payment, {'page':1}, name="list"),
    url(r'^payment/list/(?P<page>[0-9]+)$', list_payment,  name="list_page"),
    url(r'^payment/report$', get_payment_report,  name="payment_report"),
    url(r'^my-order-report$', get_my_orders,  name="my_order_report"),
]
