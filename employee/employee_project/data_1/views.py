from django.shortcuts import render,redirect
from .forms import chartForm
from .models import chart
# Create your views here.
def data_1_list(request):
    if request.method == "GET":
        form = chartForm()
        
        return render(request,"data_1/data_1_list.html",{"form":form})
    
    else:
        form = chartForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("data_1_see")

def data_1_form(request):
    if request.method == "GET":  
        form = chartForm()    
        return render(request,"data_1_see",{"form":form})
    else:
        form = chartForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("data_1_see")
    
def data_1_see(request):
    context = {"data_1_see":chart.objects.all()}  
    return render(request,"data_1/data_1_see.html",context)


def data_delete(request):
        return 



