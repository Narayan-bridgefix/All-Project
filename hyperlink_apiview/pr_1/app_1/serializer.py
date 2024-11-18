from rest_framework import serializers
from .models import *
class AlbumSerializer(serializers.ModelSerializer):
    # tracks = serializers.StringRelatedField(many=True)
    # tracks2 = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='track-detail'
    # )
    # track_listing = serializers.HyperlinkedIdentityField(view_name='track-list')

    class Meta:
        model = Album
        fields = ['track_listing','album_name', 'artist']