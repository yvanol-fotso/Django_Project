from django.db import models

# Create your models here.
from django.utils import timezone
from django.db import models
from django.urls import reverse


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    #url de redirection lorsque tout s'est bien passe.NB on a utiliser les route Nomme

    def get_absolute_url(self):
        return reverse("mytodo:list", args=[self.id])


    def __str__(self):
       return self.title


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    
    #url de redirection lorsque tout s'est bien passe.NB on a utiliser les route Nomme
     
    def get_absolute_url(self):
     return reverse("mytodo:item-update", args=[str(self.todo_list.id), str(self.id)])

    def __str__(self):
     return f"{self.title}: due {self.due_date}"

    class Meta:
       ordering = ["due_date"]
