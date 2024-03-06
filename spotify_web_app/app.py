from flask import Flask, render_template, request, redirect
import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

SPOTIPY_CLIENT_ID = 'a1e58f49c4d040099dd170c1ff7ee5a9'
SPOTIPY_CLIENT_SECRET = 'fbfb902061064bed9d031367aad6299d'
SPOTIPY_REDIRECT_URI = 'http://localhost:3000'

sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    auth_url = sp_oauth.get_authorize_url()
    print("Auth_url: "+str(auth_url))
    return redirect(auth_url)

@app.route('/callback')
def callback():
    token_info = sp_oauth.get_access_token()
    access_token = token_info['access_token']
    sp = Spotify(auth=access_token)
    search_query = request.args.get('search_query')
    search_results = sp.search(q=search_query, type='track')
    print(search_results)
    songs = []
    for track in search_results['tracks']['items']:
        song = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'uri': track['uri']
        }
        songs.append(song)

    return render_template('results.html', songs=songs)


if __name__ == '__main__':
    app.run(debug=True)