from django.db import models
class RegstrationData(models.Model):
    first_name=models.CharField(max_length=100,null=True)
    second_name=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=150)
    password=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)
