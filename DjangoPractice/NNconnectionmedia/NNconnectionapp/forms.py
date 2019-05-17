from django import forms
from .models import Registration,Login
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        fields='__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'