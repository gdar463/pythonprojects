import lib
import pyautogui
import pyperclip

lib.initCountdown(5)

clip = pyperclip.paste().strip().splitlines()
clip_idx = [i for i, item in enumerate(clip) if item == ""]
clip_idx.reverse()

for x in clip_idx:
    print(x)
    clip.pop(x)

clip.sort(key=str.lower)

for x in clip:
    pyautogui.typewrite(x + "\n")