from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


def registration_view(request):
    form = RegistrationForm()
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            del form
            return redirect('login')

    return render(request, 'registration.html', context={
        'form': form
    })

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
        if user is not None:
            login(request, user)
            return redirect('todo:list')
        form.add_error('password',"username yoki parol notogri")

    return render(request, 'login.html', context={
        'form': form
    })

@login_required
def logout_view(request):
    logout(request)
    return redirect('todo:list')