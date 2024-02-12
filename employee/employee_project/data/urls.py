
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.data_form, name = 'data'),
    path('list/',views.data_list,  name = 'data_list')
]

