from django.db import models

# Create your models here.
class Assignment(models.Model):
    name = models.CharField(max_length=128)
    total_score = models.IntegerField()
    instructions = models.CharField(max_length=1024)

class Feedback(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    points = models.IntegerField()
    comment = models.CharField(max_length=256)
    