import requests
from bs4 import BeautifulSoup

spotify_client_id = "64a1495f2f824e489dbffbd13e85e8c9"
spotify_secret_client = "64ffba1f3651430e8d7f333b2abddb44"

d,m,y = input("enter date(dd mm yyyy) if num is single then type with 0:").split()
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{y}-{m}-{d}/")
web_data = response.text

soup = BeautifulSoup(response.text, 'html.parser')
track_titles = soup.select("div.o-chart-results-list-row-container > ul:nth-child(1) > li:nth-child(4) > ul:nth-child(1) > li:nth-child(1) > h3:nth-child(1)")
top_100_tracks = [track.getText().strip() for track in track_titles]

track_artists = soup.select("div.o-chart-results-list-row-container > ul:nth-child(1) > li:nth-child(4) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(2)")
top_100_artists = [artist.getText().strip() for artist in track_artists]

print(top_100_tracks)

with open("songs.txt", "w") as file:
    for song in top_100_artists:
        file.write(f"{song}\n")