from django.db import models
from datetime import datetime #je add this
from django.utils.html import format_html #je add this

# Create your models here.

class Task(models.Model): 
	name = models.CharField(max_length=250) 
	description = models.TextField() 
	created_date = models.DateField(auto_now_add=True) 
	closed = models.BooleanField(default=False)

	def __str__(self):
		return self.name

    # def colored_due_date(self): 
    #    due_date=django_date(self.due_date,"d F Y") 
    #    # definition de la variable color à faire en fonction de la due_date 
    #    return format_html("<span style=color:%s>%s</span>" %(color_due_date))



    # avec ma methode car pour eux ne marche pas
	def colored_due_date(self): 
	    # created_date=datetime.date(self.created_date,"d M Y")
	    # created_date = int(self.created_date.strftime('%d%m%Y') )
	    jour = int(self.created_date.strftime('%d') )
	    mois = int(self.created_date.strftime('%m') )
	    anne = int(self.created_date.strftime('%Y') )

	    created_date = int(jour)+int(mois)+int(anne)

	    # definition de la variable color à faire en fonction de la due_date 
	    return format_html("<span style=color:{}>{}</span>" ,created_date,created_date)


