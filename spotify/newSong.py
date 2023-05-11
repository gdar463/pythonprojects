from spotipy.oauth2 import SpotifyOAuth
import spotipy
import json
import win11toast
import time

scope = "user-read-playback-state"

f = open("secrets.txt", "r")
client = f.read().splitlines()
f.close()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client[0], client_secret=client[1], redirect_uri=client[2]))
while True:
    results = str(sp.current_playback(market=client[3]))

    results = results.replace("'", '"')
    results = results.replace("False", "false")
    results = results.replace("True", "true")
    results = json.loads(results)

    name = results["item"]["name"]
    artist = ""
    prev = ""
    if prev != name:
        for x in range(len(results["item"]["artists"])):
            artist = artist + ", " + results["item"]["artists"][x]["name"]
        print(name, artist, prev)
        win11toast.toast(name, artist[2:])
        prev = name
    time.sleep(10)