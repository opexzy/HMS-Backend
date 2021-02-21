from django.conf.urls import url
from .views.coupon_manager import *

urlpatterns = [
    url(r'^add$',add_coupon, name="add"),
    url(r'^list$',list_coupon, {'page':1}, name="list"),
    url(r'^list/(?P<page>[0-9]+)$', list_coupon,  name="list_page"),
    url(r'^delete/(?P<code>[a-zA-Z0-9]+)$', delete_coupon,  name="delete"),
    url(r'^claim$', claim_coupon, name="cliam"),
]
