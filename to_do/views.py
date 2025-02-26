from django.shortcuts import render, redirect
from .forms import CreateTodoForm, EditTodoForm
from .models import ToDoModel
from django.contrib.auth.decorators import login_required


@login_required
def todo_edit_view(request, id: int):
    obj = ToDoModel.objects.get(id=id)
    form = EditTodoForm(instance=obj)
    if request.method == 'POST':
        form = EditTodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('todo:list')
    return render(request,  'edit.html', context={
        'form': form
    })

def todo_list_view(request):
    if request.user.is_authenticated:
        q = request.GET.get('q', '')
        todos =ToDoModel.objects.all().filter(user=request.user)
        if q:
            todos = todos.filter(title__icontains=q)
        return render(request, 'list.html', context={
        'todos': todos,
        'q': q
    })
    return render(request, 'list.html')
    

@login_required
def todo_create_view(request):
    form = CreateTodoForm()
    if request.method == 'POST':
        form = CreateTodoForm(request.POST)
        if form.is_valid():
            todo = ToDoModel(title=form.cleaned_data['title'], 
                             description=form.cleaned_data['description'], 
                             user=request.user)
            todo.set_current_language('ru')
            todo.save()
            return redirect('to_do:list')

    return render(request, 'create.html', context={
        'form': form
    })

@login_required
def todo_delete_view(request, id:int):
    to_do = ToDoModel.objects.get(id=id)
    to_do.delete()
    return redirect('to_do:list')

@login_required
def todo_detail_view(request, id):
    to_do = ToDoModel.objects.get(id=id)
    return render(request, 'detail.html', context={
        'obj': to_do
    })

@login_required
def change_active_view(request, id):
    to_do = ToDoModel.objects.get(id=id)
    if to_do.is_active:
        to_do.is_active = False
    else:
        to_do.is_active = True

    to_do.save()
    return redirect('todo:detail', id=id)

