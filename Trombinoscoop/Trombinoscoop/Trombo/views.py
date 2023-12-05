from django.shortcuts import render
from django import forms
from django.core.exceptions import ValidationError 

# Create your views here.

from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,  HttpResponse 

from .forms import LoginForm,  StudentProfileForm , EmployeeProfileForm,AddFriendForm
from .models import Personne,Etudiant,Employe,Message 


def welcome(request):
	
  logged_user = get_logged_user_from_request(request) 
  if not logged_user is None : 
    if 'newMessage' in request.GET and request.GET['newMessage'] != '':
		   newMessage = Message(auteur=logged_user, contenu=request.GET['newMessage'], date_de_publication = datetime.date.today()) 
		   newMessage.save() 
    friendMessages = Message.objects.filter(auteur=logged_user).order_by('-date_de_publication') 
    return render(request,'welcome.html',{'logged_user' :logged_user,'friendMessages' :friendMessages})
  else: 
      return HttpResponseRedirect('/login') 




def login(request): 

	if request.method=="POST":
		form = LoginForm(request.POST or None) 
		if form.is_valid():
			user_email = form.cleaned_data['email']
			logged_user = Personne.objects.get(courriel=user_email) 
			request.session['logged_user_id'] = logged_user.id #initialisation de la session

			return HttpResponseRedirect('/welcome') 
	else: 
		form = LoginForm() 
	
	return render(request,'login.html', {'form' : form}) 




def register(request): 
   if len(request.GET) > 0 and 'profileType' in request.GET: 

      studentForm = StudentProfileForm(prefix="st") 
      employeeForm = EmployeeProfileForm(prefix="em") 

      if request.GET['profileType'] == 'student': 
          studentForm = StudentProfileForm(request.GET, prefix="st") 
          if studentForm.is_valid() : 
             studentForm.save(commit=True) 
             return HttpResponseRedirect('/login') 

      elif request.GET['profilelype'] == 'employee' : 
           employeeForm = EmployeeProfileForm(request.GET, prefix="em") 
           if employeeForm.is_valid(): 
              employeeForm.save(commit=True) 
              return HttpResponseRedirect('/login') 

              #Le formulaire envoyé n'est pas valide 
      return render(request,'user_profile.html ' ,{'studentForm' : studentForm, 'employeeForm': employeeForm}) 
   else: 
     
       studentForm = StudentProfileForm(prefix="st") 
       employeeForm = EmployeeProfileForm(prefix="em") 
       return render(request,'user_profile.html ', {'studentForm': studentForm, 'employeeForm' : employeeForm}) 



def get_logged_user_from_request(request): 

     if 'logged_user_id' in request.session: 

        logged_user_id = request.session['logged_user_id'] 
           # On cherche un etudiant 

        if len(Etudiant.objects.filter(id=logged_user_id)) == 1: 
             return Etudiant.objects.get(id=logged_user_id) 
             # On cherche un Employe 

        elif len(Employe.objects.filter(id=logged_user_id)) == 1: 
             return Employe.objects.get(id=logged_user_id) 
             # Si on n'a rien trouve 
        else: 

      	     return None  
     else: 
      	return None      


def add_friend(request) : 

    logged_user = get_logged_user_from_request(request) 
    if logged_user: 
    #Teste si le formulaire a été envoyé 
      if len(request.GET) > 0: 
         form = AddFriendForm(request.GET) 

         if form.is_valid(): 
            new_friend_email = form.cleaned_data['email'] 
            newFriend = Personne.objects.get(courriel=new_friend_email) 
            logged_user.amis.add(newFriend) 
            logged_user.save() 
            return HttpResponseRedirect('/welcome') 

         else: 
          return render(request,'add_friend.html' , {'form' : form}) 
         #Le formulaire n'a pas été envoyé 
      else: 
        form = AddFriendForm() 
        return render(request,'add_friend.html', {'form' : form} ) 
    else: 
      return HttpResponseRedirect('/login')  




def show_profile(request): 

   logged_user = get_logged_user_from_request(request) 
   if logged_user: 
   # Teste si le paramètre attendu est bien passé 
    if 'userToShow' in request.GET and request.GET['userToShow'] != '':
      results = Personne.objects.filter(id=request.GET['userToShow']) 
      if len(results) == 1:

        if Etudiant.objects.filter(id=request.GET['userToShow']): 
           user_to_show = Etudiant.objects.get(id=request.GET['userToShow']) 
        else: 
           user_to_show = Employe.objects.get(id=request.GET['userToShow']) 
        return render(request,'show _profile.html',{'user_to_show' : user_to_show})

      else: 
        return render(request,'show _profile.html', {'user_to_show' : logged_user})
      # Le paramètre n'a pas été trouvé 
    else: 
      return render(request,'show _profile.html',{'user_to_show': logged_user}) 
   else: 
      return HttpResponseRedirect('/login') 



def modify_profile(request) : 

  logged_user = get_logged_user_from_request(request)

  if logged_user: 
    if len(request.GET) > 0: 
      if type(logged_user) == Etudiant:  
       form = StudentProfileForm(request.GET, instance=logged_user) 
      else: 
        form = EmployeeProfileForm(request.GET, instance=logged_user) 
      if form.is_valid(): 
        form.save(commit=True) 
        return HttpResponseRedirect('/welcome') 

      else: 
        return render(request,'modify _profile.html', {'form' : form}) 
    else: 
      if type(logged_user) == Etudiant: 
          form = StudentProfileForm(instance=logged_user) 
      else: 
        form = EmployeeProfileForm(instance=logged_user) 
      return render(request,'modify _profile.html', {'form' : form}) 
  else: 
    return HttpResponseRedirect('/login') 




def ajax_check_email_field(request): 

  HTML_to_return = ' '

  if 'value' in request.GET:

    field = forms .EmailField() 
    try: 
      field.clean(request.GET['value'])
    except ValidationError as ve:
      HTML_to_return = '<ul class="errorlist">'

      for message in ve.messages: 
        HTML_to_return += '<li>' + message + '</li>'

      HTML_to_return += '</ul>' 

  return HttpResponse(HTML_to_return)  






def ajax_add_friend(request):

  HTML_to_return = ' ' 
  logged_user = get_logged_user_from_request(request) 

  if not logged_user is None: 

    if 'email' in request.GET: 
      new_friend_email = request.GET['email'] 
      if len(Personne.objects.filter(courriel=new_friend_email)) == 1:
        new_friend = Personne.objects.get(courriel=new_friend_email) 
        logged_user.amis.add(new_friend) 
        logged_user.save()

      HTML_to_return = '<li><a href="show_profile?userToShow='
      HTML_to_return += str(new_friend.id) 
      HTML_to_return += '">' 
      HTML_to_return += new_friend.prenom + ' ' + new_friend.nom 
      HTML_to_return += '</a></li>' 

      return HttpResponse(HTML_to_return)   