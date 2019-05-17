from django.db import models
class Student(models.Model):
    sname=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    email=models.EmailField()
    def __self__(self):
        return self.sname
class Course(models.Model):
    student=models.ForeignKey(Student)
    cname=models.CharField(max_length=20)
    fee=models.IntegerField()
    def __self__(self):
        return self.cname

