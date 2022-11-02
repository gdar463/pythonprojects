import lib
import os
import pyautogui
import random
import time

lib.initCountdown(5)

processes = ("Code - Insiders", "acad", "javaw")

while lib.checkIfProcRunning("PWAAT"):
    if random.randint(1,50) == 33:
        pyautogui.press("f12")
        print("\nScreenshot!\n")
    else:
        print("Nope")
    time.sleep(0.5)

for (x) in processes:
    while lib.checkIfProcRunning(x):
        if random.randint(1,70) == 44:
            with pyautogui.hold("ctrl"):
                pyautogui.press("0")
                print("\nScreenshot!\n")
        else:
            print("Nope")
        time.sleep(1)

print("No process found!")
os.system("pause")