from django import forms
from .forms import forms
class ContactForm(forms.Form):
    name=forms.CharField(
        label='Enter your name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    company=forms.CharField(
        label='Enter Your company',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your company'
            }
        )
    )
    salary=forms.IntegerField(
        label='Enter Your salary',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Your salary'
            }
        )
    )
    mobile=forms.IntegerField(
        label='Enter your mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your mobile'
            }
        )
    )
    email=forms.EmailField(
        label='Enter Your mobile EmailID',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email ID'
            }
        )
    )
    username=forms.CharField(
        label='Enter Your UserName',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Username'
            }
        )
    )
    password=forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Password'
            }
        )
    )