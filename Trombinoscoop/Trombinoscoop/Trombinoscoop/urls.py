
from django.contrib import admin
from django.conf import settings
from django.urls import path, include



urlpatterns = (
	path('admin/', admin.site.urls),
    path('', include('Trombo.urls', namespace='trombo')),
   
    
)