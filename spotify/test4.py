import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser

client_id = 'a1e58f49c4d040099dd170c1ff7ee5a9'
client_secret = 'fbfb902061064bed9d031367aad6299d'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def play_music_by_artist(artist_name,limit=20):
    results = sp.search(q=f'artist:{artist_name}', type='artist', limit=limit)
    # print(results)
    if 'artists' in results:
        artists_data = results['artists']['items']
        print(artists_data)
        if artists_data:
            print(f"First {limit} results for '{query}':")
            for index, q_artists in enumerate(artists_data, start=1):
                q_track_name = q_artists["name"]
                q_artists_id = q_artists['id']
                print(q_artists_id)
                albumResults = sp.artist_albums(q_artists_id, limit=50)
                albumResults = albumResults['items']
                # print(albumResults)
                for album in albumResults:
                    albumID = album['id']
                    album_name = album['name']
                    print("ALBUM: " + album['name'])
                    trackResults = sp.album_tracks(albumID)
                    trackResults = trackResults['items']
                    if trackResults:
                        for index, track in enumerate(trackResults, start=1):
                            track_name = track['name']
                            artist = track['artists'][0]['name']
                            song_source = track['artists'][0]['external_urls']["spotify"]
                            artists_id = track['artists'][0]['id']
                            print(f"{index}. {track_name} by {artist} Artist_id -> {artists_id}")
                            print(song_source)






    # items = results['artists']['items']
    # if len(items) > 0:
    #     artist = items[0]
    #     artist_id = artist['id']

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

query = "Hukum hukum"
# search_tracks(query)

artist_name = "Ar rahman"
play_music_by_artist(artist_name)