import random
import time
exec(open(r"pfc_IA.py").read())
def afficher_grille(grille):
    print("     0)  1)  2)")
    print("   -------------")
    print("0)", end='')
    for i in range(3):
        print(" | "+str(grille[i]), end='')
    print(" |")
    print("   -------------")
    print("1)", end='')
    for i in range(3):
        print(" | "+str(grille[i+3]), end='')
    print(" |")
    print("   -------------")
    print("2)", end='')
    for i in range(3):
        print(" | "+str(grille[i+6]), end='')
    print(" |")
    print("   -------------")

def bot(grille):
    place = [0,1,2,3,4,5,6,7,8]
    #conditions de victoires
    if (grille[0] == grille[1]) and (grille[0] == "O") and (grille[2]!="X"):
        grille[2] = "O"
    elif (grille[2] == grille[1]) and (grille[2] == "O") and (grille[0]!="X"):
        grille[0] = "O"
    elif (grille[0] == grille[2]) and (grille[0] == "O") and (grille[1]!="X"):
        grille[1] = "O"
    elif (grille[3] == grille[4]) and (grille[3] == "O") and (grille[5]!="X"):
        grille[5] = "O"
    elif (grille[5] == grille[4]) and (grille[5] == "O") and (grille[3]!="X"):
        grille[3] = "O"
    elif (grille[3] == grille[5]) and (grille[5] == "O") and (grille[4]!="X"):
        grille[4] = "O"
    elif (grille[6] == grille[7]) and (grille[6] == "O") and (grille[8]!="X"):
        grille[8] = "O"
    elif (grille[8] == grille[7]) and (grille[8] == "O") and (grille[6]!="X"):
        grille[6] = "O"
    elif (grille[6] == grille[8]) and (grille[6] == "O") and (grille[7]!="X"):
        grille[7] = "O"
    elif (grille[0] == grille[3]) and (grille[0] == "O") and (grille[6]!="X"):
        grille[6] = "O"
    elif (grille[3] == grille[6]) and (grille[3] == "O") and (grille[0]!="X"):
        grille[0] = "O"
    elif (grille[0] == grille[6]) and (grille[0] == "O") and (grille[3]!="X"):
        grille[3] = "O"
    elif (grille[1] == grille[4]) and (grille[1] == "O") and (grille[7]!="X"):
        grille[7] = "O"
    elif (grille[4] == grille[7]) and (grille[7] == "O") and (grille[1]!="X"):
        grille[1] = "O"
    elif (grille[1] == grille[7]) and (grille[7] == "O") and (grille[4]!="X"):
        grille[4] = "O"
    elif (grille[2] == grille[5]) and (grille[2] == "O") and (grille[8]!="X"):
        grille[8] = "O"
    elif (grille[8] == grille[5]) and (grille[8] == "O") and (grille[2]!="X"):
        grille[2] = "O"
    elif (grille[2] == grille[8]) and (grille[2] == "O") and (grille[5]!="X"):
        grille[5] = "O"
    elif (grille[0] == grille[4]) and (grille[0] == "O") and (grille[8]!="X"):
        grille[8] = "O"
    elif (grille[4] == grille[8]) and (grille[4] == "O") and (grille[0]!="X"):
        grille[0] = "O"
    elif (grille[0] == grille[8]) and (grille[0] == "O") and (grille[4]!="X"):
        grille[4] = "O"
    elif (grille[2] == grille[4]) and (grille[2] == "O") and (grille[6]!="X"):
        grille[6] = "O"
    elif (grille[6] == grille[4]) and (grille[6] == "O") and (grille[2]!="X"):
        grille[2] = "O"
    elif (grille[2] == grille[6]) and (grille[2] == "O") and (grille[4]!="X"):
        grille[4] = "O"
    #conditions de blocages
    elif (grille[0] == grille[1]) and (grille[0] == "X") and (grille[2]!="O"):
        grille[2] = "O"
    elif (grille[2] == grille[1]) and (grille[2] == "X") and (grille[0]!="O"):
        grille[0] = "O"
    elif (grille[0] == grille[2]) and (grille[0] == "X") and (grille[1]!="O"):
        grille[1] = "O"
    elif (grille[3] == grille[4]) and (grille[3] == "X") and (grille[5]!="O"):
        grille[5] = "O"
    elif (grille[5] == grille[4]) and (grille[5] == "X") and (grille[3]!="O"):
        grille[3] = "O"
    elif (grille[3] == grille[5]) and (grille[5] == "X") and (grille[4]!="O"):
        grille[4] = "O"
    elif (grille[6] == grille[7]) and (grille[6] == "X") and (grille[8]!="O"):
        grille[8] = "O"
    elif (grille[8] == grille[7]) and (grille[8] == "X") and (grille[6]!="O"):
        grille[6] = "O"
    elif (grille[6] == grille[8]) and (grille[6] == "X") and (grille[7]!="O"):
        grille[7] = "O"
    elif (grille[0] == grille[3]) and (grille[0] == "X") and (grille[6]!="O"):
        grille[6] = "O"
    elif (grille[3] == grille[6]) and (grille[3] == "X") and (grille[0]!="O"):
        grille[0] = "O"
    elif (grille[0] == grille[6]) and (grille[0] == "X") and (grille[3]!="O"):
        grille[3] = "O"
    elif (grille[1] == grille[4]) and (grille[1] == "X") and (grille[7]!="O"):
        grille[7] = "O"
    elif (grille[4] == grille[7]) and (grille[7] == "X") and (grille[1]!="O"):
        grille[1] = "O"
    elif (grille[1] == grille[7]) and (grille[7] == "X") and (grille[4]!="O"):
        grille[4] = "O"
    elif (grille[2] == grille[5]) and (grille[2] == "X") and (grille[8]!="O"):
        grille[8] = "O"
    elif (grille[8] == grille[5]) and (grille[8] == "X") and (grille[2]!="O"):
        grille[2] = "O"
    elif (grille[2] == grille[8]) and (grille[2] == "X") and (grille[5]!="O"):
        grille[5] = "O"
    elif (grille[0] == grille[4]) and (grille[0] == "X") and (grille[8]!="O"):
        grille[8] = "O"
    elif (grille[4] == grille[8]) and (grille[4] == "X") and (grille[0]!="O"):
        grille[0] = "O"
    elif (grille[0] == grille[8]) and (grille[0] == "X") and (grille[4]!="O"):
        grille[4] = "O"
    elif (grille[2] == grille[4]) and (grille[2] == "X") and (grille[6]!="O"):
        grille[6] = "O"
    elif (grille[6] == grille[4]) and (grille[6] == "X") and (grille[2]!="O"):
        grille[2] = "O"
    elif (grille[2] == grille[6]) and (grille[2] == "X") and (grille[4]!="O"):
        grille[4] = "O"
    #blocage coin
    elif (grille[0]==grille[8]) and (grille[0]=="X") and (grille[4]=="O"):
        grille[3] = "O"
    elif (grille[2]==grille[6]) and (grille[2]=="X") and (grille[4]=="O"):
        grille[3] = "O"
    elif (grille[0] or grille[2] or grille[6] or grille[8]) == "X":
        grille[4] = "O"
    #random d??but
    else:
        bug = True
        while bug!=False:
            choix = random.choice(place)
            if grille[choix] == "O":
                bug = True
                del place[choix]
                print(choix)
            elif grille[choix] == "X":
                bug = True
                del place[choix]
                print(choix)
            elif grille[choix] == " ":
                bug = False
                print(choix)
                grille[choix] = "O"
            
    
        
