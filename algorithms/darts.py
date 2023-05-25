import random
import math
import time

coordsmax = 30
startAngle = 0
endAngle = 0

random.seed(time.time_ns())
x,y = random.randint(-coordsmax,coordsmax),random.randint(-coordsmax,coordsmax)
distance = math.sqrt(x**2 + y**2)

if distance > coordsmax:
    mult = 0
elif distance <= coordsmax and distance >= coordsmax/100 * 90:
    mult = 2
elif distance < coordsmax/100 * 90 and distance > coordsmax/100 * 60:
    mult = 1
elif distance <= coordsmax/100 * 60 and distance >= coordsmax/100 * 50:
    mult = 3
elif distance < coordsmax/100 * 50 and distance > coordsmax/100 * 15:
    mult = 1
elif distance <= coordsmax/100 * 15 and distance > coordsmax/100 * 5:
    mult = 25
else:
    mult = 50

angle = math.degrees(math.atan2(y, x))

if angle == 0:
    angle += 360
if angle < 0:
    angle = abs(angle) + 180

for i in range(20):
    if i == 0:
        if angle <= 9 and angle + 9 > 0:
            points = 6
            break
    elif angle <= 18 * i + 9 and angle > 18 * i - 9:
        sectors = [6,13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10]
        points = sectors[i]
        break
    else:
        points = 1

print("You threw at " + str(x) + ", " + str(y))

if mult == 0:
    print("Out")
elif mult == 1:
    print("S" + str(points))  # type: ignore
elif mult == 2:
    print("D" + str(points))  # type: ignore
elif mult == 3:
    print("T" + str(points))  # type: ignore
elif mult == 25:
    print("25")
elif mult == 50:
    print("Bull")

print(points * mult)  # type: ignore