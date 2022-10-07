A = ["NBi","NGo","Oc"]
B = ["Bi","NGo","NOc"]
C = ["Bi","NGo","NOc"]
D = ["NBi","Go","NOc"]
E = ["Bi","NGo","Oc"]
F = ["Bi","Go","NOc"]
G = ["Bi","Go","Oc"]
H = ["Bi","Go","Oc"]
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

if listconfirm.lower() == "n":
    print("Chiusura...")
    exit()
elif listconfirm.lower() == "":
    print("Chiusura...")
    exit()
elif listconfirm.lower() == "y":
    print("La lista è confermata")
    
