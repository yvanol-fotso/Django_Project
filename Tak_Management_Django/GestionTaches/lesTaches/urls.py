from django.urls import path 
from . import views 

urlpatterns=[ 
    # path('home',views.home,name='home'),
    path('home/<name>',views.home,name='home'),
    path('listing', views.task_listing,name="listing"),
    path('listing2', views.task_listing2,name="listing2"),
]


''' 
Nom d’utilisateur: admin
Adresse électronique: admin@demo.com
Password:santibaniez
Password (again):santibaniez
Superuser created successfully.
'''
