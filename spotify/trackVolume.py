from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from spotipy.oauth2 import SpotifyOAuth
import lib
import spotipy
import time

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None) # type: ignore
volume = cast(interface, POINTER(IAudioEndpointVolume))  # type: ignore

def setMasterVolume(volumePercent):
    scalarVolume = int(volumePercent) / 100
    volume.SetMasterVolumeLevelScalar(scalarVolume, None)  # type: ignore

scope = "user-read-playback-state"

f = open("secrets.txt", "r")
client = f.read().splitlines()
f.close()

track = lib.fileToDict("trackVolumes.txt")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client[0], client_secret=client[1], redirect_uri=client[2]))

while True:
    results = str(sp.current_playback(market=client[3]))
    for x in track.keys():
        if results.find(x):
            volumeTrack = int(str(track.get(x)))
            setMasterVolume(volumeTrack)
    time.sleep(10)