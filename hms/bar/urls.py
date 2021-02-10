from django.conf.urls import url
from .views.drink_manager import *

urlpatterns = [
    url(r'^drink/all$',get_all_drinks, name="all"),
    url(r'^drink/add$',add_drink, name="add"),
    url(r'^drink/edit$',update_drink, name="edit"),
    url(r'^drink/list$',list_drink, {'page':1}, name="list"),
    url(r'^drink/list/(?P<page>[0-9]+)$', list_drink,  name="list_page"),
    url(r'^drink/order$',order_drink, name="order"),
    url(r'^drink/order/list$',list_order, {'page':1}, name="order_list"),
    url(r'^drink/order/list/(?P<page>[0-9]+)$', order_drink,  name="order_list_page"),
]
