from django.db import models
class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    salary=models.BigIntegerField()
    company=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
class Login(models.Model):
    user=models.CharField(max_length=250)
    password=models.CharField(max_length=100)
    dob=models.DateField()