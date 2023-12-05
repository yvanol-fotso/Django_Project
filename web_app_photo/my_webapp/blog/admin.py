from django.contrib import admin

# Register your models here.

# je rend mes models visible dans l'administration

from .models import Blog,Photo

admin.register(Blog)
admin.register(Photo)

