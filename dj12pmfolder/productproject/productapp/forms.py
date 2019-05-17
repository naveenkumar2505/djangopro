from django import forms
from .models import Product
class ProductModelForm(forms.ModelForm):
    class Meta():
         model=Product
         fields='__all__'

class UpdateForm(forms.ModelForm):
       class Meta():
             model=Product
             fields=['product_id','product_cost','product_color']

class deleteForm(forms.ModelForm):
    class Meta():
        model=Product
        fields=['product_id']
