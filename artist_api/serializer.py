from rest_framework import serializers

class ArtistSerializer(serializers.Serializer):
    mbid = serializers.CharField(allow_blank=True,)
    tmid = serializers.IntegerField(required=False)
    name = serializers.CharField(allow_blank=True)
    sortName = serializers.CharField(allow_blank=True)
    disambiguation = serializers.CharField(allow_blank=True,required=False)
    url = serializers.CharField(allow_blank=True)

class ArtistsSerializer(serializers.Serializer):
    type = serializers.CharField(allow_blank=True)
    itemsPerPage = serializers.IntegerField(required=False)
    page = serializers.IntegerField(required=False)
    total = serializers.IntegerField(required=False)
    artist = ArtistSerializer(many=True)