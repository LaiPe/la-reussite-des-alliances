import main
import fonctions
def tabVar():
    fonctions.texte_encadre("TABLEAU DES VARIABLES")
    print(main.tab+"carte1:",carte1)
    print(main.tab+"carte2:",carte2)
    print(main.tab+"liCartes:",liCartes)
    print(main.tab+"liCartes2:",liCartes2)
    print(main.tab+"liCartes3:",liCartes3)
    print(main.tab+"liFichier:",liFichier)
    print(main.tab+"car:",car)
    print(main.tab+"entier:",entier)

def affich_liFichier():
    for i in range(len(liFichier)):
        print(main.tab,i+1,".",liFichier[i],sep="")
def choixVar(type):
    print("Quelle variable choisissez-vous ?")
    if type=="c":
        print(
            main.tab+"1.carte1",
            main.tab+"2.carte2",
            sep="\n"
        )
        conti=True
        while conti:
            choix=input("Choix?:")
            if choix=="1":
                return "c1"
            elif choix=="2":
                return "c2"
            else:
                print("Veuillez enter un carractère valide.") 
    elif type=="lc":
        print(
            main.tab+"1.liCartes",
            main.tab+"2.liCartes2",
            main.tab+"3.liCartes3",
            sep="\n"
        )
        conti=True
        while conti:
            choix=input("Choix?:")
            if choix=="1":
                return "lc1"
            elif choix=="2":
                return "lc2"
            elif choix=="3":
                return "lc3"
            else:
                print("Veuillez enter un carractère valide.")
    else:
        print("Erreur: argument inconnu,  'type' dans choixVar(type) inconnu")
 
def choixFichier():
    global liFichier
    conti=True
    while conti:
        existFich=input("Votre fichier existe-il déjà ? (o pour oui, n pour non):")
        if existFich=="o":
            affich_liFichier()
            sousConti=True
            while sousConti:
                chFich=int(input("Lequel ?:"))
                if chFich in range(1,len(liFichier)+1):
                    return liFichier[chFich-1]
                else:
                    print("Veuillez enter un carractère valide.")
        if existFich=="n":
            nomFich=input("Donnez lui un nom (n'oubliez pas de noter l'extension):")
            f=open("../ressources/"+nomFich,"w")
            f.close
            liFichier+=[nomFich]
            return nomFich
        else:
            print("Veuillez enter un carractère valide.")

