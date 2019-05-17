from django.db import models
class EmployeeData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    salary=models.BigIntegerField()
    dob=models.DateField()
    role=models.CharField(max_length=50)
