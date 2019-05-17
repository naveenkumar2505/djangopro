from django.db import models
class Product(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=50)
    product_color=models.CharField(max_length=50)
    product_cost=models.FloatField()
    product_weight=models.IntegerField()

