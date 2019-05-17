from django.db import models
# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    def __self__(self):
        return self.sname
class Course(models.Model):
    student=models.ManyToManyField(Student)
    cname=models.CharField(max_length=20)
    fee=models.IntegerField()
    def __self__(self):
        return self.cname