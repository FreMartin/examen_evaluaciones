from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm


def home(request):
        
    return render(request, 'examen/inicio.html', {})


def registro(request):
    if request.method == 'POST':
        reg_form = RegistroForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            login(request, user) 
            return redirect('examen') 
    else:
        reg_form = RegistroForm()

    return render(request, 'examen/inicio.html', {'reg_form': reg_form})



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('examen')
    else:
        form = AuthenticationForm()

    return render(request, 'examen/login.html', {'form': form})
