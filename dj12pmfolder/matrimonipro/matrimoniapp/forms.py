from django import forms
from django.contrib.auth import get_user_model
user=get_user_model()
class RegistrationForm(forms.Form):
    firstname=forms.CharField(
        label='Enter Your FirstName',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your FirstName'
            }
        )
    )
    lastname=forms.CharField(
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
    password1=forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Password'
            }
        )
    )
    password2=forms.CharField(
        label='Enter Your ConfirmPassword',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your ConfirmPassword'
            }
        )
    )
    mobile=forms.IntegerField(
        label='Enter Your mobileNumber',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your mobile number'
            }
        )
    )
    dob=forms.DateField(
        label='Enter Your Date Of Birth',
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your YYYY-MM-DD'
            }
        )
    )
    email=forms.EmailField(
        label='Enter Your Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )
    )
    gender=forms.CharField(
        label='Enter Your Gender',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your gender'
            }
        )
    )
    loc=forms.CharField(
        label='Enter Your location',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Location'
            }
        )
    )
    job=forms.CharField(
        label='Enter Your Job',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Job'
            }
        )
    )
    salary=forms.IntegerField(
        label='Enter Your Salary',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Salary'
            }
        )
    )
    height=forms.FloatField(
        label='Enter Your height feet',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your height'
            }
        )
    )
    weight=forms.IntegerField(
        label='Enter Your weight in Kg',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your weight'
            }
        )
    )
    color=forms.CharField(
        label='Enter Your color',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your color'
            }
        )
    )
#validation forms
def clean_username(self):
    username=self.cleaned_data.get('username')
    us=user.objects.filter(username=username)
    if us.exists():
        raise forms.ValidationError('User already exists')
    return username
def clean_email(self):
    email=self.cleaned_data.get('email')
    em=user.objects.filter(email=email)
    if em.exists():
        raise forms.ValidationError('email already exists')
    elif '@gmail.com' not in email:
        raise forms.ValidationError('email must contain @gmail.com')
    return email
def clean_mobile(self):
    mobile=self.cleaned_data.get('mobile')
    mb=user.objects.filter(mobile=mobile)
    if mb.exists():
        raise forms.ValidationError('mobile number already exists')
    return mobile
def clean(self):
    data=self.cleaned_data()
    password1=self.cleaned_data.get('password1')
    password2=self.cleaned_data.get('password2')
    if password1!=password2:
        raise forms.ValidationError('password must be match')
    return data

class LoginForm(forms.Form):
    username=forms.CharField(
        label='Enter your Username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your UserName'
            }
        )
    )
    password=forms.CharField(
        label='Enter your Username',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Password'
            }
        )
    )
class PasswordForm(forms.Form):
    username=forms.CharField(
        label='Enter Your UserName',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your UserName'
            }
        )
    )
    password1=forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your password'
            }
        )
    )
    password2=forms.CharField(
        label='Enter Your ConformPassword',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your ConformPassword'
            }
        )
    )