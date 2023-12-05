# -*- coding: utf-8 -*-

""" blog url configuration"""
from django.urls import path
from django.contrib.auth import views as auth_views



from blog import views as blog_views


app_name = 'blog'

urlpatterns = (

    path('home/', blog_views.home, name='home'),
    path('photo/upload/', blog_views.photo_upload, name='photo_upload'),
)

