from django.contrib import admin
from .models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ['sno','name','sloc','image','profile']
admin.site.register(Student,StudentAdmin)
