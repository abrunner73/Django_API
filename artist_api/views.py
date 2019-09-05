from django.shortcuts import render
from django.http import request
from django.conf import settings
from artist_api.serializer import ArtistSerializer, ArtistSearchSerializer, SetListSerializer
import requests

# Create your views here.

def load_artist(request):

    header = {'Accept': 'application/json','x-api-key': settings.API_KEY}

    r = requests.get("https://api.setlist.fm/rest/1.0/artist/8e3fcd7d-bda1-4ca0-b987-b8528d2ee74e",headers=header)

    json = r.json()

    s = ArtistSerializer(data=json)

    if s.is_valid():
        #artist = s.save()

        return render(request, 'artist.html', {'artist': s.data})
    else:
        return render(request, 'error.html')


def artist_search_result_view(request):

    header = {'Accept': 'application/json','x-api-key': settings.API_KEY}

    r = requests.get("https://api.setlist.fm/rest/1.0/search/artists?artistName=genesis&p=1&sort=relevance",headers=header)

    json = r.json()

    s = ArtistSearchSerializer(data=json)

    if s.is_valid():
        #artists = s.save()

        return render(request, 'artists.html', {'artists': s.data['artist']})
    else:
        return render(request, 'error.html')


def setlist_result_view(request):

    header = {'Accept': 'application/json','x-api-key': settings.API_KEY}

    r = requests.get("https://api.setlist.fm/rest/1.0/search/setlists?artistMbid=8e3fcd7d-bda1-4ca0-b987-b8528d2ee74e&date=08-06-1992&p=1",headers=header)

    json = r.json()

    s = SetListSerializer(data=json)

    if s.is_valid():

         #print(json['setlist'][0])

         return render(request,'setlist.html', {'setlist': json['setlist'][0]})
