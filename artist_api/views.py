from django.shortcuts import render
from django.http import request
from django.conf import settings
from artist_api.serializer import ArtistSerializer
import requests

# Create your views here.

def load_artist(request):

    header = {'Accept': 'application/json','x-api-key': settings.API_KEY}

    r = requests.get("https://api.setlist.fm/rest/1.0/artist/8e3fcd7d-bda1-4ca0-b987-b8528d2ee74e",headers=header)

    json = r.json()

    s = ArtistSerializer(data=json)

    if s.is_valid():
        artist = s.save()

        return render(request, 'artist.html', {'artist': artist})
    else:
        return render(request, 'error.html')


