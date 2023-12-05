from django.db import models

# Create your models here.

from django.conf import settings


class Photo(models.Model):

	image = models.ImageField()
	caption = models.CharField(max_length=130,blank=True)
	uploader = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add = True)



class Blog(models.Model):
	photo = models.ForeignKey(Photo,null=True,on_delete=models.SET_NULL,blank=True)
	title = models.CharField(max_length=130)
	content = models.CharField(max_length=5000)
	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	started = models.BooleanField(default=False)

