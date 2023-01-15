import random
import time

def afficherGrille():
    print("       0     1     2\n"
          "    ┏━━━━━┳━━━━━┳━━━━━┓\n"
          " 0  ┃  "+grille[0][0]+"  ┃  "+grille[0][1]+"  ┃  "+grille[0][2]+"  ┃\n"
          "    ┣━━━━━╋━━━━━╋━━━━━┫\n"
          " 1  ┃  "+grille[1][0]+"  ┃  "+grille[1][1]+"  ┃  "+grille[1][2]+"  ┃\n"
          "    ┣━━━━━╋━━━━━╋━━━━━┫\n"
          " 2  ┃  "+grille[2][0]+"  ┃  "+grille[2][1]+"  ┃  "+grille[2][2]+"  ┃\n"
          "    ┗━━━━━┻━━━━━┻━━━━━┛\n")

def placerSymbole(ligne, col, symbole):
    grille[ligne][col] = symbole
    lstCasesLibres.remove((ligne,col))

def ifCaseLibre(ligne, col):
    if(grille[ligne][col]) == "_":
        return True
    return False

def bar():
    print("---------------------------------")

def verifVictoire(symbole):

    for i in grille:
        if i == [symbole for _ in range(3)]:
            return True

    for i in range(3):
        lst = []
        for k in grille:
            lst.append(k[i])
        if lst == [symbole for _ in range(3)]:
            return True

    if grille[0][0] == grille [1][1] == grille[2][2] == symbole\
            or grille[2][0] == grille[1][1] == grille[0][2] == symbole:
        return True
    return False

Rejouer = "O"
Joueur1 = {"prenom" : "", "symbole" : "X"}
Joueur2 = {"prenom" : "", "symbole" : "O"}

while Rejouer == "O":
    grille = [["_" for _ in range(3)] for _ in range(3)]
    lstCasesLibres = [(x,y) for x in range(3) for y in range(3)]
    Joueur1['prenom'] = input("Entrez le nom du joueur 1 : ")
    Joueur2['prenom'] = input("Entrez le nom du joueur 2 : ")
    bar()
    print(Joueur1['prenom'],"tu joueras les X")
    print(Joueur2['prenom'],"tu joueras les O")
    print("Un tirage au sort va désigner le premier joueur...")
    JoueurActuel = random.choice([Joueur1, Joueur2])
    time.sleep(1)
    bar()
    while True:
        print(JoueurActuel['prenom']," à ton tour !")
        afficherGrille()
        while True :
            while True :
                ligne = int(input("Choissisez la colonne"))
                if ligne not in [0, 1, 2]:
                    print("C'est impossible")
                else:
                    break
            while True :
                col = int(input("Choissisez la ligne"))
                if col not in [0,1,2]:
                    print("C'est impossible")
                else :
                    break
            if ifCaseLibre(ligne, col):
                break
            else :
                 print("Cette case est déjà remplie")

        placerSymbole(ligne, col, JoueurActuel['symbole'])
        bar()
        if verifVictoire(JoueurActuel['symbole']):
            afficherGrille()
            print("GG ", JoueurActuel['prenom'], " ! Tu as gagné !")
            break

        if len(lstCasesLibres) == 0:
            afficherGrille()
            print("Égalité ! Toutes les cases ont été remplies !")
            break

        if JoueurActuel == Joueur1:
            JoueurActuel = Joueur2
        else:
            JoueurActuel = Joueur1
    break
bar()
print("Merci d'avoir joué !")
bar()