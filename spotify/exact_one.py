import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser

client_id = 'a1e58f49c4d040099dd170c1ff7ee5a9'
client_secret = 'fbfb902061064bed9d031367aad6299d'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def play_music_by_artist(artist_name,limit=20):
    results = sp.search(q=f'artist:{artist_name}', type='artist', limit=limit)
    print(results)
    if 'artists' in results:
        if results['artists']['items']:
            artist = results['artists']['items'][0]
            top_tracks = sp.artist_top_tracks(artist['id'])
            for track in top_tracks['tracks'][:20]:
                artists_id = track['artists'][0]['id']
                print(f"{track['name']} by {track['artists'][0]['name']} Artist_id -> {artists_id}")
                song_source = track['artists'][0]['external_urls']["spotify"]
                print(song_source)
                song_uri = artist['uri']
                print(song_uri)
                sp.start_playback(uris=[song_uri])
                break


def search_tracks(query, limit=20):
    results = sp.search(q=query, type='track', limit=limit)
    print(results)
    if 'tracks' in results:
        tracks = results['tracks']['items']
        if tracks:
            print(f"First {limit} results for '{query}':")
            for index, track in enumerate(tracks, start=1):
                track_name = track['name']
                artist = track['artists'][0]['name']
                song_source = track['artists'][0]['external_urls']["spotify"]
                artists_id = track['artists'][0]['id']
                print(f"{index}. {track_name} by {artist} Artist_id -> {artists_id}")
                print(song_source)

        else:
            print(f"No results found for '{query}'")
    else:
        print(f"Error in the search results for '{query}'")

# query = "Hukum hukum"
# search_tracks(query)

artist_name = "Ar rahman"
play_music_by_artist(artist_name)