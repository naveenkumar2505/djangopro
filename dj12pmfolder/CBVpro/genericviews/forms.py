from django import forms
class PersonForm(forms.Form):
    name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name',
            }
        )
    )
    desc=forms.CharField(
        label='Enter description',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name',
            }
        )
    )