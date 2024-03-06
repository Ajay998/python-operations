import json
import spotipy
import webbrowser
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

username = '31pkxz7yohaftlgxvbbx5jtsdeea'
clientID = 'a1e58f49c4d040099dd170c1ff7ee5a9'
clientSecret = 'fbfb902061064bed9d031367aad6299d'
redirect_uri = 'http://localhost:3000'

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
print(token)
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()

print(json.dumps(user_name, sort_keys=True, indent=4))

track_name = "Hukum hukum"

results = spotifyObject.search(q=track_name, type='track')

print(results)

if len(results['tracks']['items']) > 0:
    songs_dict = results['tracks']
    song_items = songs_dict['items']
    for songs_data in song_items:
        song_url = songs_data['external_urls']['spotify']
        print(song_url)
else:
    print("No results found for the specified track name.")