

from django import forms 
from .models import data, data1
import calculation 


class dataForm(forms.ModelForm):
     height = forms.DecimalField(label='Height (in meters)')
     weight = forms.DecimalField(label = 'Weight (in kg)')
     age = forms.IntegerField()
     bmi = forms.DecimalField(
     widget = calculation.FormulaInput('weight/(height*height)') # <- using single math expression
     
    )

     
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
     





class data1Form(forms.ModelForm):
          
          
          fruits = forms.ChoiceField(
          help_text = "<strong>Note:</strong> <strong>Do you like to fruits ?</strong> ",
          choices = (
               ('Yes', "Yes"), 
               ('NO', 'no'),
               
          ), 
          
         widget = forms.RadioSelect,
     
    )
          vegetables = forms.MultipleChoiceField(
               choices = (
               ('potato', "potato"), 
               ('tomato', 'tomato'),
               ('cabbage', 'cabbage'),
               ('brinjal', "brinjal"), 
               ('ladys finger', 'lady finger'),
                ("drumstick", "drumstick"), 
               ('pumpkim', 'pumpkim'),
                ('pointed ground', "pointed ground"), 
               ('spinach', 'spinach')
        ), 
  
        
        widget = forms.CheckboxSelectMultiple,
        
    )
          protein = forms.MultipleChoiceField(
               choices = (
               ('chicken', "chicken"), 
               ('fish', 'fish'),
               ('Egg', "Egg"), 
               ('lanb', 'lanb'),
               ('beef', 'beef'),
               
        ), 
        
        
        widget = forms.CheckboxSelectMultiple,
        
    )
          curbs = forms.MultipleChoiceField(
               choices = (
               ('rice', "rice"), 
               ('ruti', 'ruti'),
               
               
        ), 
        
        
        widget = forms.CheckboxSelectMultiple,
        
    )


          class Meta:
               model = data1
               fields = "__all__"