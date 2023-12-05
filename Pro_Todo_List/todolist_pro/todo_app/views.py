from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView,CreateView,UpdateView,DeleteView

from .models import ToDoList,ToDoItem

from django.urls import reverse, reverse_lazy

class TodoListView(ListView):
   model = ToDoList #model a utiliser

   template_name = "todo_app/index.html"





class ItemListView(ListView):
   model = ToDoItem
   template_name = "todo_app/todo_list.html"

   def get_queryset(self):
     return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

   def get_context_data(self):
       context = super().get_context_data()
       context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
       return context


#puisque dans la classe ListCreate(CreateView): je n'ai pas preciser le template name alors quesceque django fait il utilise 
#le nom de model aue j'ai specifier pour cette classe il ajoute un unserscore et concatene a form.html 
#et te dmande de creer une vue ayant ce nom la pour pour /qui sera utiliser par cette classe

class ListCreate(CreateView):
   model = ToDoList
   fields = ["title"]

   def get_context_data(self):
       context = super(ListCreate, self).get_context_data()
       context["title"] = "Add a new list"
       return context


class ItemCreate(CreateView):
   model = ToDoItem
   fields = [
    "todo_list",
    "title",
    "description", 
    "due_date",
   ]


def get_initial(self):
       initial_data = super(ItemCreate, self).get_initial()
       todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
       initial_data["todo_list"] = todo_list
       return initial_data
      
def get_context_data(self):
       context = super(ItemCreate, self).get_context_data()
       todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
       context["todo_list"] = todo_list
       context["title"] = "Create a new item"
       return context
      
def get_success_url(self):
       return reverse("mytodo:list", args=[self.object.todo_list_id])
   



class ItemUpdate(UpdateView):
  model = ToDoItem
  fields = [
    "todo_list",
    "title",
    "description",   
    "due_date",
  ]


  def get_context_data(self):
   context = super(ItemUpdate, self).get_context_data()
   context["todo_list"] = self.object.todo_list
   context["title"] = "Edit item"
   return context

def get_success_url(self):
   return reverse("mytodo:list", args=[self.object.todo_list_id])




# Delete

class ListDelete(DeleteView):
   model = ToDoList
   # You have to use reverse_lazy() instead of reverse(),
   # as the urls are not loaded when the file is imported.

   success_url = reverse_lazy("mytodo:index")


class ItemDelete(DeleteView):
   model = ToDoItem
   
   def get_success_url(self):
      return reverse_lazy("mytodo:list", args=[self.kwargs["list_id"]])
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["todo_list"] = self.object.todo_list
      return context