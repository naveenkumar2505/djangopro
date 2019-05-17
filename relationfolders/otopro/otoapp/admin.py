from django.contrib import admin
from .models import Student,Course
class AdminStuden(admin.ModelAdmin):
    list_display = ['ename','loc','email']
class AdminCourses(admin.ModelAdmin):
    list_display = ['cname','fee']
admin.site.register(Student,AdminStuden)
admin.site.register(Course,AdminCourses)

