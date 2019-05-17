from django import forms
class Emp(forms.Form):
    name=forms.CharField(max_length=20)
    loc=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=50)