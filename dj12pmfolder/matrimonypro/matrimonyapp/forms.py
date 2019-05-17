from django import forms
from .models import Register

class RegistrationForm(forms.Form):
    name = forms.CharField(
        label='Name',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Name Here'
            }
        )
    )
    fname = forms.CharField(
        label='Father Name',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Father Name Here'
            }
        )
    )
    mname = forms.CharField(
        label='Mother Name',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Mother Name Here'
            }
        )
    )
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your Username here'
            }
        )
    )
    password= forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your Password here'
            }
        )
    )
    age = forms.CharField(
        label='Age',
        widget= forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Age Here'
            }
        )
    )
    weight = forms.IntegerField(
        label='Weight',
        widget= forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Weight Here'
            }
        )
    )


    gender = forms.CharField(
        label='Gender',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Gender Here'
            }
        )
    )
    salary = forms.IntegerField(
        label='Enter Your Salary',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Salary Here'
            }
        )
    )
    height = forms.FloatField(
        label="Enter your height (in cms) ",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Height Here'
            }
        )
    )

    email = forms.CharField(
        label='Email',
        widget= forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Email Here'
            }
        )
    )

    number = forms.CharField(
        label='Number',
        widget= forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Number Here'
            }
        )
    )



class LoginForm(forms.Form):
    username = forms.CharField(
           widget=forms.TextInput(
               attrs={
                   'class':'form-control',
                   'placeholder':'User name',
               }
           )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )

