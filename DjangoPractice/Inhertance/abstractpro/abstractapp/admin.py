#username==        password==

from django.contrib import admin
from .models import Student,Faculty

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','email','number','branch']

class FaculryAdmin(admin.ModelAdmin):
    list_display = ['name','email','number','subject']

admin.site.register(Student,StudentAdmin)
admin.site.register(Faculty,FaculryAdmin)