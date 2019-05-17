from django import forms
from multiselectfield import MultiSelectFormField
from django.forms.extras.widgets import SelectDateWidget
class RegistrationForm(forms.Form):

    First_Name=forms.CharField(
        label='Enter Your FirstName',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your FirstName'
            }
        )
    )
    Last_Name=forms.CharField(
        label='Enter Your LastName',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your LastName'
            }
        )
    )
    User_Name=forms.CharField(
        label='Enter Your LastName',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your UserName'
            }
        )
    )
    Password1=forms.CharField(
        label='Enter Your LastName',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'your Password'
            }
        )
    )
    Password2=forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Conform Password'
            }
        )
    )
    Email=forms.EmailField(
        label='Enter Your EmailId',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Eaiml'
            }
        )
    )
    Mobile=forms.IntegerField(
        label='Enter Your Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your mobile Number'
            }
        )
    )
    dob=forms.DateField(
        label='Enter your DOB',
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your DOB'
            }
        )
    )

class LoginForm(forms.Form):
    User_Name=forms.CharField(
        label='Enter Your UserName',
        widget=forms.TextInput(
            attrs={
                'class':'from-control',
                'placeholder':'Your UserName'
            }
        )
    )
    Password=forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'from-control',
                'placeholder':'your password'
            }
        )
    )
class StudentForm(forms.Form):
    Name = forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your Name'
            }
        )
    )
    Mobile = forms.IntegerField(
        label='Enter Your Mobile',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your Mobile'
            }
        )
    )
    COURSES_CHOICES = {
        ('python', 'PYTHON'),
        ('django', 'DJANGO'),
        ('restapi', 'RESTAPI'),
        ('ui', 'UI')
    }
    cources=MultiSelectFormField(max_length=100,choices=COURSES_CHOICES)
    TRAINER_CHOICE = {
        ('narayana', 'NARAYANA'),
        ('raj', 'RAJ'),
        ('nani', 'NANI'),
        ('prakash', 'PRAKASH')
    }
    trainer=MultiSelectFormField(max_length=100,choices=TRAINER_CHOICE)
    TIMING_CHOISES = {
        ('morning', 'MORNING'),
        ('afternoon', 'AFTERNOON'),
        ('evening', 'EVENING')
    }
    timing=MultiSelectFormField(max_length=100,choices=TIMING_CHOISES)
    year=range(2019,1970,-1)
    startdate=forms.DateField(
        widget=forms.extras.SelectDateWidget(years=year)
    )
class FeedbackForm(forms.Form):
    name=forms.CharField(
        label='Enter your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating=forms.IntegerField(
        label='Enter Your rating',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )
    feedback=forms.CharField(
        label="Enter your feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your feedback'
            }
        )
    )
class PasswordForm(forms.Form):

    User_Name=forms.CharField(
        label='Enter your username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your UserName'
            }
        )
    )
    Password1 = forms.CharField(
        label='Enter your  Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Password'
            }
        )
    )
    Password2=forms.CharField(
        label='Enter your Confirmation Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirmation Password'
            }
        )
    )