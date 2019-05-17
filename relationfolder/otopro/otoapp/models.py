from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    def __str__(self):
        return self.sname
class Course(models.Model):
    cname=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    def __str__(self):
        return self.cname


