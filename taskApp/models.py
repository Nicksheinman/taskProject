from django.db import models

# Create your models here.

class Task(models.Model):
    name=models.CharField(max_length=256)
    explain=models.CharField(max_length=256)
    status=models.CharField(max_length=256)
    date=models.DateField(null=True)