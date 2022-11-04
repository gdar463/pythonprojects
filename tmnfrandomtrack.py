import os
import pyautogui
import pyperclip
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

if os.path.isfile("tracks.txt"):
    os.remove("tracks.txt")

f = open("tracks.txt","w")
for x in range(len(tracks)):
    f.write(tracks[x] + "\n")
f.close()

with open("tracks.txt", "r") as f:
    lines = f.readlines()

with open("tracks.txt", "w") as f:
    for x in tracks:
        webbrowser.open("https://tmnf.exchange/trackplay/" + "".join(filter(str.isdigit, x[-7:])), 0, False)
        for line in lines:
            if line.strip("\n") != x:
                f.write(line)
        pause = input("\nThis is track number: " + x + "\nNext Track... ([N]o/[E]nter)\n")
        if pause.lower() == "n":
            break
