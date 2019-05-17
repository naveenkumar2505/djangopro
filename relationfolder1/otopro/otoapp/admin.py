from django.contrib import admin

from .models import Student,Course
# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display = ['ename','loc','email']
class AdminCourses(admin.ModelAdmin):
    list_display = ['cname','fee']
admin.site.register(Student,AdminStudent)
admin.site.register(Course,AdminCourses)