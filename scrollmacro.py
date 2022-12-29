import lib
import pyautogui
import random
import time

lib.initCountdown(5)

while True:
    pyautogui.scroll(random.randint(4,1))
    time.sleep(0.01)