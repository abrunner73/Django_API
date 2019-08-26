from django.db import models

# Create your models here.
class Artists (models.Model):
    mbid = models.CharField(max_length=200)
    tmid -= models.IntegerField()
    name = models.CharField(max_length=100)
    sortName = models.CharField(max_length=100)
    disambiguation = models.CharField(max_length=100)
    url = models.URLField()

