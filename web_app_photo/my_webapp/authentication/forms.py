from django import forms


# formulaire de connexion

class LoginForm(forms.Form):
	username = forms.CharField(max_length=60,label='Nom d\'utilisateur')
	password = forms.CharField(max_length=60,widget=forms.PasswordInput,label='Mot de passe')



from django.contrib.auth import get_user_model #methode utilitaire qui permet d'obtenier le model User sans l'importer directement


from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = get_user_model()
		fields = ('username','email','first_name','last_name','role')



#formulaire qui interagit avec l'application blog pour changer la photo de profil au nivaeu de "home"

# car au depart le user s'enregistre et se loge sans remplir le champ images  c'est maintenant via ce nouvaeu form que le user va pouvoir update son profile

class UploadProfilePhotoForm(forms.ModelForm):
	class Meta:
	    model = get_user_model()
	    fields = ('profile_photo',)

       

	   

	   
	

