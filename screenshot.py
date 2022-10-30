import time
import random
import pyautogui
import lib
import os

lib.initCountdown(5)

while lib.checkIfProcRunning("PWAAT"):
    if lib.checkIfProcRunning("PWAAT") == False:
        time.sleep(1)
        continue
    if random.randint(1,100) == 33:
        pyautogui.press("f12")
    time.sleep(1)

print("No process found!")
os.system("pause")