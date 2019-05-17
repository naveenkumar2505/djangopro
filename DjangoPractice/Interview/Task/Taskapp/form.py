from django import forms
from .models import Product,Order

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class OrcerForm(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Order