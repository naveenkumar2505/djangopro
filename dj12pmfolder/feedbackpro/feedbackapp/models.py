from django.db import models
class FeedbackData(models.Model):
    name=models.CharField(max_length=50)
    rating=models.IntegerField()
    time=models.DateTimeField()
    feedback=models.CharField(max_length=500)