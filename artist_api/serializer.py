from rest_framework import serializers
from .models import Artists

class ArtistSerializer(serializer.ModelSerializer):
    class Meta:
        model = Artists