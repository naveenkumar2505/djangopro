from django.db import models

# Create your models here.
class RegstrationData(models.Model):
    first_name=models.CharField(max_length=100,null=True)
    second_name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=150)
    password=models.CharField(max_length=50)
