from django.db import models

class Registration(models.Model):
    first_name=models.CharField(max_length=100)
    second_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=20)
