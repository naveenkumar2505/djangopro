from django.db import models
from .models import models
class  ConData(models.Model):
    name=models.CharField(max_length=30)
    number=models.BigIntegerField(max_length=30)
    email=models.EmailField(max_length=100)