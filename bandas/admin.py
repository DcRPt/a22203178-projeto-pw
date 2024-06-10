from django.contrib import admin
from django.utils.html import format_html
from .models import Band, Album, Song

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'year_start', 'num_members', 'band_photo_html')
    list_filter = ('nationality', 'year_start')
    search_fields = ('name', 'bio')
    
    def band_photo_html(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="60" height="60"/>', obj.get_band_photo())
        return "No Image"
    band_photo_html.short_description = 'Photo'

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'band', 'release_year', 'number_of_songs', 'album_cover_html')
    list_filter = ('release_year', 'band')
    search_fields = ('title', 'band__name')
    
    def album_cover_html(self, obj):
        if obj.cover:
            return format_html('<img src="{}" width="60" height="60"/>', obj.get_album_cover())
        return "No Image"
    album_cover_html.short_description = 'Cover'

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'duration', 'spotify_link')
    list_filter = ('album__band', 'album')
    search_fields = ('title', 'lyrics', 'album__title', 'album__band__name')

admin.site.register(Band, BandAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
