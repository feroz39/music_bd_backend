from django.contrib import admin
from .models import Album, Track, Artist

admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Artist)