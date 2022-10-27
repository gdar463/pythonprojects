import random
import webbrowser
import os

games = {"slimerancher":"steam://rungameid/433340","bloons":"steam://rungameid/960090","tmnf":"\"C:\\Users\\Dario\\Documents\\Giochi\\TM Natitions\\Backup\\TMInfinity.exe\"","pheonix":"steam://rungameid/787480","cities":"steam://rungameid/255710","prism":"\"C:\\Users\\Dario\\Documents\\Giochi\\Minecraft\\PrismLauncher\\prismlauncher.exe\"","factorio":"steam://rungameid/427520","autocad":"\"C:\\Program Files\\Autodesk\\AutoCAD 2023\\acad.exe\"  /product ACAD /language \"it-IT\"","vscode":"\"C:\\Users\\Dario\\AppData\\Local\\Programs\\Microsoft VS Code Insiders\\Code - Insiders.exe\""}

selectedNum = random.randint(0,len(games)-1)
selectedElement = list(games.values())[selectedNum]

if selectedElement.startswith("steam") == True:
    webbrowser.open(selectedElement)
elif selectedElement.startswith("\"C:") == True:
    os.system(selectedElement)