from django.shortcuts import render

# Create your views here.

def register_list(request):
    return render(request,"registers/ registers.html")

def register(request):
    return render(request,"registers/registers.html")

def register_delete(request):
    return 