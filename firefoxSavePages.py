import lib
import os
import pyautogui
import pyperclip
import pywinauto
import time
import webbrowser

lib.initCountdown(5)

if os.path.isfile("./links/links.txt") == True:
    continu = input("There's already a link list. Do you want to use it? [Y/n]")
    if continu.lower().strip() == "n":
        pass
    else:
        f = open("./links/links.txt", "r")
        fileLinks = f.read().splitlines()
        webbrowser.open(fileLinks[0])
        time.sleep(4)
        fileLinks.pop(0)
        for x in fileLinks:
            webbrowser.open(x)
        f.close
        time.sleep(1)
        os.remove("./links/links.txt")
        exit()

windows = pywinauto.Desktop(backend="uia").windows()
titles = ([w.window_text() for w in windows])
title_idx = [i for i, item in enumerate(titles) if item.endswith('Mozilla Firefox')]
title = titles[title_idx[0]].replace("[","").split("]")[0]

links = []

app = pywinauto.Application(backend="uia").connect(class_name="MozillaWindowClass")
app.top_window().set_focus()

with pyautogui.hold("ctrl"):
    pyautogui.press("1")

time.sleep(0.25)

for x in range(int(title)):
    pyautogui.click(400,60)
    with pyautogui.hold("ctrl"):
        pyautogui.press(["a","c"])
    links.append(pyperclip.paste())
    with pyautogui.hold("ctrl"):
        pyautogui.press("w")
    time.sleep(0.25)

f = open("./links/links.txt", "w")
for x in range(len(links)):
    f.write(links[x] + "\n")
f.close