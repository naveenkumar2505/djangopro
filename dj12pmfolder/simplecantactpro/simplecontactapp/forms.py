from django import forms
class ContactForm(forms.Form):
    name =forms.CharField(
        label='Enter First Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your first Name'
            }
        )
    )
    salary=forms.IntegerField(
        label='Enter your salary',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Salary'
            }
        )
    )
    company=forms.CharField(
        label='Enter Your Company',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Company'
            }
        )
    )
    location=forms.CharField(
        label='Enter your location',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Location'
            }
        )
    )
    email=forms.EmailField(
        label='Enter You Email ID',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email ID'
            }
        )
    )
    #name=forms.CharField(max_length=20)
    #loc=forms.CharField(max_length=30)
    #email=forms.EmailField(max_length=50)