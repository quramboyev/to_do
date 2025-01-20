from django.shortcuts import render

def todo_list_view(request):
    return render(request, 'list.html')

def todo_create_view(request):
    return render(request, 'create.html')

def todo_delete_view(request, id):
    ...

def todo_detail_view(request, id):
    ...

