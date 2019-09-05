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

class Coordinates(models.Model):
    long = models.FloatField()
    lat = models.FloatField()


class Country(models.Model):
    code = models.CharField(max_length=20,blank=True)
    name = models.CharField(max_length=50,blank=True)


class City(models.Model):
    id = models.CharField(primary_key=True,max_length=20,blank=True)
    name = models.CharField(max_length=50,blank=True)
    stateCode = models.CharField(max_length=2,blank=True)
    state = models.CharField(max_length=20,blank=True)


class Venue(models.Model):
    url = models.URLField(blank=True)
    id = models.CharField(primary_key=True,max_length=20,blank=True)
    name = models.CharField(max_length=50,blank=True)


class Songs(models.Model):
    name = models.CharField(max_length=100,blank=True)
    info = models.CharField(max_length=200,blank=True)
    tape = models.NullBooleanField()

class Set(models.Model):
    name = models.CharField(max_length=50,blank=True)
    encore = models.IntegerField()


class Tour(models.Model):
    name = models.CharField(max_length=50,blank=True)


class SetList(models.Model):
    info = models.CharField(max_length=200,blank=True)
    id = models.CharField(primary_key=True,max_length=20,blank=True)
    versionId = models.CharField(max_length=50,blank=True)
    eventDate = models.CharField(max_length=10,blank=True)
    lastUpdated = models.CharField(max_length=10,blank=True)
    url = models.URLField(blank=True)