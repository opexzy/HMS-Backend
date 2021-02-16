from django.conf.urls import url
from .views.room_management import *

urlpatterns = [
    url(r'^add$',add_room, name="add"),
    url(r'^edit$',update_room, name="edit"),
    url(r'^all$',all_rooms, name="all"),
    url(r'^list$',list_room, {'page':1}, name="list"),
    url(r'^list/(?P<page>[0-9]+)$', list_room,  name="list_page"),
    url(r'^book$',book_room, name="book"),
    url(r'^booking/list$',list_booking, {'page':1}, name="booking_list"),
    url(r'^booking/list/(?P<page>[0-9]+)$', list_booking,  name="booking_list_page"),
]
