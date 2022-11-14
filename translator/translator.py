import lib
import os

lib.initCountdown(5)

if os.path.isfile("translatorList.txt") == False:
    f = open("translatorList.txt", "x")
    f.close()
    created = True
    raise Exception("File was just created, please fill it in")

transDict = lib.fileToDict("translatorList.txt")

def ask():
    askedWord = input("What word do you want translated?\n> ").lower()

    if askedWord in transDict.keys():
        print("Translated is:\n" + transDict[askedWord])
    else:
        contin = input("The asked word isn't present in the file. Do you want to [A]dd it or [T]ry another word?\n> ").lower()
        if contin == "a":
            newWord = input("What's the translation?\n> ")
            f = open("translatorList.txt", "a")
            f.write(askedWord + "=" + newWord)
            f.close()
        else:
            ask()

ask()