"""upload_image URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path ,include

from django.conf import settings #new
from django.conf.urls.static import static



urlpatterns = [
    path('',include('image_app.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


''' Username: admin
Email address: santibaniez
Error: Enter a valid email address.
Email address: admin@gmail.com
Password:santibaniez
Password (again):santibaniez
Superuser created successfully.
'''