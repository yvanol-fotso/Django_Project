from django.contrib import admin
from .models import Faculte, Personne, Message,Fonction,Cursus,Campus,Employe,Etudiant

# Register your models here.
admin.site.register(Faculte)
admin.site.register(Personne)
admin.site.register(Message)
admin.site.register(Campus)
admin.site.register(Fonction)
admin.site.register(Cursus)
admin.site.register(Employe)
admin.site.register(Etudiant)


