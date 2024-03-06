import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="a1e58f49c4d040099dd170c1ff7ee5a9",
                                               client_secret="fbfb902061064bed9d031367aad6299d",
                                               redirect_uri="http://localhost:3000",
                                               scope="user-read-currently-playing"))

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
                song_uri = track['artists'][0]['uri']
                print(song_uri)
                sp.start_playback(uris=[song_uri])
                break
        else:
            print(f"No results found for '{query}'")
    else:
        print(f"Error in the search results for '{query}'")

query = "Hukum hukum"
search_tracks(query)