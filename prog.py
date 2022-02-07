import random
#=========AFFICHAGE=============
def carte_to_chaine(carte):
    dico=dict(carte)
    if not(carte["valeur"] in ["A","V","D","R"]):
        dico["valeur"]=str(carte["valeur"])
    if dico["valeur"]!="10":
        dico["valeur"]=" "+dico["valeur"]
       
    if dico["couleur"]=="C":
        return dico["valeur"]+chr(9825)
    elif dico["couleur"]=="P":
        return dico["valeur"]+chr(9824)
    elif dico["couleur"]=="K":
        return dico["valeur"]+chr(9826)
    else: #trèfle
        return dico["valeur"]+chr(9827)
def afficher_reussite(liCartes):
    for carte in liCartes:
        print((carte_to_chaine(carte)),end=" ")
    print("\n")
#=======LECTURE/ECRITURE FICHIERS=======
def init_pioche_fichier(nomFichier):
    f=open(nomFichier)
    txt=f.read()
    li=txt.split()
    dico={}
    liCartes=[]
    for e in li:
        carte=e.split("-")
        dico["valeur"]=carte[0]
        dico["couleur"]=carte[1]
        liCartes+=[dict(dico)]
    f.close()
    return liCartes
def ecrire_fichier_reussite(nomFichier,liCartes):
    f=open(nomFichier,"w")
    for carte in liCartes:
        f.write(carte["valeur"]+"-"+carte["couleur"]+" ")
    f.close()
#=======CREATION DE PIOCHE========
def init_pioche_alea(nb_cartes = 32):
    liCartes=[]
    carte={}
    couleurs=['C','P','K','T']
    valeurs32=['7','8','9','10','A','V','D','R']
    valeurs=['2','3','4','5','6','7','8','9','10','A','V','D','R']
    if nb_cartes==32:
        valeurs=valeurs32
    for couleur in couleurs:
        for valeur in valeurs:
            carte['valeur']=valeur
            carte['couleur']=couleur
            liCartes+=[dict(carte)]   
    random.shuffle(liCartes)
    return liCartes
#==========REGLES============
def alliance(carte1,carte2):
    alliance=False
    if carte1["valeur"]==carte2["valeur"] or carte1["couleur"]==carte2["couleur"]:
        alliance=True
    return alliance
def saut_si_possible(liste_tas,num_tas):
    a=alliance(liste_tas[num_tas-2],liste_tas[num_tas])
    if a:
        liste_tas.pop(num_tas-2)
        return True
    else:
        return False

if __name__ == "__main__":
    print("Bonjour")
    carte1={"valeur":"A","couleur":"C"}
    carte2={"valeur":"R","couleur":"T"}
    liCartes=[{"valeur":3,"couleur":"C"},{"valeur":10, "couleur":"K"},{"valeur":3,"couleur":"K"}]
    
    #afficher_reussite(liCartes)
    #print(carte_to_chaine(carte))
    
    #jeu=init_pioche_fichier("data_init.txt")
    #afficher_reussite(jeu)
    #ecrire_fichier_reussite("test.txt",jeu)
    #jeu=init_pioche_fichier("test.txt")
    #afficher_reussite(jeu)
    
    #jeu2 = init_pioche_alea()
    #afficher_reussite(jeu2)

    a=alliance(carte1,carte2)
    if a:
        print("il y a une alliance")
    else:
        print("y'a pas d'alliance")

    print(saut_si_possible(liCartes,2))
    print(liCartes)

