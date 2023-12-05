from django.urls import path 
from . import views 

urlpatterns=[ 

    path('',views.contact,name='contact'),
    path('contact1',views.contact1,name='contact1'), 
    path('detail/<int:cid>',views.detail,name='detail'),

]


''' 
Nom d’utilisateur: admin
Adresse électronique: admin@demo.com
Password:santibaniez
Password (again):santibaniez
Superuser created successfully.
'''

