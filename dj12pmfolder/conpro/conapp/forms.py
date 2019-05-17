from django import forms
from .forms import forms
class ConForm(forms.Form):
    name=forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    number=forms.IntegerField(
        label='Enter Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your number'
            }
        )
    )
    email=forms.EmailField(
        label='Enter your email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email id'
            }
        )
    )