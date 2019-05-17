from django import forms
from .models import Registration
from django.contrib.auth import get_user_model


user = get_user_model()


class Registration_Form(forms.Form):
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }
        )
    )
    second_name = forms.CharField(
        label='Second name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter surname'
            }

        )
    )
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }

        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }

        )
    )


    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = user.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email already Exists')
        elif not '@gmail.com' in email:
            raise forms.ValidationError('Email should contains @gmail.com')
        return email
