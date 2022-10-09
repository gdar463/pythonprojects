# Inserisci le informazioni qui
# NBi = Non Bionda
# NGo = Non Gonna
# NOc = Non Ccchiali
# Bi = Bionda
# Go = Gonna
# Oc = Occhiali

A = ["NBi","NGo","Oc"]
B = ["Bi","NGo","NOc"]
C = ["Bi","NGo","NOc"]
D = ["NBi","Go","NOc"]
E = ["Bi","NGo","Oc"]
F = ["Bi","Go","NOc"]
G = ["Bi","Go","Oc"]
H = ["Bi","Go","Oc"]

##########################################################

import os

##########################################################

def AskConfirmation():
    listconfirm = input(str(all)
                    .replace("],","],\n")
                    .replace("["," ")
                    .replace("]"," ")
                    .replace("{"," Risultano giuste le informazioni? [y/N] \n ")
                    .replace("}"," \n ")
                    .replace("'NBi'","non è bionda")
                    .replace("'Bi'","    è bionda")
                    .replace("'NGo'","non ha la gonna")
                    .replace("'Go'","    ha la gonna")
                    .replace(", 'NOc' ,"," e non ha gli occhiali")
                    .replace(", 'Oc' ,"," e     ha gli occhiali")
                    .replace(", 'Oc'"," e     ha gli occhiali"))
    if listconfirm.lower().strip() == "n":
        print(" Chiusura...")
        exit()
    elif listconfirm.lower().strip() == "":
        print(" Chiusura...")
        exit()
    elif listconfirm.lower().strip() == "y":
        pass
    else:
        os.system("cls")
        print(" Riprova\n")
        AskConfirmation()

##########################################################

all = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E,
    "F": F,
    "G": G,
    "H": H
}

##########################################################

os.system("cls")
AskConfirmation()
