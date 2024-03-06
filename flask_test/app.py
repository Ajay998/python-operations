from flask import Flask, request, render_template, redirect,session, flash, make_response
from requests_oauthlib import OAuth2Session
# from flask_oauthlib.client import OAuth

from requests.auth import HTTPBasicAuth
import mysql.connector
from urllib.parse import urlencode
import requests
from datetime import date


app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xxxxx",
    database="api_spotify"
)

SPOTIPY_CLIENT_ID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
SPOTIPY_CLIENT_SECRET = 'yyyyyyyyyyyyyyyyyyyyyyyyyy'
SPOTIPY_REDIRECT_URI = 'http://localhost:3000'

auth_url = 'https://accounts.spotify.com/api/token'
AUTHORIZATION_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
data = {
    'grant_type': 'client_credentials',
    'client_id': SPOTIPY_CLIENT_ID,
    'client_secret': SPOTIPY_CLIENT_SECRET,
}
auth_response = requests.post(auth_url, data=data)
access_token = auth_response.json().get('access_token')
print(access_token)
base_url = 'https://api.spotify.com/v1/search'

sp_oauth_2 = OAuth2Session(SPOTIPY_CLIENT_ID,  redirect_uri=SPOTIPY_REDIRECT_URI)
authorization_base_url = "https://accounts.spotify.com/authorize"
authorization_url, state = sp_oauth_2.authorization_url(authorization_base_url)
print(authorization_url)



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
    auth_params = {
        'client_id': SPOTIPY_CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': SPOTIPY_REDIRECT_URI,
    }
    auth_url_with_params = f"{AUTHORIZATION_URL}?{urlencode(auth_params)}"
    return redirect(auth_url_with_params)
@app.route('/search_tracks')
def search_tracks(limit=20):
    search_tracks = request.args.get('search_tracks')
    print(search_tracks)
    src = request.remote_addr
    print(src)
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    artist_info = requests.get('https://api.spotify.com/v1/search',
                               headers=headers,
                               params={'q': search_tracks, 'type': 'track', 'limit': limit})
    results = artist_info.json()
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


@app.route('/play/<track_uri>')
def play(track_uri):
    #############################################################3
    authorization_code = request.args.get('code')
    print(authorization_code)
    token_data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': SPOTIPY_REDIRECT_URI,
        'client_id': SPOTIPY_CLIENT_ID,
        'client_secret': SPOTIPY_CLIENT_SECRET,
    }
    response = requests.post(TOKEN_URL, data=token_data)
    token_info = response.json()

    # Get user's devices using the access token
    if 'access_token' in token_info:
        access_token = token_info['access_token']
        devices_url = 'https://api.spotify.com/v1/me/player/devices'
        headers = {'Authorization': f'Bearer {access_token}'}
        devices_response = requests.get(devices_url, headers=headers)
        devices_info = devices_response.json()
        print(devices_info)
    #################################################################3


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
