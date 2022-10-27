import time

def initCountdown(num):
    for(x) in range(num):
        x = (num-x)
        print(x)
        time.sleep(1)
    print("GO")