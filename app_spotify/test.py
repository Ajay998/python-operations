import requests

SPOTIPY_CLIENT_ID = 'a1e58f49c4d040099dd170c1ff7ee5a9'
SPOTIPY_CLIENT_SECRET = 'fbfb902061064bed9d031367aad6299d'
SPOTIPY_REDIRECT_URI = 'http://localhost:3000'

# Create an OAuth2 object
oauth = requests.OAuth2(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

# Get the authorization URL
auth_url = oauth.get_authorize_url()

# Redirect the user to the authorization URL
print(auth_url)

# Get the authorization code from the user
code = input('Enter the authorization code: ')

# Get the access token
token = oauth.get_access_token(code)

# Print the access token
print(token)