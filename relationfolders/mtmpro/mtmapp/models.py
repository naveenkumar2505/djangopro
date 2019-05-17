from django.db import models
class Students(models.Model):
    sname=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    def __self__(self):
        return self.ename
# class Student(models.Model):
#     sname=models.CharField(max_length=)
#     marks=models.IntegerField()
class Customer(models.Model):
    student=models.ManyToManyField(Students)
    cname=models.CharField(max_length=20)
    sales=models.IntegerField()
    def __self__(self):
        return self.cname
