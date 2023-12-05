from django.shortcuts import render,redirect

# Create your views here.

from django.contrib.auth import login, authenticate,logout

from .forms import LoginForm,SignupForm,UploadProfilePhotoForm

from blog.views import home


def login_page(request):

  form = LoginForm()
  message = ""

  if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
            # raw_password = form.cleaned_data.get('password')
         username = form.cleaned_data['username']
         raw_password = form.cleaned_data['password']
         user = authenticate(request, username=username, password=raw_password)
         if user is not None:
         	login(request,user)
         	message= f'Bonjour ,{user.username}! vous etes bien connecter.'
         	return redirect('blog:home')
		    
         else:
         	 message = 'Identifiant incorrect'


  return render(request,'authentication/login.html',context={'form':form,'message':message})		



def logout_user(request):
	logout(request)
	return redirect('authentication:login')



# avec les vues generic ie les vues basees sur les classes ayant des methodes pour traiter les deux type de requets get et post

from django.views.generic import View

class loginPageView(View):

	template_name = 'authentication/login.html'
	form_class = LoginForm

	def get(self,request):

		form = self.form_class()
		message= ''
		return render(request,self.template_name,context={'form':form,'message':message})


def post(self,request):

    form = self.form_class(request.POST)
    if form.is_valid():
        #on peut dabor recuper et stocker dans les variables coe plus haut
    	user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
    	if user is not None:

         	 login(request,user)
         	 message= f'Bonjour ,{user.username}! vous etes bien connecter.'
         	 return redirect('blog:home')

        # else:    	 
    message = 'Identifiant incorrect'


    return render(request,'authentication/login.html',context={'form':form,'message':message})		




from django.conf import settings

#notons que en utilisant les validateur par defaut de django les champ password doivent etre long et complexe sinon genere l'erreur "ce password est trop courant"

def signup_page(request):

	form = SignupForm()
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			#auto-login user
			login(request,user)
			return redirect(settings.LOGIN_REDIRECT_URL)

	return render(request,'authentication/signup.html',context={'form':form})	




def upload_profile_photo(request):

    form = UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
      form = UploadProfilePhotoForm(request.POST,request.FILES,instance=request.user)
      if form.is_valid():
        user = form.save()
         #auto-login user
        login(request,user)
        return redirect(settings.LOGIN_REDIRECT_URL) #equivalent a "return redirect('blog:home')" car la variable LOGIN_REDIRECT_URL definir dans le fichier setting
        #dis que si tout se passe bien lors du login alor redirige le user vers la page profile

    return render(request,'authentication/upload_profile_photo.html',context={'form':form}) 