if __name__=="__main__":
    fonctions.texte_encadre("DEBUG_MODE",True)
    print(
        "Bienvenue dans le mode de débug.",
        "Il contient des paquets d'intructions classés par fonctions afin de les tester.",
        sep="\n"
    )
    #Variables
    carte1={"valeur":"A","couleur":"C"}
    carte2={"valeur":"R","couleur":"T"}
    liCartes=[{"valeur":9,"couleur":"C"},{"valeur":10, "couleur":"K"},{"valeur":9,"couleur":"T"}]
    liCartes2=[]
    liCartes3=[]
    liFichier=["data_init.txt","test.txt"]
    car="random"
    entier=3

    conti_prog=True
    while conti_prog:
        tabVar()
        fonctions.texte_encadre("MENU DE DEBOGAGE")
        print(
            main.tab+"1.Fonctions d'affichage",
            main.tab+"2.Fonctions de lecture/ecriture",
            main.tab+"3.Création de pioche",
            main.tab+"4.Fonctions de règles",
            main.tab+"5.Fonction étape",
            main.tab+"q.Fermer debug_mode",
            sep="\n"
            )
        conti=True
        while conti:
            choix=input("Choix?:")
            if choix=="1":
                print(
                    main.tab+"a.carte_to_chaine",
                    main.tab+"b.afficher_reussite",
                    main.tab+"c.texte_encadre",
                    main.tab+"r.Retour",
                    sep="\n"
                )
                sousConti=True
                while sousConti:
                    choix=input("Choix?:")
                    if choix=="a":
                        chVar=choixVar("c")
                        if chVar=="c1":
                            print(fonctions.carte_to_chaine(carte1))
                        elif chVar=="c2":
                            print(fonctions.carte_to_chaine(carte2))
                        else:
                            print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        input("(Appuyer sur entrer pour revenir au menu)")
                        sousConti=False
                    elif choix=="b":
                        chVar=choixVar("lc")
                        if chVar=="lc1":
                            fonctions.afficher_reussite(liCartes)
                        elif chVar=="lc2":
                            fonctions.afficher_reussite(liCartes2)
                        elif chVar=="lc3":
                            fonctions.afficher_reussite(liCartes3)
                        else:
                            print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        input("(Appuyer sur entrer pour revenir au menu)")
                        sousConti=False
                    elif choix=="c":
                        conti=True
                        while conti:
                            choix=input("Le texte est-il un titre ? (o pour oui, n pour non)")
                            if choix=="o":
                                fonctions.texte_encadre(car,True)
                                conti=False
                            elif choix=="n":
                                fonctions.texte_encadre(car)
                                conti=False
                            else:
                                print("erreur valeur")
                        input("(Appuyer sur entrer pour revenir au menu)")
                        sousConti=False
                    elif choix=="r":
                        sousConti=False
                    else:
                        print("Veuillez enter un carractère valide.")    
                conti=False
            elif choix=="2":
                print(
                    main.tab+"a.init_pioche_fichier",
                    main.tab+"b.ecrire_fichier_reussite",
                    sep="\n"
                )
                sousConti=True
                while sousConti:
                    choix=input("Choix?:")
                    if choix=="a":
                        chVar=choixVar("lc")
                        if chVar=="lc1":
                            liCartes=fonctions.init_pioche_fichier("../ressources/"+choixFichier())
                        elif chVar=="lc2":
                            liCartes2=fonctions.init_pioche_fichier("../ressources/"+choixFichier())
                        elif chVar=="lc3":
                            liCartes3=fonctions.init_pioche_fichier("../ressources/"+choixFichier())
                        else:
                            print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        input("(Appuyer sur entrer pour revenir au menu)")
                        sousConti=False
                    elif choix=="b":
                        chVar=choixVar("lc")
                        if chVar=="lc1":
                            liCartes=fonctions.ecrire_fichier_reussite("../ressources/"+choixFichier(),liCartes)
                        elif chVar=="lc2":
                            liCartes2=fonctions.ecrire_fichier_reussite("../ressources/"+choixFichier(),liCartes2)
                        elif chVar=="lc3":
                            liCartes3=fonctions.ecrire_fichier_reussite("../ressources/"+choixFichier(),liCartes3)
                        else:
                            print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        input("(Appuyer sur entrer pour revenir au menu)")
                        sousConti=False
                    elif choix=="r":
                        sousConti=False
                    else:
                        print("Veuillez enter un carractère valide.") 
                conti=False
            elif choix=="3":
                chVar=choixVar("lc")
                print("Création d'un jeu à 32 ou 52 cartes ?")
                chNbCartes=input("(ecrivez 32 pour le jeu à 32, n'importe quelle autre nombre pour le jeu à 52)")
                if chVar=="lc1":
                    liCartes=fonctions.init_pioche_alea(chNbCartes)
                elif chVar=="lc2":
                    liCartes2=fonctions.init_pioche_alea(chNbCartes)
                elif chVar=="lc3":
                    liCartes3=fonctions.init_pioche_alea(chNbCartes)
                else:
                    print("Erreur: variable inconnue, code retour choixVar() inconnu")
                input("(Appuyer sur entrer pour revenir au menu)")
                conti=False
            elif choix=="4":
                print(
                    main.tab+"a.alliance",
                    main.tab+"b.saut_si_possible",
                    main.tab+"c.piocher",
                    sep="\n"
                )
                sousConti=True
                while sousConti:
                    choix=input("Choix?:")
                    if choix=="a":
                        choixVar("c")#carte1
                        choixVar("c")#carte2
                    elif choix=="b":
                        choixVar("lc")#liCartes
                        choixVar("ri")#int
                    elif choix=="c":
                        choixVar("lc")#liCartes2
                        choixVar("lc")#liCartes3(pioche)
                    elif choix=="r":
                        sousConti=False
                    else:
                        print("Veuillez enter un carractère valide.") 
                conti=False
            elif choix=="5":
                print("oui")
                conti=False
            elif choix=="m":
                conti=False
            elif choix=="q":
                conti_prog=False
            else:
                print("Veuillez enter un carractère valide.")
