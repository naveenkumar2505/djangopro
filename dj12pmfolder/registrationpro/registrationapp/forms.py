from django import forms
from .forms import forms
class RegistrationForm(forms.Form):
    first_name=forms.CharField(
        label='Enter Your FirstName',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your FirstName'
            }
        )
    )
    latst_name=forms.CharField(
        label='Enter Your LastName',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your LastName'
            }
        )
    )
    username=forms.CharField(
        label='Enter Your UserName',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your UserName'
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
    mobile=forms.IntegerField(
        label='Enter Your MobileNumber',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Number'
            }
        )
    )
    email=forms.EmailField(
        label='Enter Your EmailID',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your EmailId'
            }
        )
    )
    gender=forms.CharField(
        label='Enter Your gender',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Gender'
            }
        )
    )
class LoginForm(forms.Form):
    username=forms.CharField(
        label='Enter Your username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your username'
            }
        )
    )
    password=forms.CharField(
        label='Enter Your password',
        widget=forms.PasswordInput(
            {
                'class': 'form-control',
                'placeholder': 'Your Password'
            }
        )
    )