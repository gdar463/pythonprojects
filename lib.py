import time
import platform
import socket
import os

def initCountdown(num):
    for(x) in range(num):
        x = (num-x)
        print(x)
        time.sleep(1)
    print("GO")

def detectOs(string):
    osStr = platform.system()
    if osStr == "Windows":
        string = "win"
    elif osStr == "Linux":
        string = "linux"
    elif osStr == "macOS":
        string = "mac"
    else:
        osStr = "unknown"
    return osStr

def shutdown(osStr):
    if osStr == "win":
        hostname = socket.gethostname()
        os.system("shutdown /s /m \\\\" + hostname + " /t 7 /c \"Bye\"")
    elif osStr == "linux":
        os.system("sudo shutdown -h now \"Bye\"")
    elif osStr == "mac":
        print("Please shutdown your system by yourself")