from django.db import models

# Create your models here.


# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    instrument = models.CharField(max_length=200)
    def __str__(self):
        return self.first_name

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    released_time = models.DateTimeField()
    upload_music_file = models.FileField(upload_to ='uploads/% Y/% m/% d/',max_length=255)
    album_email = models.EmailField(max_length=254, default=None)
    song_duration = models.FloatField(default=0.00)
    image_upload = models.ImageField(upload_to='uploads/% Y/% m/% d/')
    def __str__(self):
        return self.name
