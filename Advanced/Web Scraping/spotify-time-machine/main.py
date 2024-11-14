from bs4 import BeautifulSoup
import requests
import datetime as dt
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

date_seperated = date.split("-")
new_date = []
for number in date_seperated:
    if number.isdigit():
        new_date.append(int(number))
    else:
        raise TypeError("Invalid format")

date = dt.date(year=new_date[0], month=new_date[1], day=new_date[2])

MUSIC_URL = "https://www.billboard.com/charts/hot-100"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
response = requests.get(f"{MUSIC_URL}/{date}", headers=headers)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

song_names = [(name.getText()).strip() for name in
              soup.select(selector=".o-chart-results-list-row-container li .c-title")]

song_artist = [(artist.getText()).strip() for artist in soup.select(selector=".o-chart-results-list-row-container li "
                                                                           ".c-label") if ((artist.getText()).strip()).isdigit() == False]


def get_track_uri(song_name):
    index = song_names.index(song_name)
    results = sp.search(q=f"{song_name} {song_artist[index]}", limit=1, type='track')
    tracks = results['tracks']['items']
    if tracks:
        return tracks[0]['uri']
    else:
        print(f"Song '{song_name}' not found.")
        return None


# Set up your credentials
client_id = 'ded644e3026140bca3040a0f40e1a61d'
client_secret = '616118d8b055491aaed8de572056a8d2'
redirect_uri = 'http://localhost:8888/callback'

# Authenticate
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,
                              scope='playlist-modify-private playlist-modify-public'))

# Get the current user's ID
user_id = sp.current_user()['id']

# Create a new playlist
playlist_name = f'Top 100 - {date}'
playlist_description = 'A playlist created with Spotipy'
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)

print(f"Playlist '{playlist_name}' created successfully!")

track_uris = [get_track_uri(song) for song in song_names if get_track_uri(song)]

# Add tracks to the playlist
if track_uris:
    sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)
    print(f"Tracks added to playlist '{playlist_name}' successfully!")
else:
    print("No tracks were added to the playlist.")
