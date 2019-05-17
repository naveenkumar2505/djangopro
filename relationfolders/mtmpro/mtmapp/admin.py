from django.contrib import admin
from .models import Students,Customer
class AdminStudents(admin.ModelAdmin):
    list_display = ['sname','loc','email']
class AdminCustomer(admin.ModelAdmin):
    list_display = ['cname','sales']
admin.site.register(Students,AdminStudents)
admin.site.register(Customer,AdminCustomer)

