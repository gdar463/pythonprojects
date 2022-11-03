import lib
import os
import pyautogui
import pyperclip
import pywinauto
import time
import webbrowser

lib.initCountdown(5)

trackNum = input("How many tracks do you want?")

tracks = []

for x in range(int(trackNum)):
    webbrowser.open("https://tmnf.exchange/trackrandom", 0, True)
    time.sleep(0.25)
    pyautogui.click(400,60)
    with pyautogui.hold("ctrl"):
        pyautogui.press(["a","c"])
    tracks.append(pyperclip.paste())
    with pyautogui.hold("ctrl"):
        pyautogui.press("w")
    time.sleep(0.25)

for x in tracks:
    webbrowser.open(x)
    os.system("pause")