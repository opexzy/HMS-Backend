from django.conf.urls import url
from .views.reservation_manager import *

urlpatterns = [
    url(r'^create$',make_reservation, name="create"),
    url(r'^list$',list_reservation, {'page':1}, name="list"),
    url(r'^list/(?P<page>[0-9]+)$', list_reservation,  name="list_page"),
]
