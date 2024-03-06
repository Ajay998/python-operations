from django.shortcuts import render, get_object_or_404
from .models import Music, Playlist
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
import random

def index(request):
    songs = list(Music.objects.all())
    random.shuffle(songs)

    user_playlists = Playlist.objects.filter(user=request.user)

    return render(request, 'home.html', {'song_list': songs, 'user_playlists': user_playlists})

@csrf_protect
def add_to_playlist(request, song_id):
    if request.method == 'POST':
        song = get_object_or_404(Music, pk=song_id)
        user_playlist = Playlist.objects.filter(user=request.user).first()

        if user_playlist:
            user_playlist.songs.add(song)
            return JsonResponse({'success': True})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def search_songs(request):
    query = request.GET.get('query', '')
    matching_songs = []

    if query:
        songs = Music.objects.filter(name__icontains=query)
        matching_songs = [
            {"id": song.id, "name": song.name, "artist": song.artist.name} 
            for song in songs
        ]

    return JsonResponse({'matching_songs': matching_songs})

def upload(request):
    return render(request, 'upload.html')

def playlist(request, playlist_slug):
    playlist = get_object_or_404(Playlist, slug=playlist_slug)
    song_list = playlist.songs.all()

    return render(request, 'playlist.html', {'playlist': playlist, 'song_list': song_list})

def login(request):
    return render(request, 'login.html')

@login_required
def create_playlist(request):
    if request.method == 'POST':
        new_playlist = Playlist.objects.create(user=request.user)

        return JsonResponse({'success': True, 'playlist_slug': new_playlist.slug})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'})
