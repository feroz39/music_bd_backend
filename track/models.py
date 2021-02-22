import uuid
from django.db import models
from django.urls import reverse
from .utils import (
    track_unique_slug_generator,
    album_unique_slug_generator,
    artist_unique_slug_generator,
)
from django.db.models.signals import pre_save # Signals

# Path of files

def cover_path(instance, filename):
    filebase, extension = filename.split(".")
    dir = instance.title.replace(' ', '-').lower()
    return "album-{0}/{1}.{2}".format(dir, 'cover', extension)

def track_path(instance, filename):
    dir = instance.album.title.replace(' ', '-').lower()
    fileName = (dir + '-' + instance.title.replace(' ', '-').lower())
    return "album-{0}/{1}.{2}".format(dir, fileName, 'mp3')

def artist_path(instance, filename):
    name, ext = filename.split('.')
    return "artist/{0}/{1}.{2}".format(instance.name.replace(' ', '-').lower(), 'cover', ext)



# Database Tables
class Album(models.Model):
    slug = models.SlugField(blank=True, unique=True, editable=False)
    title = models.CharField(max_length=100)
    released = models.CharField(max_length=4)
    picture = models.FileField(upload_to=cover_path)
    artist = models.ManyToManyField('Artist', related_name='albums',)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().delete(*args, **kwargs)


class Track(models.Model):
    slug = models.SlugField(blank=True, unique=True, editable=False)
    title = models.CharField(max_length=100)
    track_file = models.FileField(upload_to=track_path)
    album = models.ForeignKey('Album', related_name='tracks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.track_file.delete()
        super().delete(*args, **kwargs)


class Artist(models.Model):
    slug = models.SlugField(blank=True, unique=True, editable=False)
    name = models.CharField(max_length=100)
    picture = models.FileField(upload_to=artist_path)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().delete(*args, **kwargs)


# Save the uniqe slug

def album_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = album_unique_slug_generator(instance)

def track_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = track_unique_slug_generator(instance)

def artist_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = artist_unique_slug_generator(instance)


pre_save.connect(album_pre_save_receiver, sender=Album)
pre_save.connect(track_pre_save_receiver, sender=Track)
pre_save.connect(artist_pre_save_receiver, sender=Artist)