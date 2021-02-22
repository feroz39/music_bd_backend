from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import generics
from drf_multiple_model.views import ObjectMultipleModelAPIView
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination

from .models import Track, Album, Artist
from .serializers import (
    TrackSerializer,
    AlbumListSerializer,
    AlbumDetailsSerializer,
    ArtistSerializer,
    ArtistDetailsSerializer,
)

# List Track
class TrackListAPIView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

# Single Track
class TrackDetailsAPIView(generics.RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    lookup_field = 'slug'

# List of Album
class AlbumListAPIView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumListSerializer

# Single Album
class AlbumDetailsAPIView(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumDetailsSerializer
    lookup_field = 'slug'

# List of Artist
class ArtistListAPIView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# Single Artist
class ArtistDetailsAPIView(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistDetailsSerializer
    lookup_field = 'slug'


# Search Album, Singer or/and Artist
class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 2

class SearchAPIView(ObjectMultipleModelAPIView):
    pagination_class = LimitPagination
    filter_backends = [filters.SearchFilter]

    def title_filter(queryset, request, *args, **kwargs):
        letter_to_filter = request.query_params['filter']
        return queryset.filter(title__icontains=letter_to_filter)

    def name_filter(queryset, request, *args, **kwargs):
        letter_to_filter = request.query_params['filter']
        return queryset.filter(name__icontains=letter_to_filter)

    querylist = (
        {
            'queryset': Album.objects.all(),
            'serializer_class': AlbumListSerializer,
            'filter_fn': title_filter
        },
        {
            'queryset': Track.objects.all(),
            'serializer_class': TrackSerializer,
            'filter_fn': title_filter
        },
        {
            'queryset': Artist.objects.all(),
            'serializer_class': ArtistSerializer,
            'filter_fn': name_filter
        },
    )