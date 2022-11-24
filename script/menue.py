import webbrowser
print("pierre feuille ciseaux l\u00e9o = 0")
print("pierre feuille ciseau Robin = 1")
print("morpion IA = 2")
print("morpion 1 vs 1 = 3")
jeu = int(input("\u00c0 koi keu tu veu jou\u00e9 : "))

if jeu == 0:
    jouer = 1
    exec(open(r"ProjetClipetLéo.py").read())
elif jeu == 1:
    jouer = 1
    exec(open(r"ProjetFrouinRobin.py").read())
elif jeu == 2:
    jouer = 1
    exec(open(r"Morpion_IA.py").read())
elif jeu == 3:
    jouer = 1
    exec(open(r"morpion_pvp.py").read())
elif jeu == 4:
    webbrowser.open("https://krunker.io/")
elif jeu == 5:
    webbrowser.open("https://poki.com/fr/g/ultimate-tic-tac-toe")
elif jeu == 6:
    webbrowser.open("https://chifoumi.app/fr/")
elif jeu == 2048:
    webbrowser.open("https://jeu2048.fr")
