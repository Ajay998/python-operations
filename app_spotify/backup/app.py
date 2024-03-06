from flask import Flask, request, render_template, redirect,session
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import mysql.connector
from gevent.pywsgi import WSGIServer
from datetime import date


app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ajay@123",
    database="spotify"
)

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
    print(auth_url)
    return redirect(auth_url)

@app.route('/search_tracks')
def search_tracks(limit=20):
    token_info = sp_oauth.get_access_token()
    access_token = token_info['access_token']
    sp = Spotify(auth=access_token)
    search_tracks = request.args.get('search_tracks')
    print(search_tracks)
    results = sp.search(q=search_tracks, type='track', limit=limit)
    if 'tracks' in results:
        tracks = results['tracks']['items']
        if tracks:
            print(f"First {limit} results for '{search_tracks}':")
            songs = []
            for index, track in enumerate(tracks, start=1):
                song = {
                    'name': track['name'],
                    'artist': track['artists'][0]['name'],
                    'uri': track['uri'],
                    'song_source' : track['artists'][0]['external_urls']["spotify"],
                    'artists_id' : track['artists'][0]['id']
                }
                songs.append(song)
            return render_template('results.html', songs=songs)

        else:
            print(f"No results found for '{search_tracks}'")
    else:
        print(f"Error in the search results for '{search_tracks}'")

@app.route('/search_artist')
def search_artist(limit=20):
    token_info = sp_oauth.get_access_token()
    access_token = token_info['access_token']
    print(access_token)
    sp = Spotify(auth=access_token)
    search_artist = request.args.get('search_artist')
    print(search_artist)
    results = sp.search(q=f'artist:{search_artist}', type='artist', limit=limit)
    if 'artists' in results:
        if results['artists']['items']:
            artist = results['artists']['items'][0]
            top_tracks = sp.artist_top_tracks(artist['id'])
            songs = []
            for track in top_tracks['tracks'][:20]:
                song = {
                    'name': track['name'],
                    'artist': track['artists'][0]['name'],
                    'uri': track['uri'],
                    'song_source' : track['artists'][0]['external_urls']["spotify"],
                    'artists_id' : track['artists'][0]['id']
                }
                songs.append(song)
            return render_template('results.html', songs=songs)
        else:
            print(f"No results found for '{search_tracks}'")
    else:
        print(f"Error in the search results for '{search_tracks}'")


@app.route('/play/<track_uri>')
def play(track_uri):
    sp = Spotify(auth_manager=sp_oauth)
    print(track_uri)
    devices = sp.devices()
    print(devices)
    device_id = sp.devices()['devices'][0]['id']  # Get the user's active device
    print("device_id: "+str(device_id))
    track_name = request.args.get("page")
    print(track_name)
    src = request.remote_addr
    print(src)
    cursor = db.cursor()
    cursor.execute("SELECT id FROM queue WHERE track_uid = %s",(track_uri,))
    track_id = cursor.fetchone()
    if track_id:
        print("Already track present in queue list")
    else:
        cursor.execute("INSERT INTO queue (user,track_name,track_uid) VALUES (%s, %s, %s)", ("Ajay", track_name, track_uri))
    db.commit()

    return render_template('playing.html', track_playing="Playing "+str(track_name)+"..")

if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=8080)
    http_server = WSGIServer(("0.0.0.0", 8000), app)
    http_server.serve_forever()