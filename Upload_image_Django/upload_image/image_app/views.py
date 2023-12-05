from django.shortcuts import render , redirect #new 'redirect'

# Create your views here.
from django.http import HttpResponse
from .forms import*

def hotel_image_view (request):

    if request.method == 'POST':
     form =HotelForm(request.POST,request.FILES)

     if form.is_valid():

        form.save()
     return redirect('success')

    else:
        form =HotelForm()
    return render(request,'index.html',{'form':form})



def success(request):
       		return HttpResponse( '<h1 style="margin-top: 5%;in-bottom:; margin-left:35%"> Upload and image by Fotso &copy; 2021</h1> <br>'
       			'<p style="display: inline-block; margin-left:35%;margin-top: 6%; text-align: center;align-items: center;border: solid;width:30%;padding: 2%;background-color: violet;color: white;"><a href="/hotel_images" style="text-decoration:none;">Upload Succesful Click here to see All Hotel Image</a></p>')   



def display_hotel_images(request):

 	if request.method == 'GET':
 	#gettings all the objects of hotel.

 	   hotel = Hotel.objects.all()

 	   return render(request,'display_hotel_images.html',{'hotel_images':hotel})
