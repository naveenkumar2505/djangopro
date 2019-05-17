from django.db import models

# Create your models here.
class Emp(models.Model):
    ename=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    def __str__(self):      #string representation
        return self.ename
