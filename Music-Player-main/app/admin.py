from django.contrib import admin
from .models import Artist, Music,Playlist
from django import forms

class PlaylistAdminForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = '__all__'
        widgets = {
            'songs': forms.CheckboxSelectMultiple,  # You can customize the widget here
        }

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    form = PlaylistAdminForm
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'description')
