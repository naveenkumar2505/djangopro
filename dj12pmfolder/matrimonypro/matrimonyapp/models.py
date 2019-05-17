from django.db import models

class Register(models.Model):
    name =models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    mname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    age = models.IntegerField()
    weight = models.IntegerField()
    gender = models.CharField(max_length=20)
    salary = models.IntegerField(null=True)
    height = models.FloatField(null=True)
    email = models.EmailField(max_length=20)
    mobile = models.CharField(max_length=20)
    phote = models.ImageField(upload_to='images', max_length=200  )
    
