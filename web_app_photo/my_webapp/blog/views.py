from django.shortcuts import render,redirect

# Create your views here.

from django.contrib.auth.decorators import login_required #pour restreindre l'acces a la home page

from .forms import PhotoForm
from .models import Photo

@login_required
def home(request):
	photos = Photo.objects.all()

	return render(request,'blog/home.html',context={'photos':photos})


@login_required
def photo_upload(request):

	form = PhotoForm()
	if request.method == 'POST':
		form = PhotoForm(request.POST,request.FILES)
		if form.is_valid():

			photo = form.save(commit=False) #j'enregistre mais je ne save pas en bd
			#set the uploader to the user before the user before saving the model
			photo.uploader = request.user

			#now we can save the photo
			photo.save()
			return redirect('blog:home')

	return render(request,'blog/photo_upload.html',context={'form':form})



