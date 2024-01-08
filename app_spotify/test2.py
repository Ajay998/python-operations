import requests
import base64
import json
from urllib.parse import urlencode
SPOTIPY_CLIENT_ID = 'a1e58f49c4d040099dd170c1ff7ee5a9'
SPOTIPY_CLIENT_SECRET = 'fbfb902061064bed9d031367aad6299d'
SPOTIPY_REDIRECT_URI = 'http://localhost:3000'
AUTHORIZATION_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_URI = 'https://api.spotify.com/v1/me/player/recently-played'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
auth_string = SPOTIPY_CLIENT_ID + ":" + SPOTIPY_CLIENT_SECRET
auth_bytes = auth_string.encode("utf-8")
auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")
# headers = {
#     "Authorization" : "Basic "+auth_base64,
#     "Content-Type" : "application/x-www-form-urlencoded"
# }
SCOPE = 'user-read-playback-state user-modify-playback-state'
auth_params = {
    'client_id': SPOTIPY_CLIENT_ID,
    'response_type': 'code',
    'redirect_uri': SPOTIPY_REDIRECT_URI,
    'scope': SCOPE,
}
auth_url_with_params = f"{AUTHORIZATION_URL}?{urlencode(auth_params)}"
print(auth_url_with_params)
# auth_code = requests.get(AUTHORIZATION_URL, {
#     'client_id': SPOTIPY_CLIENT_ID,
#     'response_type': 'code',
#     'redirect_uri': SPOTIPY_REDIRECT_URI,
#     'scope': SCOPE,
# })
# print(auth_code)
# auth_header = base64.urlsafe_b64encode((SPOTIPY_CLIENT_ID + ':' + SPOTIPY_CLIENT_SECRET).encode())
# print(auth_header)
#
# BASE64_ENCODED_HEADER_STRING = base64.b64encode(bytes(f"{SPOTIPY_CLIENT_ID}:{SPOTIPY_CLIENT_SECRET}", "ISO-8859-1")).decode("ascii")
# q_headers = {}
# data = {}
#
# q_headers['Authorization'] = f"Basic {BASE64_ENCODED_HEADER_STRING}"
#
# data['grant_type'] = "client_credentials"
# data['json'] = True
# data['scope'] = 'user-read-recently-played'
# r = requests.post(url=TOKEN_URL, headers=headers, data=data)
#
# # prints the response from the server regarding the access token data (formatted to be easier to read)
# print(json.dumps(r.json(), indent=2))
#
# import requests
# from urllib.parse import urlencode
#
# # Spotify App credentials
# CLIENT_ID = SPOTIPY_CLIENT_ID
# REDIRECT_URI = SPOTIPY_REDIRECT_URI
#
# # Spotify authorization endpoint
# AUTHORIZATION_URL = 'https://accounts.spotify.com/authorize'
#
# # Step 1: Direct the user to Spotify for Authorization
# auth_params = {
#     'client_id': CLIENT_ID,
#     'response_type': 'code',
#     'redirect_uri': REDIRECT_URI,
# }
#
# auth_url = f"{AUTHORIZATION_URL}?{urlencode(auth_params)}"
# print(auth_url)

auth_url = 'https://accounts.spotify.com/api/token'
auth_data = {
    'grant_type': 'client_credentials'
}
auth_header = {
    'Authorization': 'Basic ' + base64.b64encode(f"{SPOTIPY_CLIENT_ID}:{SPOTIPY_CLIENT_SECRET}".encode()).decode()
}
response = requests.post(auth_url, data=auth_data, headers=auth_header)
print(response.json())