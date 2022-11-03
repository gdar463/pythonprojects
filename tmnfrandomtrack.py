import os
import pyautogui
import pyperclip
import re
import time
import webbrowser

trackNum = input("How many tracks do you want?")

tracks = []

for x in range(int(trackNum)):
    webbrowser.open("https://tmnf.exchange/trackrandom", 0, True)
    time.sleep(3)
    pyautogui.click(400,60)
    with pyautogui.hold("ctrl"):
        pyautogui.press(["a","c"])
    tracks.append(pyperclip.paste())
    with pyautogui.hold("ctrl"):
        pyautogui.press("w")
    time.sleep(0.5)

track0 = re.sub("/D", "", tracks[0][-7:])
webbrowser.open("https://tmnf.exchange/trackplay/" + track0, 1, False)
tracks.pop(0)

for x in tracks:
    x = re.sub("/D", "", x[-7:])
    webbrowser.open("https://tmnf.exchange/trackplay/" + x, 0, False)
    os.system("pause")