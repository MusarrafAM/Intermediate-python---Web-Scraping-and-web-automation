from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you waant to travel to ? Type the date in this formate YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL).text


soup = BeautifulSoup(response, "html.parser")
songs_tag = soup.select("h3.c-title.lrv-u-font-size-16")
top_100_song_list = []
for song in songs_tag:
    top_100_song_list.append(song.text.strip())

# top_100_song_list = [song.text.strip() for song in songs_tag]  # using list comprehension

print(top_100_song_list)


# -------------------------------------------------------- spotify for developers ------------------------------
client_id = "6199f920c17f4477894d2007a3695eec"
client_secret = "61c274e0b8474110bd83ac7446dc137c"

# If you can't understand the below code no problem.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", redirect_uri="http://example.com",
                                               client_id=client_id,client_secret=client_secret, show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]
print(user_id)


song_names = top_100_song_list

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create the playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
