from django import forms
from .models import Drop
class MyModelForm(forms.ModelForm):
    class Meta:
        model=Drop
        fields = ['first_name',
                  'last_name',
                  'email',
                  'age',
                  'color',
                  'gender']
        CHOICES = (('F', 'Male',), ('F', 'Female',))
        gender = forms.ChoiceField(
            widget=forms.RadioSelect(),
            choices=CHOICES
        )
