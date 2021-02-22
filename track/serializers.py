from rest_framework import serializers
from .models import Track, Album, Artist


class TrackSerializer(serializers.ModelSerializer):
    album_cover = serializers.StringRelatedField(source='album.picture',)
    album = serializers.ReadOnlyField(source='album.title')
    artists = serializers.StringRelatedField(source='album.artist', many=True)

    class Meta:
        model = Track
        fields = ['slug', 'title', 'album', 'artists', 'track_file', 'album_cover']


class AlbumListSerializer(serializers.ModelSerializer):
    artists = serializers.StringRelatedField(source='artist', many=True)
    class Meta:
        model = Album
        fields = ['slug', 'title', 'picture', 'artists', 'released']


class AlbumDetailsSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    artists = serializers.StringRelatedField(source='artist', many=True)
    class Meta:
        model = Album
        fields = ['slug', 'title', 'released', 'picture', 'artists', 'tracks']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['slug', 'name', 'picture']


class ArtistDetailsSerializer(serializers.ModelSerializer):
    albums = AlbumListSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ['slug', 'name', 'picture', 'albums']