import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'a1e58f49c4d040099dd170c1ff7ee5a9'
client_secret = 'fbfb902061064bed9d031367aad6299d'


client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def play_music_by_artist(artist_name):

    results = sp.search(q=f'artist:{artist_name}', type='artist')

    if len(results['artists']['items']) > 0:
        artist = results['artists']['items'][0]
        artist_id = artist['id']

        top_tracks = sp.artist_top_tracks(artist_id)

        if top_tracks:
            print(f"Top Tracks by {artist_name}:")
            for track in top_tracks['tracks']:
                print(f"{track['name']} by {artist_name}")
        else:
            print(f"No top tracks found for {artist_name}")
    else:
        print(f"No results found for the artist: {artist_name}")

artist_name = "Artist Name"

play_music_by_artist(artist_name)

