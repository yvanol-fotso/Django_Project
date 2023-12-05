from django import forms
from .models import TodoItem

class TodoItemCreateForm(forms.ModelForm):
	class Meta:
		model = TodoItem
		fields = ('title','body','due_date','category')




# pour la mise a jour

class TodoItemUpdateForm(forms.ModelForm):
	class Meta:
		model = TodoItem
		fields = ('title','body','due_date','task_finished','category')

