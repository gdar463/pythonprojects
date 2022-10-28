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

def detectOs():
    osStr = platform.system()
    if osStr == "Windows":
        osAlias = "win"
    elif osStr == "Linux":
        osAlias = 'linux'
    elif osStr == "macOS":
        osAlias = "mac"
    else:
        osAlias = "unknown"
    return osAlias

def shutdown(str):
    if str == "win":
        hostname = socket.gethostname()
        os.system("shutdown /s /m \\\\" + hostname + " /t 10 /c \"Bye\"")
    elif str == "linux" or str == "mac":
        os.system("sudo shutdown -h now \"Bye\"")

def goodbye():
    osStrs = detectOs()
    shutdown(osStrs)
    exit()
