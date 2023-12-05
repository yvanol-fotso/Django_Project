
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .views import welcome,login,register, add_friend ,show_profile,modify_profile,ajax_check_email_field,ajax_add_friend  

app_name = 'trombo'

urlpatterns = (
    path('welcome',welcome, name='welcome'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('add_friend', add_friend, name='add_friend'),
    path('show_profile', show_profile, name='show_profile'),   
    path('modify_profile',modify_profile, name='modify_profile'),   
    path('ajax-checkEmailField',ajax_check_email_field, name='ajax_check_email_field'),  #validation de la creation d'un compte via ajax 
    path('ajax-addFriend', ajax_add_friend, name='ajax_add_friend')
)

'''configuration interface d'administration
username:admin
password:santibaniez
email:admin@demo.com
'''



