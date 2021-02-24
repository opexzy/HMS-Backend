from django.conf.urls import url
from .dashboard import dashboard

urlpatterns = [
    url(r'^dashboard$',dashboard, name="dashboard"),
]
