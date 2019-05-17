from django.contrib import admin
from .models import Student,Courses,Faculty

class StudentAdmin(admin.ModelAdmin):
    list_display = ['sname','email','number']
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['cname']
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['fname','fee']

admin.site.register(Student,StudentAdmin)
admin.site.register(Courses,CoursesAdmin)
admin.site.register(Faculty,FacultyAdmin)