from django.contrib import admin
from .models import Product,Order,OrderItem
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id','product_name','product_size','product_price']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id','order_name']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['orderId','productId']


admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)

