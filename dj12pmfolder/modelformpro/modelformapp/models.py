from django.db import models
class ModelFormData(models.Model):
    userid=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    sal=models.IntegerField()
    loc=models.CharField(max_length=100)
