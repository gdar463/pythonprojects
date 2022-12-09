import os
import pathlib
import shutil

downloads = pathlib.Path(str(pathlib.Path.home()) + "\\downloads")
extensions = pathlib.Path(str(pathlib.Path.home()) + "\\appdata\\locallow\\PythonScripts\\extensions.txt")

def ask():
        print("What extensions do you want to filter? (write stop to stop)")
        f = open(extensions, "x")
        ext = input("> ").strip().lower()
        if ext == "stop":
            f.close()
            exit()
        else:
            f.write(ext + "\n")
            ask()

if extensions.exists():
    f = open(extensions, "r")
    fileLines = f.read().splitlines()
    f.close()
else:
    print("Extensions file doesn't exist. Do you want to add any? [Y/n]")
    if input("> ").strip().lower() == "n":
        exit()
    else:
        ask()

for x in fileLines:  # type: ignore
    xGroup = list(downloads.glob("*." + x))
    for f in xGroup:
        if not pathlib.Path(str(downloads) + "\\" + x + "\\").exists():
            os.mkdir(str(downloads) + "\\" + x + "\\")
        shutil.move(str(downloads) + "\\" + str(f), str(downloads) + "\\" + x + "\\" + f)