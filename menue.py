import webbrowser

print("pierre feuille ciseau robin = 1")
print("morpion IA = 2")
print("morpio 1 vs 1 = 3")
jeu = int(input("a koi keu tu veu joué : "))

if jeu == 1:
    exec(open(r"C:/Users/rfrouin\Documents/python sem 1/Projet python/ProjetFrouinRobin.py").read())
elif jeu == 2:
    exec(open(r"C:/Users/rfrouin/Documents/try/test.py").read())
elif jeu == 3:
    exec(open(r"C:/Users/rfrouin/Documents/try/morpion_pvp.py").read())
elif jeu == 4:
    webbrowser.open("https://krunker.io/")
elif jeu == 5:
    webbrowser.open("https://poki.com/fr/g/ultimate-tic-tac-toe")
elif jeu == 6:
    webbrowser.open("https://chifoumi.app/fr/")
