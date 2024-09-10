from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm

def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user  = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.username = user.email
            user.save()

            messages.success(request, "Registration succesful! Please Login")
            return redirect(reverse('login'))
        else:
            messages.error(request, "Error in the registration form")

    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form':form})
    
def home(request):
    return render(request, 'index.html')