

from django import forms 
from .models import chart


class chartForm(forms.ModelForm):
  
     Notes = forms.CharField(
        widget = forms.Textarea(),
     
     )
       
       
     class Meta:
          model = chart
          fields = "__all__"
          
  


 
     def __init__(self, *args, **kwargs):
          super(chartForm, self).__init__(*args, **kwargs)
        
          self.fields['Notes'].required = False
     





