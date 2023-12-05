
from django.urls import path

from .views import TodoListView,ItemListView,ListCreate,ListDelete,ItemCreate,ItemUpdate,ItemDelete

app_name = 'mytodo'

urlpatterns = [
    path('',TodoListView.as_view(),name='index'),

    path("list/<int:list_id>/",ItemListView.as_view(), name="list"),


    # now CRUD for ToDoLists Model  begin Here
    path("list/add/",ListCreate.as_view(), name="list-add"),

    path("list/<int:pk>/delete/",ListDelete.as_view(), name="list-delete"),


    # now CRUD for ToDoItems Model  begin Here

    path("list/<int:list_id>/item/add/",ItemCreate.as_view(),name="item-add",),

    path("list/<int:list_id>/item/<int:pk>/",ItemUpdate.as_view(),name="item-update",),

    path("list/<int:list_id>/item/<int:pk>/delete/",ItemDelete.as_view(),name="item-delete",),
]