import random

def init_pioche_alea(nb_cartes=32):
    liCartes=[]
    carte={}
    couleurs=['C','P','K','T']
    valeurs32=[7,8,9,10,'A','V','D','R']
    valeurs=[2,3,4,5,6,7,8,9,10,'A','V','D','R']
    if nb_cartes==32:
        valeurs=valeurs32
    for couleur in couleurs:
        for valeur in valeurs:
            carte['valeur']=valeur
            carte['couleur']=couleur
            liCartes+=[dict(carte)]   
    random.shuffle(liCartes)
    return liCartes

nomvar=[
    "carte1",
    "carte2",
    "liCartes",
    "liCartes2",
    "liCartes3",
    "car"
]
var=[
    {"valeur":"A","couleur":"C"},
    {"valeur":"R","couleur":"T"},
    [{"valeur":9,"couleur":"C"},{"valeur":10, "couleur":"K"},{"valeur":9,"couleur":"T"}],
    [],
    [],
    "random"
]

chVar=int(input("Quelle variable? (0,1,2,3,4 ou 5):"))
print("Création d'un jeu à 32 ou 52 cartes ?")
chNbCartes=int(input("(ecrivez 32 pour le jeu à 32, n'importe quelle autre nombre pour le jeu à 52)"))
var[chVar]=init_pioche_alea(chNbCartes)
input("(Appuyer sur entrer pour revenir au menu)")

print(var[chVar])
