from django.db import models

# Create your models here.



from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):

	CREATOR = 'CREATOR'
	SUBSCRIBER = 'SUBSCRIBER'


	ROLE_CHOICES = (

		(CREATOR,'CREATOR'),
		(SUBSCRIBER,'SUBSCRIBER'),
	)

	profile_photo = models.ImageField(verbose_name='photo de profile')
	role = models.CharField(max_length=30,choices=ROLE_CHOICES,verbose_name='Role')
