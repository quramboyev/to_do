from django.shortcuts import render, redirect
from .forms import RegistrationForm

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
            return redirect('list')

    return render(request, 'registration.html', context={
        'form': form
    })

def login_view(request):
    ...

def logout_view(request):
    ...