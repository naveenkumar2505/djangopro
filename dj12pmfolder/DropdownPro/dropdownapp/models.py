from django.db import models
from django import forms
class Drop(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    COLOR_CHOICES = (
        ('green', 'GREEN'),
        ('blue', 'BLUE'),
        ('red', 'RED'),
        ('orange', 'ORANGE'),
        ('black', 'BLACK'),
    )
    color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')

