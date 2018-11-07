from django.urls import path
from django.urls import include
from django.conf.urls import url

from .views import *

app_name = 'people'

urlpatterns = [
    url(r'^$', people_start,name = 'people_start'),
    url(r'(?P<i>\d+)/(?P<city>\d+)$', people_list,name = 'people_list')
]