from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, default='Português')
    year_start = models.IntegerField(default=2024)
    num_members = models.IntegerField(default=1)
    photo = models.ImageField(upload_to='band_photos', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_band_photo(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return '/media/bandas/defaultImage.jpg'

class Album(models.Model):
    title = models.CharField(max_length=50)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='album_covers/', null=True, blank=True)
    number_of_songs = models.IntegerField(default=1)
    release_year = models.IntegerField(default=2024)

    def __str__(self):
        return self.title

    def get_album_cover(self):
        if self.cover and hasattr(self.cover, 'url'):
            return self.cover.url
        else:
            return '/media/bandas/defaultImage.jpg'

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    lyrics = models.TextField(default='', null=True, blank=True)
    spotify_link = models.URLField(null=True, blank=True, default='')
    duration = models.CharField(max_length=10, default='0:00')
    biography = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.title