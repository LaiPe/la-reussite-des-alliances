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
def texte_encadre(texte,titre=False):
    if titre:
        texte=" "+texte+" "
        print("="*len(texte)*11)
        print("="*len(texte)*5,texte,"="*len(texte)*5,sep="")
        print("="*len(texte)*11)
        print()
    else:
        print("="*len(texte),texte,"="*len(texte))
#=======LECTURE/ECRITURE FICHIERS=======
def init_pioche_fichier(nomFichier):
    f=open(nomFichier)
    txt=f.read()
    li=txt.split()
    dico={}
    liCartes=[]
    for e in li:
        carte=e.split("-")
        if carte[0] in ["A","V","D","R"]:
            dico["valeur"]=carte[0]
        else:
            dico["valeur"]=int(carte[0])
        dico["couleur"]=carte[1]
        liCartes+=[dict(dico)]
    f.close()
    return liCartes
def ecrire_fichier_reussite(nomFichier,liCartes):
    f=open(nomFichier,"w")
    for carte in liCartes:
        if carte["valeur"] in ["A","V","D","R"]:
            f.write(carte["valeur"]+"-"+carte["couleur"]+" ")
        else:
            f.write(str(carte["valeur"])+"-"+carte["couleur"]+" ")
    f.close()
#==========CREATION DE PIOCHE==========
def init_pioche_alea(nb_cartes = 32):
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
def piocher(liste_tas,pioche):
    liste_tas+=[pioche.pop(0)]
#=========================ETAPE========================
def une_etape_reussite(liste_tas,pioche,affiche=False):
    piocher(liste_tas,pioche)
    if affiche:
        print("Pioche:",end=" ")
        afficher_reussite(liste_tas)

    saut=saut_si_possible(liste_tas,len(liste_tas)-1)
    if affiche and saut:
        print("Saut de pioche:",end=" ")
        afficher_reussite(liste_tas)
    if saut:
        i=2
        while i<len(liste_tas):
            saut=saut_si_possible(liste_tas,len(liste_tas)-1)
            i+=1
            if affiche and saut:
                print("Saut:",end=" ")
                afficher_reussite(liste_tas)
            if saut:
                i=2
