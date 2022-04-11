import random
import main
import numpy as np
import matplotlib.pyplot as plt
#=========AFFICHAGE=============
def carte_to_chaine(carte):
    result=""
    if carte["valeur"]!=10:
        result+=" "
    result+=str(carte["valeur"])
    
    if carte["couleur"]=="C":
        return result+chr(9825)
    elif carte["couleur"]=="P":
        return result+chr(9824)
    elif carte["couleur"]=="K":
        return result+chr(9826)
    else: #trèfle
        return result+chr(9827)
def afficher_reussite(liCartes):
    for carte in liCartes:
        print(carte_to_chaine(carte),end=" ")
    print("\n")
def afficher_reussite_num(liCartes):
    i=0
    li_saut=[]
    for carte in liCartes:
        print(carte_to_chaine(carte),end=" ")
        if carte["valeur"]==10:
            li_saut+=[True]
        else:
            li_saut+=[False]
    print()
    for saut in li_saut:
        if saut:
            print(" ","^"*3,sep="",end=" ")
        else:
            print(" ","^"*2,sep="",end=" ")
    print()
    cpt=1
    for saut in li_saut:
        if saut:
            print(" "*3,cpt,sep="",end=" ")
        else:
            print(" "*2,cpt,sep="",end=" ")
        cpt+=1
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
#==========REGLES============
def alliance(carte1,carte2):
    alliance=False
    if carte1["valeur"]==carte2["valeur"] or carte1["couleur"]==carte2["couleur"]:
        alliance=True
    return alliance
def saut_si_possible(liste_tas,num_tas):
    if (len(liste_tas)<3) or (num_tas>(len(liste_tas)-2)):
        return False
    a=alliance(liste_tas[num_tas-1],liste_tas[num_tas+1])
    if a:
        liste_tas.pop(num_tas-1)
        return True
    else:
        return False
def piocher(liste_tas,pioche):
    liste_tas+=[pioche.pop(0)]
#=========================ETAPE========================
def une_etape_reussite(liste_tas,pioche,affiche=False):
    piocher(liste_tas,pioche)
    if affiche:
        afficher_reussite(liste_tas)

    saut=saut_si_possible(liste_tas,len(liste_tas)-2)
    if affiche and saut:
        afficher_reussite(liste_tas)
    if saut:
        i=1
        while i<len(liste_tas)-1:
            saut=saut_si_possible(liste_tas,i)
            if affiche and saut:
                afficher_reussite(liste_tas)
            if saut:
                i=0
            i+=1
    return None
#=================PARTIE==========================
def reussite_mode_auto(pioche,affiche=False):
    if affiche:
        afficher_reussite(pioche)
    liste_tas=[]
    i=0
    l=len(pioche)
    piocheM=list(pioche)
    
    while i<l:
        une_etape_reussite(liste_tas,piocheM,affiche)
        i+=1
    return liste_tas
def reussite_mode_manuel(pioche,nb_tas_max=2):
    piocheM=list(pioche)
    l=len(pioche)
    i=0
    conti=True
    liste_tas=[]
    while conti and i<l :
        texte_encadre("La Réussite des Alliances")
        print(
            main.tab+"a.Piocher",
            main.tab+"b.Faire un saut",
            main.tab+"f.Fin de partie",
            sep="\n"
                )
        choix=input("Choix?:")
        if choix=="a":
            piocher(liste_tas,piocheM)
            afficher_reussite(liste_tas)
            i+=1
        elif choix=="b":
            afficher_reussite_num(liste_tas)
            print(
                "Choisissez un tas pour réaliser le saut. Indiquez le nombre du tas supérieur.",
                "Par exemple, si vous voulez réaliser un saut entre le premier et le troisième tas, entrer le chiffre 3.",
                sep="\n"
            )
            chTas=int(input("Choix?:"))-1
            if saut_si_possible(liste_tas,chTas):
                print("Saut effectué")
            else:
                print("Saut impossible")
        elif choix=="f":
            conti=False
    print("Fin de la partie !")
    while i<l:
        piocher(liste_tas,piocheM)
        afficher_reussite(liste_tas)
        i+=1
    print("Voici votre jeu:")
    afficher_reussite(liste_tas)
    print("Votre pioche était:")
    afficher_reussite(pioche)
    if len(liste_tas)<=nb_tas_max:
        print("Félicitations, vous avez gagné !")
    else:
        print("Malheureusement, vous avez perdu...")
    return liste_tas
def lance_reussite(mode,nb_cartes=32,affiche=False,nb_tas_max=2):
    if mode=="manuel":
        return reussite_mode_manuel(init_pioche_alea(nb_cartes),nb_tas_max)
    else: #auto
        return reussite_mode_auto(init_pioche_alea(nb_cartes),affiche)
#====================EXTENSIONS====================
def verifier_pioche(liCartes,nb_cartes=32):
    liCartesVerif=init_pioche_alea(nb_cartes)
    result=True
    for carteV in liCartesVerif:
        if not(carteV in liCartes):
            result=False
            break
    if len(liCartes)!=nb_cartes:
        result=False
    return result

def res_multi_simulation(nb_sim,nb_cartes=32):
    result=[]
    for i in range(nb_sim):
        pioche=init_pioche_alea(nb_cartes)
        liCartes=reussite_mode_auto(pioche)
        result+=[len(liCartes)]
    return result
def statistiques_nb_tas(nb_sim,nb_cartes=32):
    appel = res_multi_simulation(nb_sim,nb_cartes)
    if not(len(appel)>0):
        print("Pas de valeur dans la liste")
        return None
    moyenne = 0
    maxi = None
    mini = None
    for i in range(len(appel)):
        moyenne += appel[i]
        if maxi == None or appel[i] > maxi:
            maxi = appel[i]
        if mini == None or appel[i] < mini:
            mini = appel[i]
    moyenne = moyenne/nb_sim
    print("La moyenne est :",moyenne)
    print("le minimum est :",mini)
    print("le maximum est :",maxi)

def proba(nb_cartes=32):
    i=2
    prctage=0
    result=[]
    while i<=nb_cartes:
        li=res_multi_simulation(100,nb_cartes)
        for e in li:
            if e<=i:
                prctage+=1
        result+=[prctage]
        i+=1
        prctage=0
    return result
def affiche_proba(nb_cartes=32):
    x=[]
    y=proba(nb_cartes)
    for e in range(2,nb_cartes+1):
        x+=[str(e)]
    plt.plot(x,y)
    plt.xlabel("Nombres de cartes limite pour la victoire")
    plt.ylabel("Pourcentage de réussite")
    plt.show()
