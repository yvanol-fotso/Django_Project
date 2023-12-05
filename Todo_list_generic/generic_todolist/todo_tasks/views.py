from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic import ListView, CreateView,UpdateView,DeleteView

from .models import TodoItem

from .forms import TodoItemCreateForm,TodoItemUpdateForm



#list Todo 

class TodoItemListView(ListView):
	model = TodoItem
	template_name ='todo_tasks/todo_itemlist.html'



#create Todo

class TodoItemCreateView(CreateView):
	model = TodoItem #model a use pour save
	template_name = 'todo_tasks/todo_itemcreate.html'
	form_class = TodoItemCreateForm #formulaire qui servira a creer
	success_url = '/todo/list/' #url de redirection lorsque la todo a ete crerr avec success



#Udpate todo

class  TodoItemUpdateView(UpdateView):
	model = TodoItem #model a use pour save
	template_name = 'todo_tasks/todo_itemupdate.html'
	form_class = TodoItemUpdateForm #formulaire qui servira a creer
	success_url = '/todo/list/' #url de redirection lorsque la todo a ete crerr avec success


#delete todo

class TodoItemDeleteView(DeleteView):
	model = TodoItem
	template_name ='todo_tasks/todo_itemdelete.html'
	success_url = '/todo/list'




