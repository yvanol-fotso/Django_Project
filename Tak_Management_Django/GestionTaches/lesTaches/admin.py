from django.contrib import admin

# Register your models here.

from lesTaches.models import Task 

class TaskAdmin(admin.ModelAdmin): 
	class TaskAdmin(admin.ModelAdmin): 
		list_display=('name','description','closed') 
		read_only=('created_date')

		
admin.site.register(Task,TaskAdmin)


# admin.site.register(Task)

