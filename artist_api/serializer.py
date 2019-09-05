from rest_framework import serializers
from artist_api.models import Artist, ArtistSearch, Coordinates, Country, City, Venue, Songs, Set, Tour, SetList

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'


class ArtistSearchSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True)

    class Meta:
        model= ArtistSearch
        fields = '__all__'

    #def create(self, validated_data):
    #    return ArtistSearch.objects.create(**validated_data)


class CoordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Coordinates
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    coords = CoordSerializer()
    country = Country()

    class Meta:
        model = City
        fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Venue
        fields = '__all__'


class SongsSerializer(serializers.ModelSerializer):
    withh = ArtistSerializer(many=True)
    cover = ArtistSerializer()

    class Meta:
        model = Songs
        fields = '__all__'


class SetSerializer(serializers.ModelSerializer):
    song = SongsSerializer(many=True)

    class Meta:
        model = Set
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class SetListSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True,required=False)
    venue = VenueSerializer(many=True,required=False)
    tour = TourSerializer(many=True,required=False)
    set = SetSerializer(many=True,required=False)

    class Meta:
        model = SetList
        fields = '__all__'
