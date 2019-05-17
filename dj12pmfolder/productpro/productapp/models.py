from django.db import models
class ProductData(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=20)
    cname=models.CharField(max_length=20)
    cost=models.IntegerField()
    color=models.CharField(max_length=20)
    weight=models.IntegerField()
    mfgdate=models.DateField()