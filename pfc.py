import random
#Importer le module time
import time
#Définir jouer qui retourne une foction input qui demande si l'utilisateur veut jouer où oui = 1 et non =2
print("Afin d'ajouter un peu de challenge, vous allez vous battre vontre le bot afin de savoir qui de vous deux vas commencer")
jouer = 1
time.sleep(0.5)
#Si jouer est égale à 1
if jouer == 1:
    #tant que jouer est égal à 1
    while jouer == 1:
        #Alors :
        #Créer variable winPlayerUn et la mettre à 0
        winPlayerUn = 0
        #Créer variable winPlayerRobot et la mettre à 0
        winRobot = 0
        #Définir nbJoueur qui retourne une fonction input qui demande combien y a-t-il de joueur
        nbJoueur = 1
        #Si typeJeu est égal à 1 et nbJoueur est égal à 1
        if nbJoueur == 1:
            #Alors :
            #créer une liste listeClassique avec "pierre" "feuille" "ciseaux"
            listeClassique = ["pierre","feuille","ciseaux"]
            #Définir round qui retourne une fonction input qui demande combien de round sont nécessaire pour gagner le match
            round = int(input("Combien de round seront nécaissaire pour gagner le match ? : "))
            # tant que winPlayerUn < round ou winRobot < round
            while winPlayerUn < round and winRobot < round:
                #Définir choixJoueur qui retourne une fonction input qui demande le choix du jouer
                choixJoueur = str(input("choisissez entre pierre feuille et ciseaux. Attention à bien écrire ! : "))
                #Définir choixRobot qui retourne une fonnction random dans la liste listeClassique
                choixRobot = random.choice(listeClassique)
                #Dormir 1 seconde
                time.sleep(1)
                #Ecrire pierre
                print("pierre")
                #Dormir 1 seconde
                time.sleep(1)
                #Ecrire fueille
                print("feuille")
                #Dormir 1 seconde
                time.sleep(1)
                #Ecrire ciseuax
                print("ciseaux")
                #dormir 1 seconde
                time.sleep(1)
                #Ecrire "Choix robot : ",choixRobot," VS Choix joueur : ",choixJoueur
                print("le robot à choisi : ",choixRobot," et vous avez choisi : ",choixJoueur,)
                #dormir 1 seconde
                time.sleep(1)
                #Si choixRobot == choixJoueur
                if choixRobot == choixJoueur:
                    #Alors : ecrire "égalité"
                    print("C'est une égalité !")
                #Sinon si choixRobot == "pierre" et choixJoueur == "ciseaux"
                elif choixRobot == "pierre" and choixJoueur == "ciseaux":
                    #Alors : ecrire "le robot à gagner et tu a perdue"
                    print("le robot à gagner et tu a perdue")
                    #Incrementer 1 à winRobot
                    winRobot = winRobot + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winPlayerUn " manche(s) remporté(s)."
                    print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winPlayerUn, " manche(s) remporté(s).")
                #Sinon si choixRobot == "ciseaux" et choixJoueur == "pierre"
                elif choixRobot == "ciseaux" and choixJoueur == "pierre":
                    #Alors : écrire "bravo tu as gagnés cette manche"
                    print("bravo tu as gagnés cette manche")
                    #Incrementer 1 à winPlayer
                    winRobot = winRobot + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winPlayerUn " manche(s) remporté(s)."
                    print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winPlayerUn, " manche(s) remporté(s).")
                #Sinon si choixRobot == "feuille" et choixJoueur == "pierre"
                elif choixRobot == "feuille" and choixJoueur == "pierre":
                    #Alors : ecrire "le robot à gagner et tu a perdue"
                    print("le robot à gagner et tu a perdue")
                    #Incrementer 1 à winRobot
                    winRobot = winRobot + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winPlayerUn " manche(s) remporté(s)."
                    print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winPlayerUn, " manche(s) remporté(s).")
                #Sinon si choixRobot == "pierre" et choixJoueur == "feuille"
                elif choixRobot == "pierre" and choixJoueur == "feuille":
                    #Alors : écrire "bravo tu as gagnés cette manche"
                    print("bravo tu as gagnés cette manche")
                    #Incrementer 1 à winPlayer
                    winRobot = winRobot + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winPlayerUn " manche(s) remporté(s)."
                    print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winPlayerUn, " manche(s) remporté(s).")
                #Sinon si choixRobot == "ciseaux" et choixJoueur == "feuille"
                elif choixRobot == "ciseaux" and choixJoueur == "feuille":
                    #Alors : ecrire "le robot à gagner et tu a perdue"
                    print("le robot à gagner et tu a perdue")
                    #Incrementer 1 à winRobot
                    winRobot = winRobot + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winPlayerUn " manche(s) remporté(s)."
                    print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winPlayerUn, " manche(s) remporté(s).")
                #Sinon si choixRobot == "feuille" et choixJoueur == "ciseaux"
                elif choixRobot == "feuille" and choixJoueur == "ciseaux":
                    #Alors : écrire "bravo tu as gagnés cette manche"
                    print("bravo tu as gagnés cette manche")
                    #Incrementer 1 à winPlayer
                    winRobot = winRobot + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winPlayerUn " manche(s) remporté(s)."
                    print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winPlayerUn, " manche(s) remporté(s).")
                #Sinon
                else:
                    #Alors : écrire "erreur, vous avez écris",choixJoueur,"au lieu de pierre, feuille, ciseaux"
                    print("erreur, vous avez écris",choixJoueur,"au lieu de pierre, feuille ou ciseaux")
            #Si winPlayerUn == round
            if winPlayerUn == round:
                #Alors : écrire "tu as gagner"
                print("tu as gagner")
                joueur = 1
            #Sinon
            else:
                #Alors : écrire "tu as perdu"
                print("tu as perdu")
                joueur = 2
            print(joueur)
            jouer = 0