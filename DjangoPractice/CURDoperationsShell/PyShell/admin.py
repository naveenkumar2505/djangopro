from django.contrib import admin
from .models import Student,Courses,oppertunity
class StudentAdmin(admin.ModelAdmin):
    list_display = ['sname','email','number']
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['cname','fee']
class OpertunityAdmin(admin.ModelAdmin):
    list_display = ['software','softwareDev','softwareTest','softwareAnal','softwareDebug','softwareMaint']
admin.site.register(Student,StudentAdmin)
admin.site.register(Courses,CoursesAdmin)
admin.site.register(oppertunity,OpertunityAdmin)