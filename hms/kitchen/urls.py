from django.conf.urls import url

from bar.views.drink_manager import get_all_drinks
from .views.food_manager import *

urlpatterns = [
    url(r'^food/all$',get_all_foods, name="all"),
    url(r'^food/add$',add_food, name="add"),
    url(r'^food/edit$',update_food, name="edit"),
    url(r'^food/list$',list_food, {'page':1}, name="list"),
    url(r'^food/list/(?P<page>[0-9]+)$', list_food,  name="list_page"),
    url(r'^food/order$',order_food, name="order"),
    url(r'^food/order/list$',list_order, {'page':1}, name="order_list"),
    url(r'^food/order/list/(?P<page>[0-9]+)$', order_food,  name="order_list_page"),
]
