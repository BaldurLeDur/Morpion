import time
print("Afin de pimenter un peu la partie vous allez devoir faire un pierre feuille ciseaux pour savoir qui va commencer")

#Créer variable winPlayerUn et la mettre à 0
winPlayerUn = 0
#Créer variable winPlayerDeux et la mettre à 0
inPlayerDeux = 0
#Définir round qui retourne une fonction input qui demande combien de round sont nécessaire pour gagner le match
round = int(input("Combien de round seront n\u00e9caissaire pour gagner le match ? : "))
while winPlayerUn < round and winPlayerDeux < round:
    #Définir choixJoueurUn qui retourne une fonction input qui demande ce que veut jouer le joueur 1
    choixJoueurUn = str(input("joueur 1 choisissez entre pierre feuille et ciseaux. Attention à bien \u00e9crire ! : "))
    #Définir choixJoueurDeux qui retourne une fonction input qui demande ce que veut jouer le jouer 2
    choixJoueurDeux = str(input("joueur 2 choisissez entre pierre feuille et ciseaux. Attention à bien \u00e9crire ! : "))
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
    #Ecrire "Choix ","joueur 1 : ",choixJoueurUn," VS Choix ","joueur 2 : ",choixJoueurDeux
    print("joueur 1 à choisi ",choixJoueurUn," et ","joueur 2 à choisi ",choixJoueurDeux)
    #dormir 1 seconde
    time.sleep(1)
    #Si choixJoueurUn == choixJoueurDeux
    if choixJoueurUn == choixJoueurDeux:
        #Alors : ecrire "égalité"
        print("\u00e9galit\u00e9")
    #Sinon si choixJoueurUn == "pierre" et choixJoueurDeux == "ciseaux"
    elif choixJoueurUn == "pierre" and choixJoueurDeux == "ciseaux":
        #Alors : ecrire "joueur 1 a gagner"
        print("joueur 1 a gang\u00e9")
        #Incrementer 1 à winPlayerUn
        winPlayerUn = winPlayerUn + 1
        #Dormir 0.5 seconde
        time.sleep(0.5)
        #Ecrire "joueur 1 est à ",winPlayerUn, "manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux " manche(s) remporté(s)."
        print("joueur 1 est à ",winPlayerUn," manche(s) remport\u00e9(s) et ","joueur 2 est à ",winPlayerDeux," manche(s) remport\u00e9(s).")
    #Sinon si choixJoueurUn == "ciseaux" et choixJoueurDeux == "pierre"
    elif choixJoueurUn == "ciseaux" and choixJoueurDeux == "pierre":
        #Alors : écrire "joueur 2 à gagner"
        print("joueur 2 à gagner")
        #Incrementer 1 à winPlayerDeux
        winPlayerDeux = winPlayerDeux + 1
        #Dormir 0.5 seconde
        time.sleep(0.5)
        #Ecrire "joueur 1 est à ",winPlayerUn, "manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux " manche(s) remporté(s)."
        print("joueur 1 est à ",winPlayerUn," manche(s) remport\u00e9(s) et ","joueur 2 est à ",winPlayerDeux," manche(s) remport\u00e9(s).")
    #Sinon si choixJoueurUn == "feuille" et choixJoueurDeux == "pierre"
    elif choixJoueurUn == "feuille" and choixJoueurDeux == "pierre":
        #Alors : ecrire "joueur 1 a gagner"
        print("joueur 1 a gang\u00e9")
        #Incrementer 1 à winPlayerUn
        winPlayerUn = winPlayerUn + 1
        #Dormir 0.5 seconde
        time.sleep(0.5)
        #Ecrire "joueur 1 est à ",winPlayerUn, "manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux " manche(s) remporté(s)."
        print("joueur 1 est à ",winPlayerUn," manche(s) remport\u00e9(s) et ","joueur 2 est à ",winPlayerDeux," manche(s) remport\u00e9(s).")
    #Sinon si choixJoueurUn == "pierre" et choixJoueurDeux == "feuille"
    elif choixJoueurUn == "pierre" and choixJoueurDeux == "feuille":
        #Alors : écrire "joueur 2 à gagner"
        print("joueur 2 à gagner")
        #Incrementer 1 à winPlayerDeux
        winPlayerDeux = winPlayerDeux + 1
        #Dormir 0.5 seconde
        time.sleep(0.5)
        #Ecrire "joueur 1 est à ",winPlayerUn, "manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux " manche(s) remporté(s)."
        print("joueur 1 est à ",winPlayerUn," manche(s) remport\u00e9(s) et ","joueur 2 est à ",winPlayerDeux," manche(s) remport\u00e9(s).")
    #Sinon si choixJoueurUn == "ciseaux" et choixJoueurDeux == "feuille"
    elif choixJoueurUn == "ciseaux" and choixJoueurDeux == "feuille":
        #Alors : ecrire "joueur 1 a gagner"
        print("joueur 1 a gang\u00e9")
        #Incrementer 1 à winPlayerUn
        winPlayerUn = winPlayerUn + 1
        #Dormir 0.5 seconde
        time.sleep(0.5)
        #Ecrire "joueur 1 est à ",winPlayerUn, "manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux " manche(s) remporté(s)."
        print("joueur 1 est à ",winPlayerUn," manche(s) remport\u00e9(s) et ","joueur 2 est à ",winPlayerDeux," manche(s) remport\u00e9(s).")
    #Sinon si choixJoueurUn == "feuille" et choixJoueurDeux == "ciseaux"
    elif choixJoueurUn == "feuille" and choixJoueurDeux == "ciseaux":
        #Alors : écrire "joueur 2 à gagner"
        print("joueur 2 à gagner")
        #Incrementer 1 à winPlayerDeux
        winPlayerDeux = winPlayerDeux + 1
        #Dormir 0.5 seconde
        time.sleep(0.5)
        #Ecrire "joueur 1 est à ",winPlayerUn, "manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux " manche(s) remporté(s)."
        print("joueur 1 est à ",winPlayerUn," manche(s) remport\u00e9(s) et ","joueur 2 est à ",winPlayerDeux," manche(s) remport\u00e9(s).")
    elif choixJoueurUn != "pierre" or "feuille" or "ciseaux":
        choixJoueurUn = input(" Joueur 1, vous avez \u00e9crit " + choixJoueurUn + "au lieu de pierre, feuille, ou ciseau. veuillez r\u00e9esayer : ")
    elif choixJoueurDeux != "pierre" or "feuille" or "ciseaux":
        choixJoueurDeux = input(" Joueur 2, vous avez \u00e9crit " + choixJoueurDeux + "au lieu de pierre, feuille, ou ciseau. veuillez r\u00e9esayer : ")
#Si winPLayerUn == round
if winPlayerUn == round:
    #Alors : écrire "tu as gagner"
    print("joueur 1 à gagné")
    joueur = 1
    print("c'est au joueur 1 que revient le droit de commencer")
    #Sinon
else:
    #Alors : écrire "tu as perdu"
    print("tu as perdu")
    joueur = 2
    print("c'est au joueur 2 que revient le droit de commencer")
