from re import search
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# Get songs from billboard*******************************
d,m,y = input("enter date(dd mm yyyy) if num is single then type with 0:").split()
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{y}-{m}-{d}/")
web_data = response.text

soup = BeautifulSoup(response.text, 'html.parser')
track_titles = soup.select("div.o-chart-results-list-row-container > ul:nth-child(1) > li:nth-child(4) > ul:nth-child(1) > li:nth-child(1) > h3:nth-child(1)")
song_names = [track.getText().strip() for track in track_titles]

track_artists = soup.select("div.o-chart-results-list-row-container > ul:nth-child(1) > li:nth-child(4) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(2)")
top_100_artists = [artist.getText().strip() for artist in track_artists]

#********************************************************************************************************************


# *****************************************************spotify authentication*****************************************

spotify_client_id = "64a1495f2f824e489dbffbd13e85e8c9"
spotify_secret_client = "64ffba1f3651430e8d7f333b2abddb44"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://open.spotify.com/",
        client_id=spotify_client_id,
        client_secret=spotify_secret_client,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# *******************spotify song search**********************************

song_urls = []

for song in song_names:
    result = sp.search(q=f"track:{song} year:{y}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_urls.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# print(song_uris)

#******************************* create playlist ***************
playlist = sp.user_playlist_create(user=user_id, name=f"{d}-{m}-{y}", public=False, collaborative=False, description=f"{d}-{m}-{y} songs")
print(playlist["id"])


#******************* add songs to playlist**************************

songs = sp.playlist_add_items(playlist_id=playlist["id"], items=song_urls)


