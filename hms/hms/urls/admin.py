"""bipnet URL Configuration - ADMIN URL

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

urlpatterns = [
    path('auth/',include(('hms_auth.urls','auth'), namespace='auth')),
    path('staff/',include(('staff.urls','staff'), namespace='staff')),
    path('reservation/',include(('reservation.urls','reservation'), namespace='reservation')),
    path('room/',include(('room.urls','room'), namespace='room')),
    path('kitchen/',include(('kitchen.urls','kitchen'), namespace='kitchen')),
    path('bar/',include(('bar.urls','bar'), namespace='bar')),
    path('coupon/',include(('coupon.urls','bar'), namespace='coupon')),
    path('option/',include(('options.urls','option'), namespace='option')),
    path('vendor/',include(('vendor.urls','vendor'), namespace='vendor')),
    path('report/',include(('report.urls','report'), namespace='report')),
]
