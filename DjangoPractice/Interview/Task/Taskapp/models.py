from django.db import models
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=30)
    product_price=models.FloatField()
    product_size=models.IntegerField()
    product_active=models.BooleanField()

class Order(models.Model):
    order_id=models.IntegerField(primary_key=True)
    order_date=models.DateField()
    customer_email=models.EmailField(max_length=256)
    mobile_number=models.BigIntegerField()

class OrderItem(models.Model):
    orderId=models.ForeignKey(Order)
    productId=models.ForeignKey(Product)