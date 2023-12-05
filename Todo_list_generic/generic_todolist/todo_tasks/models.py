from django.db import models

# Create your models here.

from django.utils import timezone


class TodoItem(models.Model):
	DEFAULT = 'DEFAULT'
	PERSONAL = 'PERSONAL'
	SHOPING = 'SHOPING'
	WISHLIST = 'WISHLIST'
	WORK = 'WORK'

	CATEGORIES = (
        (DEFAULT,DEFAULT),
        (PERSONAL,PERSONAL),
        (SHOPING,SHOPING),
        (WISHLIST,WISHLIST),
        (WORK,WORK)

		)


	title = models.CharField(max_length=100,blank=True,null=True)
	body = models.TextField(null=True,blank=True)
	due_date = models.DateField(default=timezone.now)
	task_finished = models.BooleanField(default=True)
	category = models.CharField(max_length=20,choices=CATEGORIES,default=DEFAULT)


	def __str__(self):
		return f'{self.title}'