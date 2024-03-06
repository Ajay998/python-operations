from django.urls import path
from .views import index, upload, login, playlist, create_playlist, search_songs, add_to_playlist

urlpatterns = [
    path('',index),
    path('upload/',upload,name="upload"),
    path('login/',login,name="login"),
    path('search_songs/', search_songs, name='search_songs'),
    path('add_to_playlist/<int:song_id>/', add_to_playlist, name='add_to_playlist'),
    path('playlist/<slug:playlist_slug>/', playlist, name='playlist'),
    path('create_playlist/', create_playlist, name='create_playlist'),

] 