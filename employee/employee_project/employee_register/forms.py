

from django import forms 
from .models import Employee


class EmployeeForm(forms.ModelForm):
    contact = forms.IntegerField()
  


    class Meta:
        model = Employee
        fields =  ('name','email','password','con_password','country','contact')
        labels = {
            "con_password":"Confirm Password"
        }
        widgets = {
        'password': forms.PasswordInput(),
        'con_password': forms.PasswordInput(),
  
 }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['name'].empty_label = "name"
        self.fields['country'].required = False





    