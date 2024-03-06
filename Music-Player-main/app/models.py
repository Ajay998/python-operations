from django.db import models
from django.contrib.auth.models import User
import uuid


def default_music_photo():
    return "https://cdn.saleminteractivemedia.com/shared/images/default-cover-art.png"

class Artist(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Music(models.Model):
    name = models.CharField(max_length=30)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, null=True, blank=True)
    photo = models.ImageField(upload_to="music_photos",default=default_music_photo)
    file = models.FileField(upload_to="music_files")
    added_at = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} by {self.artist.name}"

class Playlist(models.Model):
    name = models.CharField(max_length=30, blank=True)
    songs = models.ManyToManyField(Music, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="playlist_photos", default=default_music_photo)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.name:
            count = Playlist.objects.filter(user=self.user).count() + 1
            self.name = f"Playlist #{count}"

        if not self.slug:
            self.slug = str(uuid.uuid4())

        super().save(*args, **kwargs)
