from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=256)
    password=models.CharField(max_length=256)
    email=models.CharField(max_length=256)

class Task(models.Model):
    name=models.CharField(max_length=256)
    explain=models.CharField(max_length=256)
    status=models.CharField(max_length=256)
    date=models.CharField(max_length=256)