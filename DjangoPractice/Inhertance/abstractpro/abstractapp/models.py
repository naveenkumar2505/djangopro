from django.db import models

class CommanData(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    number=models.BigIntegerField()
    class Meta:
        abstract=True
class Student(CommanData):
    branch=models.CharField(max_length=20)
class Faculty(CommanData):
    subject=models.CharField(max_length=20)