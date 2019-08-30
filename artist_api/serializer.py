from rest_framework import serializers
from artist_api.models import Artist, ArtistSearch

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        exclude = ['id']


class ArtistsSerializer(ArtistSerializer):
    artist = ArtistSerializer(many=True)

    class Meta:
        model= ArtistSearch
        exclude = ['id']

    def create(self, validated_data):
        return ArtistSearch.objects.create(**validated_data)


class CoordSerializer(serializers.Serializer):
    long = serializers.FloatField()
    lat = serializers.FloatField()


class CountrySerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()


class CitySerializer(serializers.Serializer):
    id = serializers.CharField(allow_blank=True)
    name = serializers.CharField(allow_blank=True)
    stateCode = serializers.CharField(allow_blank=True)
    state = serializers.CharField(allow_blank=True)
    coords = CoordSerializer()
    country = CountrySerializer()


class VenueSerializer(serializers.Serializer):
    city = CitySerializer()
    url = serializers.URLField(allow_blank=True)
    id = serializers.CharField(allow_blank=True)
    name = serializers.CharField(allow_blank=True)


class SongSerializer(serializers.Serializer):
    name = serializers.CharField(allow_blank=True)
    withh = ArtistSerializer()
    cover = ArtistSerializer()
    info = serializers.CharField(allow_blank=True)
    tape = serializers.NullBooleanField()


class SetSerializer(serializers.Serializer):
    name = serializers.CharField(allow_blank=True)
    encore = serializers.IntegerField(required=False)
    song = SongSerializer(many=True)


class TourSerializer(serializers.Serializer):
    name = serializers.CharField(allow_blank=True)


class SetListSerializer(serializers.Serializer):
    artist = ArtistSerializer()
    venue = VenueSerializer()
    tour = TourSerializer()
    set = SetSerializer(many=True)
    info = serializers.CharField(allow_blank=True)
    id = serializers.CharField(allow_blank=True)
    versionId = serializers.CharField(allow_blank=True)
    eventDate = serializers.CharField(allow_blank=True)
    lastUpdated = serializers.CharField(allow_blank=True)
    url = serializers.URLField(allow_blank=True)


class ConcertSerializer(serializers.Serializer):
    type = serializers.CharField(allow_blank=True)
    itemsPerPage = serializers.IntegerField(required=False)
    page = serializers.IntegerField(required=False)
    total = serializers.IntegerField(required=False)
    setlist = SetListSerializer(many=True)
