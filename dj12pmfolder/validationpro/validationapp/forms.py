from django import forms
from .forms import forms
from django.contrib.auth import get_user_model
user=get_user_model()
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
    last_name=forms.CharField(
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
    email=forms.EmailField(
        label='Enter Your Emai Id',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email Id'
            }
        )
    )
    password=forms.CharField(
        label='Enter Your password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your password'
            }
        )
    )
    password2=forms.CharField(
        label='Enter Your conform password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':' conform Your password'
            }
        )
    )
    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=user.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username Already exists')
        return username
    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs=user.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email already Exists')
        elif not '@gmail.com' in email:
              raise forms.ValidationError('Email should contains @gmail.com')
        return email
    def clean(self):
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
        if password2!=password:
            raise forms.ValidationError('password should be match')
        elif len(password)<=3 or len(password)>7:
            raise forms.ValidationError('password should contains min 3 and max 7')