def tour(grille,joueur):
    if joueur == 1:
        print("C'est \u00e0 toi joueur "+str(joueur))
        afficher_grille(grille)
        cover = 0
        liver = 0
        while cover == 0 or liver == 0:
            colonne = input("Le numero de colonne que tu veux jouer : ")
            ligne = input("Et maintenant la ligne : ")
            if grille[int(colonne)+int(ligne)*3]!=" ":
                afficher_grille(grille)
                print("Cette case est d\u00e9j\u00e0 prise >:( selectionne un autre case !")
            elif colonne >= "3":
                print("Cette valeur n'est pas d\u00e9finis recommence")
                cover = 0
            elif ligne >= "3":
                print("Cette valeur n'est pas d\u00e9finis recommence")
                liver = 0
            else:
                print("OK ! C'est plac\u00e9 dans la case ("+colonne+","+ligne+")")
                cover = 1
                liver = 1
                break
        grille[int(colonne)+int(ligne)*3]="X"
    elif joueur == "robot":
        print("le robot choisi...")
        time.sleep(3)
        bot(grille)
    afficher_grille(grille)
    time.sleep(1)

def gagnant(grille):
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
        return 1
    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]!=" "):
        return 1
    if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]!=" "):
        return 1
    if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]!=" "):
        return 1
    if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]!=" "):
        return 1
    if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]!=" "):
        return 1
    if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]!=" "):
        return 1
    if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]!=" "):
        return 1

def match_nul(grille):
    for i in range(9):
        if grille[i]==" ":
            return 0
    return 1


#DEBUT

print("Joueur 1 tu poss\u00e8de les X, le bot poss\u00e8de les O")
print("Que le match COMMENCE !!!")
grille=[" "," "," "," "," "," "," "," "," "]
gagne = 0
while gagne == 0:
    tour(grille,joueur)
    if gagnant(grille):
        print("Bravo joueur "+str(joueur)+" tu remporte la partie !")
        gagne = 1
    else:
        if match_nul(grille):
            print("Il n'y a plus de place ! C'est donc un match nul !")
            gagne = 1
    if joueur == 1:
        joueur = "robot"
    else:
        joueur = 1
print("Au-revoir !")

#FIN



