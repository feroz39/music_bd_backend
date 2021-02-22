from django.urls import path, include
from .views import (
    TrackListAPIView,
    TrackDetailsAPIView,
    AlbumListAPIView,
    AlbumDetailsAPIView,
    ArtistListAPIView,
    ArtistDetailsAPIView,
    SearchAPIView,
)

urlpatterns = [
    path('tracks/', TrackListAPIView.as_view()),
    path('tracks/<slug>/', TrackDetailsAPIView.as_view()),

    path('albums/', AlbumListAPIView.as_view()),
    path('albums/<slug>/', AlbumDetailsAPIView.as_view()),

    path('artists/', ArtistListAPIView.as_view()),
    path('artists/<slug>/', ArtistDetailsAPIView.as_view()),

    path('search/', SearchAPIView.as_view()),
]
