from flask import Flask, request, render_template, redirect
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

app = Flask(__name__)

SPOTIPY_CLIENT_ID = 'a1e58f49c4d040099dd170c1ff7ee5a9'
SPOTIPY_CLIENT_SECRET = 'fbfb902061064bed9d031367aad6299d'
SPOTIPY_REDIRECT_URI = 'http://localhost:3000'  # Set this in your Spotify Developer Dashboard

sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope='user-read-private playlist-read-private playlist-modify-public user-top-read')

@app.route('/')
def index():
    if not sp_oauth.is_token_valid():
        return render_template('login.html')
    else:
        return render_template('search.html')

@app.route('/login')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    token_info = sp_oauth.get_access_token(request.args['code'])
    if token_info:
        return redirect('/')
    else:
        return "Authentication failed."

@app.route('/search', methods=['POST'])
def search():
    if not sp_oauth.is_token_valid():
        return "Token not valid. Please log in again."

    query = request.form.get('query')
    sp = Spotify(auth_manager=sp_oauth)
    results = sp.search(q=query, type='track', limit=10)

    return render_template('search_results.html', tracks=results['tracks']['items'])

@app.route('/play/<track_uri>')
def play(track_uri):
    if not sp_oauth.is_token_valid():
        return "Token not valid. Please log in again."

    sp = Spotify(auth_manager=sp_oauth)
    device_id = sp.devices()['devices'][0]['id']  # Get the user's active device
    print(device_id)
    # sp.start_playback(device_id=device_id, uris=[track_uri])

if __name__ == '__main__':
    app.run()