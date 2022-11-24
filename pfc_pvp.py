import time
jouer = 1
print("Afin de pimenter un peu la partie vous allez devoir faire un pierre feuille ciseaux pour savoir qui va commencer")
while jouer == 1:
#Créer variable winPlayerUn et la mettre à 0
    winPlayerUn = 0
        #Créer variable winPlayerDeux et la mettre à 0
    winPlayerDeux = 0
#Définir round qui retourne une fonction input qui demande combien de round sont nécessaire pour gagner le match
    round = int(input("Combien de round seront nécaissaire pour gagner le match ? : "))
    while winPlayerUn < round and winPlayerDeux < round:
                #Définir choixJoueurUn qui retourne une fonction input qui demande ce que veut jouer le joueur 1
        choixJoueurUn = str(input("joueur 1 choisissez entre pierre feuille et ciseaux. Attention à bien écrire ! : "))
                #Définir choixJoueurDeux qui retourne une fonction input qui demande ce que veut jouer le jouer 2
        choixJoueurDeux = str(input("joueur 2 choisissez entre pierre feuille et ciseaux. Attention à bien écrire ! : "))
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
            print("égalité")
        #Sinon si choixJoueurUn == "pierre" et choixJoueurDeux == "ciseaux"
        elif choixJoueurUn == "pierre" and choixJoueurDeux == "ciseaux":
            #Alors : ecrire "joueur 1 a gagner"
            print("joueur 1 a gangé")
            #Incrementer 1 à winPlayerUn
            winPlayerUn = winPlayerUn + 1
            #Dormir 0.5 seconde
            time.sleep(0.5)
            #Ecrire "joueur 1 est à ",winPlayerUn, "manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux " manche(s) remporté(s)."
            print("joueur 1 est à ",winPlayerUn," manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux," manche(s) remporté(s).")
        #Sinon si choixJoueurUn == "ciseaux" et choixJoueurDeux == "pierre"
        elif choixJoueurUn == "ciseaux" and choixJoueurDeux == "pierre":
            #Alors : écrire "joueur 2 à gagner"
            print("joueur 2 à gagner")
            #Incrementer 1 à winPlayerDeux
            winPlayerDeux = winPlayerDeux + 1
            #Dormir 0.5 seconde
            time.sleep(0.5)
            #Ecrire "joueur 1 est à ",winPlayerUn, "manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux " manche(s) remporté(s)."
            print("joueur 1 est à ",winPlayerUn," manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux," manche(s) remporté(s).")
        #Sinon si choixJoueurUn == "feuille" et choixJoueurDeux == "pierre"
        elif choixJoueurUn == "feuille" and choixJoueurDeux == "pierre":
            #Alors : ecrire "joueur 1 a gagner"
            print("joueur 1 a gangé")
            #Incrementer 1 à winPlayerUn
            winPlayerUn = winPlayerUn + 1
            #Dormir 0.5 seconde
            time.sleep(0.5)
            #Ecrire "joueur 1 est à ",winPlayerUn, "manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux " manche(s) remporté(s)."
            print("joueur 1 est à ",winPlayerUn," manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux," manche(s) remporté(s).")
        #Sinon si choixJoueurUn == "pierre" et choixJoueurDeux == "feuille"
        elif choixJoueurUn == "pierre" and choixJoueurDeux == "feuille":
            #Alors : écrire "joueur 2 à gagner"
            print("joueur 2 à gagner")
            #Incrementer 1 à winPlayerDeux
            winPlayerDeux = winPlayerDeux + 1
            #Dormir 0.5 seconde
            time.sleep(0.5)
            #Ecrire "joueur 1 est à ",winPlayerUn, "manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux " manche(s) remporté(s)."
            print("joueur 1 est à ",winPlayerUn," manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux," manche(s) remporté(s).")
        #Sinon si choixJoueurUn == "ciseaux" et choixJoueurDeux == "feuille"
        elif choixJoueurUn == "ciseaux" and choixJoueurDeux == "feuille":
            #Alors : ecrire "joueur 1 a gagner"
            print("joueur 1 a gangé")
            #Incrementer 1 à winPlayerUn
            winPlayerUn = winPlayerUn + 1
            #Dormir 0.5 seconde
            time.sleep(0.5)
            #Ecrire "joueur 1 est à ",winPlayerUn, "manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux " manche(s) remporté(s)."
            print("joueur 1 est à ",winPlayerUn," manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux," manche(s) remporté(s).")
        #Sinon si choixJoueurUn == "feuille" et choixJoueurDeux == "ciseaux"
        elif choixJoueurUn == "feuille" and choixJoueurDeux == "ciseaux":
            #Alors : écrire "joueur 2 à gagner"
            print("joueur 2 à gagner")
            #Incrementer 1 à winPlayerDeux
            winPlayerDeux = winPlayerDeux + 1
            #Dormir 0.5 seconde
            time.sleep(0.5)
            #Ecrire "joueur 1 est à ",winPlayerUn, "manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux " manche(s) remporté(s)."
            print("joueur 1 est à ",winPlayerUn," manche(s) remporté(s) et ","joueur 2 est à ",winPlayerDeux," manche(s) remporté(s).")
        elif choixJoueurUn != "pierre" or "feuille" or "ciseaux":
            choixJoueurUn = input(" Joueur 1, vous avez écrit " + choixJoueurUn + "au lieu de pierre, feuille, ou ciseau. veuillez réesayer : ")
        elif choixJoueurDeux != "pierre" or "feuille" or "ciseaux":
            choixJoueurDeux = input(" Joueur 2, vous avez écrit " + choixJoueurDeux + "au lieu de pierre, feuille, ou ciseau. veuillez réesayer : ")
    #Si winPLayerUn == round
    if winPlayerUn == round :
        #Alors : écrire "joueur 1 à gagner"
        print("joueur 1 à gagner")
        joueur = 1
    #Sinon
    else:
        #Alors : écrire "joueur 2 à gagner"
        print("joueur 2 à gagner")
        joueur = 2
    jouer = 0