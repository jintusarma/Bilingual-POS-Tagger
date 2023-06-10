from django.urls import path,include
from .views import *
urlpatterns = [
    path('',add_tagset,name='add_tagset')
]