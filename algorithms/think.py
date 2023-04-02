import logging
import random
import os
import time

def invertList(list):
    log.info("A: " + str(actions) + " O: " + str(operands))
    temp = []
    for i in range(len(list)):
        log.info("I: " + str(i) + " T: " + str(temp) + " SI: " + str(len(list) - 1 - i) + " S: " + list[len(list) - 1 - i])
        temp.append(list[len(list) - 1 - i])
    return temp

if os.path.isfile("debug.txt"):
    f = open("debug.txt")
    if f.read() == "DEBUGON":
        logging.basicConfig(level=10, format="%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")
    else: 
        logging.basicConfig(level=30, format="%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")
    f.close()

operations = ["add", "sub", "mul"]
actions = []
operands = []

log = logging.getLogger("Thinker")

os.system("cls")
print("Pensa ad un numero")
time.sleep(2)

for i in range(random.randint(3,7)):
    selected = random.choice(operations)
    if selected == "add":
        actions.append(selected)
        operands.append(random.randint(1,25))
        print("Aggiungi al numero " + str(operands[-1]))
        input("Premi invio quando hai finito")
    elif selected == "sub":
        actions.append(selected)
        operands.append(random.randint(1,10))
        print("Sottrai al numero " + str(operands[-1]))
        input("Premi invio quando hai finito")
    elif selected == "mul":
        actions.append(selected)
        operands.append(random.randint(2,5))
        print("Moltiplica il numero per " + str(operands[-1]))
        input("Premi invio quando hai finito")
    log.debug("A: " + str(actions[-1]) + " O: " + str(operands[-1]))

actions = invertList(actions)

print("Dimmi il numero finale e proverò a indovinarlo")
num = int(input("Il numero finale è: "))

for x in actions:
    if x == "add":
        num = num - operands[-1]
    elif x == "sub":
        num = num + operands[-1]
    elif x == "mul":
        num = num / operands[-1]
    log.debug("a: " + str(actions[0]) + " O: " + str(operands[-1]) + " N: " + str(num))
    operands.pop(-1)

print("Il numero che hai pensato è: " + str(num))