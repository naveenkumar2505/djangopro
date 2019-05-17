from django.db import models

class RegistrationData(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    user_name=models.CharField(max_length=100)
    mobile_number=models.BigIntegerField()
    email=models.EmailField(max_length=50)


    def __str__(self):
        return self.first_name
