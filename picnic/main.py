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

Ar = "Go"
Br = "Bi"
Cr = "Oc"
Dr = "Go"
Er = "NGo"
Fr = "Bi"
Gr = "Go"
Hr = "Oc"

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

def AskQuestions():
    listquestions = input(str(allQuestions)
                    .replace("{","\n Risultano giuste le informazioni della sorella? [y/N] \n ")
                    .replace("',","\n")
                    .replace("'}","\n ")
                    .replace("}"," \n ")
                    .replace("'Bi","     è bionda")
                    .replace("'NGo"," non ha la gonna")
                    .replace("'Go","     ha la gonna")
                    .replace("'Oc","     ha gli occhiali")
    )
    if listquestions.lower().strip() == "n":
        print(" Chiusura...")
        exit()
    elif listquestions.lower().strip() == "":
        print(" Chiusura...")
        exit()
    elif listquestions.lower().strip() == "y":
        pass
    else:
        os.system("cls")
        print(" Riprova\n")
        AskConfirmation()

##########################################################

allQuestions = {
    "A": Ar,
    "B": Br,
    "C": Cr,
    "D": Dr,
    "E": Er,
    "F": Fr,
    "G": Gr,
    "H": Hr
}

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
AskQuestions()