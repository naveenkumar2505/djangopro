from django.db import models
from .models import models
class ContactData(models.Model):
    name=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    salary=models.IntegerField()
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=50)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

