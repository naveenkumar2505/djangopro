from django.db import models
class CurdData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    def __str__(self):
        self.last_name
class Student(models.Model):
    sname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    number=models.IntegerField()
    def __str__(self):
        return self.sname
class Courses(models.Model):
    student=models.OneToOneField(Student)
    cname=models.CharField(max_length=50)
    fee=models.IntegerField()
class oppertunity(models.Model):
    student=models.ForeignKey(Student)
    software=models.CharField(max_length=50)
    softwareDev=models.CharField(max_length=50)
    softwareTest=models.CharField(max_length=50)
    softwareAnal=models.CharField(max_length=50)
    softwareDebug=models.CharField(max_length=50)
    softwareMaint=models.CharField(max_length=50)