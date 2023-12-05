from django.db import models

# Create your models here.

from django.contrib import admin 
from django.db import models

from django.forms import ModelForm ,Textarea


class Contact(models.Model): 
	name = models.CharField(max_length=200) 
	firstname = models.CharField(max_length=200) 
	email = models.EmailField(max_length=200) 
	message = models.CharField(max_length=1000)

	def __str__(self):
		return self.name


class ContactForm(ModelForm): 
	# class Meta: 
	# 	model = Contact 
	# 	fields = ('name', 'firstname', 'email', 'message')	
	class Meta: 
		model = Contact 
		fields =('name','firstname','email','message') 
		widgets = {
             'message': Textarea(attrs={'cols':60,'rows':10}),
        }	



