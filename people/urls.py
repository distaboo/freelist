from django.urls import path
from django.urls import include
from .views import *


urlpatterns = [
    path('', people_list)
]