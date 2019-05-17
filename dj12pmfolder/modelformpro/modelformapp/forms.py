from django import forms
from .models import ModelFormData
class ModelFormF(forms.ModelForm):
    class Meta:
        model=ModelFormData
        fields='__all__'