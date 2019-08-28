from django.db import models

# Create your models here.
class Artist (models.Model):
    mbid = models.CharField()
    tmid = models.IntegerField()
    name = models.CharField()
    sortName = models.CharField()
    disambiguation = models.CharField()
    url = models.CharField()


