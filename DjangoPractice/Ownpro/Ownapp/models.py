from django.db import models

class Product(models.Model):
    product_id =models.AutoField(primary_key=True,max_length=11,default=100)
    product_name=models.CharField(max_length=250,help_text='Product name')
    product_size=models.FloatField()
    product_price=models.FloatField()
    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_id=models.IntegerField()
    order_name=models.CharField(max_length=256,help_text='Order Name')
    def __str__(self):
        return self.order_name

class OrderItem(models.Model):
    orderId=models.ForeignKey(Order)
    productId=models.ForeignKey(Product)
