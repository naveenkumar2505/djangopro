from django.db import models
class Student(models.Model):
    sno=models.IntegerField()
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    profile=models.FileField(upload_to='files')
    sloc=models.CharField(max_length=20)
    def __str__(self):
        return self.name
