from django.conf.urls import url
from .admin.views.authenticate import login, validate_token, update_password


urlpatterns = [
    url(r'^login$',login, name="login"),
    url(r'^validate$',validate_token, name="validate"),
    url(r'^pwd-change$',update_password, name="update_password"),
]