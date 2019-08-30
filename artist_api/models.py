from django.db import models

# Create your models here.
class Artist (models.Model):
    mbid = models.CharField(blank=True,max_length=200)
    tmid = models.IntegerField(null=True,blank=True)
    name = models.CharField(blank=True,max_length=200)
    sortName = models.CharField(blank=True,max_length=200)
    disambiguation = models.CharField(blank=True,max_length=200)
    url = models.URLField(blank=True)


class ArtistSearch(models.Model):
    type = models.CharField(blank=True, max_length=50)
    itemsPerPage = models.IntegerField(null=True)
    page = models.IntegerField(null=True)
    total = models.IntegerField(null=True)


