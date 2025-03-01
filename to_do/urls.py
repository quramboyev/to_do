from django.urls import path
from .views import todo_list_view, todo_create_view, todo_delete_view, todo_detail_view, \
    change_active_view, todo_edit_view, form_view

app_name = "todo"

# {% url 'todo:list' %}

urlpatterns = [
    path('', todo_list_view, name='list'),
    path('create/', todo_create_view, name='create'),
    path('delete/<int:id>/', todo_delete_view, name='delete'),
    path('detail/<int:id>/', todo_detail_view, name="detail"),
    path('change/<int:id>/', change_active_view, name='change'),
    path('edit/<int:id>/', todo_edit_view, name='edit'),
    path('fake/', form_view, name='fakeform'),
]