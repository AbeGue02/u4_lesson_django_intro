from rest_framework import serializers
from .models import Artist, Song

class SongSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        read_only=True
    )

    song_url = serializers.ModelSerializer.serializer_url_field(
        view_name='artist_detail'
    )

    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist'
    )

    class Meta:
        model = Song
        fields = ('id','song_url','artist_id','artist', 'title', 'album', 'preview_url')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    # songs = serializers.HyperlinkedRelatedField(
    #     view_name='song_detail',
    #     many=True,
    #     read_only=True
    # )

    songs = SongSerializer(
        many=True,
        read_only=True
    )

    artist_url = serializers.ModelSerializer.serializer_url_field(
        view_name='artist_detail'
    )

    class Meta:
        model = Artist
        fields = ('id', 'artist_url','photo_url', 'nationality', 'name', 'songs')


