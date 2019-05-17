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
    second_name=forms.CharField(
        label='Enter Your LastName',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your LastName'
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

    def clean_email(self):
        #email=self.cleaned_data.get('email')
        email=self.cleaned_data['email']
        emails=user.objects.filter(email=email)
        if emails.exists():
            raise forms.ValidationError('Email already Exists')
        elif not '@gmail.com' in emails:
              raise forms.ValidationError('Email should contains @gmail.com')
        return email
    def clean_password(self):
        password=self.cleaned_data.get('password')
        MIN_LENGTH=8
        if password.isdigit():
            raise forms.ValidationError('password should not be digit')
        if len(password)<MIN_LENGTH:
            raise forms.ValidationError('password must be 8 char')
        return password

