from django.db import models

class Product(models.Model):

    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField('product Name',max_length=50)
    product_size=models.IntegerField()
    product_price=models.BigIntegerField()
    product_active=models.BooleanField()

    def __str__(self):
        return self.product_name


class Order(models.Model):

    order_id=models.IntegerField(primary_key=True)
    order_date=models.DateField()
    customer_name=models.CharField('Customer name',max_length=256)
    customer_number=models.BigIntegerField()

    def __str__(self):
        return self.order_id

class OrderItem(models.Model):

    orderid=models.ForeignKey(Order)
    productid=models.ForeignKey(Product)

