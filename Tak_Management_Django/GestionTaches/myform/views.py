from django.shortcuts import render 

from .models import ContactForm ,Contact

from .forms import ContactForm2

from django.urls import reverse 
from django.http import HttpResponse 
from django.contrib import messages



# Create your views here.


def contact(request):

    contact_form = ContactForm()
    contact_form2 = ContactForm2() 
    return render(request,'contact.html', {'contact_form' : contact_form, 'contact_form2' : contact_form2})


def contact1(request): 
    # on instancie un formulaire 

    form = ContactForm() 
    # on teste si on est bien en validation de formulaire (POST) 
    if request.method == "POST": 
       # Si oui on récupère les données postées 
       form = ContactForm(request.POST) 
       # on vérifie la validité du formulaire 
       if form.is_valid(): 
          new_contact = form.save() 
         # on prépare un nouveau message 
          messages.success(request,'Nouveau contact '+new_contact.name+' '+new_contact.email) 
          #return redirect(reverse('detail', args=[new_contact.pk] ))

          context = {'pers': new_contact} 

       return render(request,'detail.html', context) 
     
      # Si méthode GET, on présente le formulaire 
    context = {'form': form}
    return render(request,'contact1.html', context)




def detail(request, cid): 
 	contact = Contact.objects.get(pk=cid) 
 	context = {'pers': contact} 
 	return render(request,'detail.html', context)

