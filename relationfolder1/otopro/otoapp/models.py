from django.db import models
class Student(models.Model):
    ename=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    def __str__(self):
        return self.ename
class Course(models.Model):
    student=models.OneToOneField(Student)
    cname=models.CharField(max_length=20)
    fee=models.IntegerField()
    def __str__(self):
        return self.cname