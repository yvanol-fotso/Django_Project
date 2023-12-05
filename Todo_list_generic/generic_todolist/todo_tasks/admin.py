from django.contrib import admin

# Register your models here.
from .models import TodoItem

#visibilite

admin.site.register(TodoItem)
