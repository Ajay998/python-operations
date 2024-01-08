import json
import spotipy
import webbrowser


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

# To print the response in readable format.
print(json.dumps(user_name, sort_keys=True, indent=4))



while True:
    print("Welcome to the project, " + user_name['display_name'])
    print("0 - Exit the console")
    print("1 - Search for a Song")
    user_input = int(input("Enter Your Choice: "))
    if user_input == 1:
        search_song = input("Enter the song name: ")
        results = spotifyObject.search(search_song, 1, 0, "track")
        print(results)
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        print(song)
        webbrowser.open(song)
        print('Song has opened in your browser.')
    elif user_input == 0:
        print("Good Bye, Have a great day!")
        break
    else:
        print("Please enter valid user-input.")