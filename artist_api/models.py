from django.db import models

# Create your models here.
class Artist (models.Model):
    #id = models.IntegerField()
    mbid = models.CharField(blank=True,max_length=200)
    tmid = models.IntegerField(null=True,blank=True)
    name = models.CharField(blank=True,max_length=200)
    sortName = models.CharField(blank=True,max_length=200)
    disambiguation = models.CharField(blank=True,max_length=200)
    url = models.URLField(blank=True)


