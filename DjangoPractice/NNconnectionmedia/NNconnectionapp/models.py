from django.db import models

class Registration(models.Model):
    firstname=models.CharField(null=True,max_length=100,help_text='Enter FirstName')
    surname=models.CharField(null=True,max_length=100,help_text='Enter LastName')
    email=models.EmailField(max_length=256)
    number=models.BigIntegerField()
    password=models.CharField(max_length=10)
    dob=models.DateField()
    gender=models.CharField(max_length=5)
class Login(models.Model):
    user=models.CharField(max_length=250)
    password=models.CharField(max_length=10)
