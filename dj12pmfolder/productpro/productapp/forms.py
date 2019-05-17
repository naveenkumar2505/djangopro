from django import forms
from .forms import forms

class ProductForm(forms.Form):
    pid=forms.IntegerField(
        label='Enter Product ID',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Product ID'
            }
        )
    )
    pname=forms.CharField(
        label='Enter Product Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Product Name'
            }
        )
    )
    cname=forms.CharField(
        label='Enter Customer Name',
        widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Customer Name'
        }
        )
    )
    cost=forms.IntegerField(
        label='Enter Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )
    color=forms.CharField(
        label='Enter Product color',
        widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Product color'
        }
        )
    )
    weight=forms.IntegerField(
        label='Enter Product Weight',
        widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Product Weight'
        }
        )
    )
    mfgdate=forms.DateField(
         label='Enter date',
         widget=forms.DateInput(
             attrs={
                 'class':'form-control',
                 'placeholder':'Date'
             }
         )
     )
    # expgdate=forms.DateField(
    #      label='Enter date',
    #      widget=forms.DateInput(
    #          attrs={
    #              'class':'form-control',
    #              'placeholder':'Date'
    #          }
    #      )
    # )