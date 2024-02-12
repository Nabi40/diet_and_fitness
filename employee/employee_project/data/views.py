from django.shortcuts import render,redirect
from .forms import dataForm, data1Form
from .models import data, data1

# Create your views here.
def data_list(request):
    if request.method == "GET":
        form = data1Form()
        return render(request,"data/data_form.html",{"form":form})
    else:
        form = data1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/data_1_form")




def data_form(request):
    if request.method == "GET":
        form = dataForm()
        return render(request,"data/data_form.html",{"form":form})
    else:
        form = dataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/data/list")
    
def data_delete(request):
        return 

