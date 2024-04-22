from django.db import models

# Create your models here.

class Movieinfo(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField()
    summary=models.TextField(default="not found")
