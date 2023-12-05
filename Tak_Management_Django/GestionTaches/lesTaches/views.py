from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 

def home(request, name): 
	return HttpResponse("Bonjour depuis Django " + name)



from lesTaches.models import Task # import de la class Task 
from django.shortcuts import render # import de la methode render

# def task_listing(request): 
# 	from django.template import Template,Context 
# 	objets=Task.objects.all().order_by('created_date') 
# 	template=Template('{% for elem in objets %} {{elem}} <br />{%endfor%}') 
# 	print(str(template)) 
# 	context=Context({'objets':objets}) 
# 	print(str(template.render(context))) 
# 	return HttpResponse(template.render(context))


def task_listing(request): 
	tasks = Task.objects.all().order_by('created_date') 
	return render(request,template_name='list.html',context={'tasches':tasks})



def task_listing2(request): 
	objects = Task.objects.all().order_by('created_date') 
	return render(request, template_name='list2.html', context={'objects': objects} )


