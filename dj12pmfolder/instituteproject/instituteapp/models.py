from django.db import models
from multiselectfield import MultiSelectField
class RegistrationData(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    User_Name=models.CharField(max_length=50)
    Password1=models.CharField(max_length=50)
    Password2=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Mobile=models.BigIntegerField()
    dob=models.DateField()
class StudentData(models.Model):
    Name = models.CharField(max_length=50)
    Mobile = models.BigIntegerField()
    Email = models.EmailField(max_length=50)
    startdate = models.DateField()
    COURSES_CHOICES={
        ('python','PYTHON'),
        ('django','DJANGO'),
        ('restapi','RESTAPI'),
        ('ui','UI')
    }
    cources=MultiSelectField(max_length=100,choices=COURSES_CHOICES )
    TRAINER_CHOICE={
        ('narayana','NARAYANA'),
        ('raj','RAJ'),
        ('nani','NANI'),
        ('prakash','PRAKASH')
    }
    trainer=MultiSelectField(max_length=100,choices=TRAINER_CHOICE)
    TIMING_CHOISES={
        ('morning','MORNING'),
        ('afternoon','AFTERNOON'),
        ('evening','EVENING')
    }
    timing=MultiSelectField(max_length=100,choices=TIMING_CHOISES)
class FeedbackData(models.Model):
    name=models.CharField(max_length=50)
    rating=models.IntegerField()
    time=models.DateTimeField()
    feedback=models.CharField(max_length=1000)