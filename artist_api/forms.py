from django.forms import ModelForm
from artist_api.models import Artist

class ArtistSearchForm(ModelForm):

    class Meta:
        model = Artist
        fields = ['name']
