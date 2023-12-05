
from django.urls import path

from .views import TodoItemListView,TodoItemCreateView,TodoItemUpdateView,TodoItemDeleteView

app_name = 'todo'


urlpatterns = [
    path('list/', TodoItemListView.as_view(),name='todo_list'),
    path('create/', TodoItemCreateView.as_view(),name='todo_create'),
    path('update/<int:pk>', TodoItemUpdateView.as_view(),name='todo_update'),
    path('delete/<int:pk>', TodoItemDeleteView.as_view(),name='todo_delete'),
]
