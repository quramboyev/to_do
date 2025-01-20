from django.urls import path
from .views import todo_list_view, todo_create_view


urlpatterns = [
    path('', todo_list_view, name='list'),
    path('create/', todo_create_view, name='create')
]