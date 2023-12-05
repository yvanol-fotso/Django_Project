from django.contrib import admin
from django.urls import path 

from .views import*

urlpatterns = [
    path('' ,hotel_image_view,name='hotel_image_view'),
    path('success/',success,name='success'),
    path('hotel_images/',display_hotel_images,name='display_hotel_images'),

]