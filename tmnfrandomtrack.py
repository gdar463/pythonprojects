import os
import pyautogui
import pyperclip
import re
import time
import webbrowser

trackNum = input("How many tracks do you want?\n")

tracks = []

webbrowser.open("google.com")
time.sleep(5)

for x in range(int(trackNum)):
    webbrowser.open("https://tmnf.exchange/trackrandom", 0, True)
    time.sleep(5)
    pyautogui.click(400,60)
    with pyautogui.hold("ctrl"):
        pyautogui.press(["a","c"])
    tracks.append(pyperclip.paste())
    with pyautogui.hold("ctrl"):
        pyautogui.press("w")
    time.sleep(0.5)

webbrowser.open("https://tmnf.exchange/trackplay/" + "".join(filter(str.isdigit, tracks[0])), 0, False)
tracks.pop(0)
os.system("pause")

for x in tracks:
    webbrowser.open("https://tmnf.exchange/trackplay/" + "".join(filter(str.isdigit, x)), 0, False)
    os.system("pause")