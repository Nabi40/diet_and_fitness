
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.data_1_form, name = 'data_1'),
    path('list/',views.data_1_list,  name = 'data_1_list'),
    path('see/',views.data_1_see,  name = 'data_1_see'),
   
]

