
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from employe_project import settings 
from .forms import dataForm, CreateUserForm
from .models import data

from .models import *

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "dashbord.html")


    else:
        return render(request, "home.html")
 


def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST) 
        if form.is_valid():
            form.save() 

            password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            user = authenticate(username=username, password=password, )
            login(request, user)

            return redirect('login')
       

        else:
            return render(request, "auth/signup.html",{'form': form})
           
       




    else:    
        form = CreateUserForm()
        return render(request, "auth/signup.html",{'form': form})
    



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('root')
            

        
        else:
            return render(request, "auth/login.html",{'form': form})



    else:
        form = AuthenticationForm()
        return render(request,"auth/login.html",{'form': form})    




def data_form(request):
    if request.method == "GET":
        form = dataForm()
        return render(request,"data/data_form.html",{"form":form})
    else:
        form = dataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/data/list")




def logout_view(request):
    logout(request)
    return redirect('root')