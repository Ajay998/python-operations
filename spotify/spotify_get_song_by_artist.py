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

artist_name = "Yuvan shankar raja"
