from django.db import models

class Student(models.Model):
     sname=models.CharField(max_length=50)
     email=models.EmailField(max_length=50)
     number=models.BigIntegerField()
     def __str__(self):
          return self.sname
class Courses(models.Model):
     student=models.ForeignKey(Student)
     cname=models.CharField(max_length=50)
     #cfee=models.BigIntegerField()
     def __str__(self):
          return self.cname
class Faculty(models.Model):
     student=models.ManyToManyField(Student)
     fname=models.CharField(max_length=50)
     fee=models.BigIntegerField()
     def __str__(self):
          return self.fname
