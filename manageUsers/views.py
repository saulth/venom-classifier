from dataclasses import dataclass
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class viewRegister(View):
    
    def get(self, request):
        form=UserCreationForm()
        return render(request, "manageUsers/register.html", {"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request, user)
            
            return redirect('Home')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request, "manageUsers/register.html", {"form":form})


def close_session(request):
    logout(request)

    return redirect('Home')

def logIn(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get("username")
            pasw=form.cleaned_data.get("password")

            user=authenticate(username=user_name, password=pasw)

            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.error(request, "Username or Password incorrect")
        else:
            messages.error(request, "Incorrect Username or Password")

    form=AuthenticationForm()
    return render(request, "manageUsers/login.html", {"form":form})

