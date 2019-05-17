from django.contrib import admin
from .models import Student,Course
# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display = ['sname','loc','email']
class AdminCourse(admin.ModelAdmin):
    list_display = ['cname','fee']
admin.register(Student,AdminStudent)
admin.register(Course,AdminCourse)




