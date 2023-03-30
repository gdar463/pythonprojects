import random
import os
import logging
import time
import bcrypt

operations = ["add", "sub", "mul"]
actions = []
operands = []

def invertList(list):
    temp = []
    for i in range(len(list)):
        temp.append(list[len(list) - i - 1])
    return temp

if os.path.isfile("debug.txt"):
    f = open("debug.txt")
    if f.read() == "DEBUGON":
        key = str.encode(input("Debug Key: "))
        if bcrypt.checkpw(key, b"$2b$12$PTxifHu.LPpGs1pm20KAC.kP74.t/U2NpnNoA4ZDXA1uJ7ceVTMqu"):
            logging.basicConfig(level=print("LOGLEVEL", "INFO"))
    f.close()

log = logging.getLogger(" Thinker")
log.setLevel(10)

os.system("cls")
print("Pensa ad un numero")
time.sleep(2)

for i in range(random.randint(3,7)):
    selected = operations[random.randint(0,2)]
    if selected == "add":
        actions.append("add")
        operands.append(random.randint(1,20))
        print("Adesso aggiungi " + str(operands[-1]) + " al numero")
        input("Premi invio quando hai fatto")
        log.debug(" A: " + str(actions[-1]) + " O: " + str(operands[-1]))
    elif selected == "sub":
        actions.append("sub")
        operands.append(random.randint(1,6))
        print("Adesso sottrai " + str(operands[-1]) + " al numero")
        input("Premi invio quando hai fatto")
        log.debug(" A: " + str(actions[-1]) + " O: " + str(operands[-1]))
    else:
        actions.append("mul")
        operands.append(random.randint(2,5))
        print("Adesso moltiplica il numero per " + str(operands[-1]))
        input("Premi invio quando hai fatto")
        log.debug(" A: " + str(actions[-1]) + " O: " + str(operands[-1]))

print("Adesso dimmi il numero finale e cercherò di indovinarlo")
num = int(input("Il numero finale è: "))

actions = invertList(actions)

for x in actions:
    if x == "add":
        num = num - operands[-1]
        log.debug(" A: " + str(x) + " O: " + str(operands[-1]) + " N: " + str(num))
    elif x == "sub":
        num = num + operands[-1]
        log.debug(" A: " + str(x) + " O: " + str(operands[-1]) + " N: " + str(num))
    else:
        num = num / operands[-1]
        log.debug(" A: " + str(x) + " O: " + str(operands[-1]) + " N: " + str(num))
    operands.pop(-1)

print("Il numero che hai pensato è " + str(num))