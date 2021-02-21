from django.conf.urls import url
from .views.option_manager import *

urlpatterns = [
    url(r'^(?P<name>[a-zA-Z0-9]+)/group$',get_groups, name="all"),
    url(r'^(?P<name>[a-zA-Z0-9]+)/add$',add_group, name="add"),
]
