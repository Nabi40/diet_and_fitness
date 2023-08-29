from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 
from .models import data


class dataForm(forms.ModelForm):
     height = forms.DecimalField()
     weight = forms.DecimalField()
     age = forms.IntegerField()
     
     description = forms.CharField(
        widget = forms.Textarea(),
     
  )
     disease = forms.MultipleChoiceField(
        choices = (
            ('blood_Pressure', "Blood Pressure"), 
            ('heart_Diseases', 'Heart Diseases'),
            ('diabetes', 'Diabetes')
        ), 
        
        
        widget = forms.CheckboxSelectMultiple,
        help_text = "<strong>Note:</strong> If you have nothing to write in the description box just write <strong>N/A</strong> ",
    )




     sex = forms.ChoiceField(
          choices = ( 
               ('male', "Male"), 
               ('female', 'Female'),
               ('third_gender', 'Third Gender'),
               
          ), 
          
          
          widget = forms.RadioSelect,
     
    )




       
       
     class Meta:
          model = data
          fields = "__all__"
          labels = {
            "height":"Height (in meters)",
            "weight":"Weight (in kg)",
            
          }
  


 
     def __init__(self, *args, **kwargs):
          super(dataForm, self).__init__(*args, **kwargs)
          self.fields['disease'].required = False
     



class CreateUserForm(UserCreationForm):
     class Meta:
          model = User
          fields = ['username', 'password1', 'password2']
          labels = {
            "username":"Email",
           
            
          }