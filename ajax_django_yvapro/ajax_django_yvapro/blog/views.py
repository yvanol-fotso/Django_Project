from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt #pour la verification du jeton csrf

def home(request):
	return render(request,"index.html") #plus besoin de preciser le chemin vers le template cars par defaut django fouille dans chaque app un dossier template et charge le template


@csrf_exempt
def compute(request):
	a = request.POST.get("a")
	b = request.POST.get("b")

	result =int(a) + int(b)

	return JsonResponse({"operation_result":result})


