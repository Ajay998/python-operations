from flask import Flask, request, render_template, redirect,session, flash
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import mysql.connector

from datetime import date


app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ajay@123",
    database="api_spotify"
)

SPOTIPY_CLIENT_ID = 'a1e58f49c4d040099dd170c1ff7ee5a9'
SPOTIPY_CLIENT_SECRET = 'fbfb902061064bed9d031367aad6299d'
SPOTIPY_REDIRECT_URI = 'http://localhost:3000'

sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
token_info = sp_oauth.get_access_token()
access_token = token_info['access_token']
print(access_token)
sp = Spotify(auth=access_token)
@app.route('/')
def index():
    cursor = db.cursor()
    src = request.remote_addr
    print(src)
    today = date.today()
    print("Today date is: ", today)
    cursor.execute("SELECT id FROM limit_queue_tracks WHERE local_ip = %s", (src,))
    get_user = cursor.fetchone()
    print(get_user)
    if get_user:
        print("Got user")
        cursor.execute("SELECT count,date FROM limit_queue_tracks WHERE local_ip = %s", (src,))
        check_user_date = cursor.fetchone()
        if check_user_date:
            user_date = check_user_date[1]
            print(user_date)
            count = check_user_date[0]
            if str(user_date) == str(today):
                print("No need to change the count")
            else:
                count = 0
                print("Different date")
                cursor.execute("UPDATE limit_queue_tracks SET date=%s, count=%s WHERE local_ip=%s",(str(today),count,str(src)))
                db.commit()
                cursor.close()
                return render_template('index.html',limit=count,user_src=src)
            return render_template('index.html', limit=count, user_src=src)
        else:
            print("No local ip for searching local ip")
            return render_template('index.html', limit=0, user_src=src)
    else:
        count = 0
        cursor.execute("INSERT INTO limit_queue_tracks (local_ip, name ,count ,date) VALUES (%s, %s, %s, %s)", (src, "Ajay", count, today))
        db.commit()
        cursor.close()
        print("No user in search_limit table")
        return render_template('index.html', limit=count, user_src=src)
@app.route('/login')
def login():
    auth_url = sp_oauth.get_authorize_url()
    print(auth_url)
    return redirect(auth_url)

@app.route('/search_tracks')
def search_tracks(limit=20):
    search_tracks = request.args.get('search_tracks')
    print(search_tracks)
    src = request.remote_addr
    print(src)
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
            return render_template('results.html', songs=songs, user_src=src)

        else:
            print(f"No results found for '{search_tracks}'")
    else:
        print(f"Error in the search results for '{search_tracks}'")

@app.route('/search_artist')
def search_artist(limit=20):
    sp = Spotify(auth=access_token)
    search_artist = request.args.get('search_artist')
    print(search_artist)
    src = request.remote_addr
    print(src)
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
            return render_template('results.html', songs=songs, user_src=src)
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
    cursor.execute("SELECT count FROM limit_queue_tracks WHERE local_ip=%s",(str(src),))
    get_limit_data = cursor.fetchone()
    if get_limit_data:
        count = get_limit_data[0]
        if count<5:
            count = count + 1
            cursor.execute("UPDATE limit_queue_tracks SET count=%s WHERE local_ip=%s", (count, str(src)))
            db.commit()
            cursor.execute("SELECT id FROM queue WHERE track_uid = %s",(track_uri,))
            track_id = cursor.fetchone()
            if track_id:
                print("Already track present in queue list")
            else:
                cursor.execute("INSERT INTO queue (user,track_name,track_uid) VALUES (%s, %s, %s)", ("Ajay", track_name, track_uri))
                db.commit()
                cursor.close()
            sp.start_playback(device_id=device_id, uris=[track_uri])
            return render_template('playing.html', track_playing="Playing "+str(track_name)+"..")
        else:
            # flash('Looks like you have changed your name!')
            return render_template('results.html', limit=count, user_src=src)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
