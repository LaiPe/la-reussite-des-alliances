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

def init_liFichier():
    f=open("liFich.csv")
    txt=f.read()
    f.close()
    return txt.split(',')
def sauv_liFichier(nomfichier):
    f=open("liFich.csv","a")
    f.write(','+nomfichier)
    f.close()
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
                print("Veuillez entrer un carractère valide.") 
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
                print("Veuillez entrer un carractère valide.")
    else:
        print("Erreur: argument inconnu,  'type' dans choixVar(type) inconnu")
 
def choixFichier(liFichier):
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
                    print("Veuillez entrer un carractère valide.")
        if existFich=="n":
            nomFich=input("Donnez lui un nom (n'oubliez pas de noter l'extension):")
            f=open("../ressources/"+nomFich,"w")
            f.close
            liFichier+=[nomFich]
            sauv_liFichier(nomFich)
            return nomFich
        else:
            print("Veuillez entrer un carractère valide.")

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
    liCartes3=[{'valeur': 6, 'couleur': 'K'}, {'valeur': 6, 'couleur': 'T'}, {'valeur': 6, 'couleur': 'T'}, {'valeur': 10, 'couleur': 'T'}, {'valeur': 'A', 'couleur': 'P'}, {'valeur': 4, 'couleur': 'C'}, {'valeur': 5, 'couleur': 'P'}, {'valeur': 'D', 'couleur': 'K'}, {'valeur': 6, 'couleur': 'C'}, {'valeur': 5, 'couleur': 'C'}, {'valeur': 9, 'couleur': 'P'}, {'valeur': 9, 'couleur': 'T'}, {'valeur': 'A', 'couleur': 'K'}, {'valeur': 10, 'couleur': 'P'}, {'valeur': 8, 'couleur': 'T'}, {'valeur': 4, 'couleur': 'P'}, {'valeur': 'V', 'couleur': 'T'}, {'valeur': 2, 'couleur': 'K'}, {'valeur': 3, 'couleur': 'K'}, {'valeur': 'R', 'couleur': 'K'}, {'valeur': 2, 'couleur': 'C'}, {'valeur': 3, 'couleur': 'T'}, {'valeur': 2, 'couleur': 'P'}, {'valeur': 'R', 'couleur': 'T'}, {'valeur': 'A', 'couleur': 'T'}, {'valeur': 'V', 'couleur': 'K'}, {'valeur': 'D', 'couleur': 'T'}, {'valeur': 7, 'couleur': 'P'}, {'valeur': 6, 'couleur': 'P'}, {'valeur': 7, 'couleur': 'K'}, {'valeur': 7, 'couleur': 'T'}, {'valeur': 3, 'couleur': 'C'}, {'valeur': 'R', 'couleur': 'P'}, {'valeur': 10, 'couleur': 'K'}, {'valeur': 9, 'couleur': 'K'}, {'valeur': 9, 'couleur': 'C'}, {'valeur': 'A', 'couleur': 'C'}, {'valeur': 'V', 'couleur': 'P'}, {'valeur': 4, 'couleur': 'T'}, {'valeur': 'V', 'couleur': 'C'}, {'valeur': 4, 'couleur': 'K'}, {'valeur': 5, 'couleur': 'K'}, {'valeur': 'R', 'couleur': 'C'}, {'valeur': 10, 'couleur': 'C'}, {'valeur': 'D', 'couleur': 'P'}, {'valeur': 8, 'couleur': 'C'}, {'valeur': 8, 'couleur': 'K'}, {'valeur': 2, 'couleur': 'T'}, {'valeur': 'D', 'couleur': 'C'}, {'valeur': 7, 'couleur': 'C'}, {'valeur': 8, 'couleur': 'P'}, {'valeur': 3, 'couleur': 'P'}]
    liFichier=init_liFichier()
    car="DEBUG_MODES"
    entier=2

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
            main.tab+"6.Fonctions de parties",
            main.tab+"e.Extensions",
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
                    main.tab+"c.afficher_reussite_num",
                    main.tab+"d.texte_encadre",
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
                    elif choix == "c":
                        chVar = choixVar("lc")
                        if chVar=="lc1":
                            fonctions.afficher_reussite_num(liCartes)
                        elif chVar=="lc2":
                            fonctions.afficher_reussite_num(liCartes2)
                        elif chVar=="lc3":
                            fonctions.afficher_reussite_num(liCartes3)
                        else:
                            print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        input("(Appuyer sur entrer pour revenir au menu)")
                        sousConti=False

                    elif choix=="d":
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
                        print("Veuillez entrer un carractère valide.")    
                conti=False
            elif choix=="2":
                print(
                    main.tab+"a.init_pioche_fichier",
                    main.tab+"b.ecrire_fichier_reussite",
                    main.tab+"r.Retour",
                    sep="\n"
                )
                sousConti=True
                while sousConti:
                    choix=input("Choix?:")
                    if choix=="a":
                        chVar=choixVar("lc")
                        if chVar=="lc1":
                            liCartes=fonctions.init_pioche_fichier("../ressources/"+choixFichier(liFichier))
                        elif chVar=="lc2":
                            liCartes2=fonctions.init_pioche_fichier("../ressources/"+choixFichier(liFichier))
                        elif chVar=="lc3":
                            liCartes3=fonctions.init_pioche_fichier("../ressources/"+choixFichier(liFichier))
                        else:
                            print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        input("(Appuyer sur entrer pour revenir au menu)")
                        sousConti=False
                    elif choix=="b":
                        chVar=choixVar("lc")
                        if chVar=="lc1":
                            fonctions.ecrire_fichier_reussite("../ressources/"+choixFichier(liFichier),liCartes)
                        elif chVar=="lc2":
                            fonctions.ecrire_fichier_reussite("../ressources/"+choixFichier(liFichier),liCartes2)
                        elif chVar=="lc3":
                            fonctions.ecrire_fichier_reussite("../ressources/"+choixFichier(liFichier),liCartes3)
                        else:
                            print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        input("(Appuyer sur entrer pour revenir au menu)")
                        sousConti=False
                    elif choix=="r":
                        sousConti=False
                    else:
                        print("Veuillez entrer un carractère valide.") 
                conti=False
            elif choix=="3":
                chVar=choixVar("lc")
                print("Création d'un jeu à 32 ou 52 cartes ?")
                chNbCartes=int(input("(ecrivez 32 pour le jeu à 32, n'importe quelle autre nombre pour le jeu à 52)"))
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
                    main.tab+"r.Retour",
                    sep="\n"
                )
                sousConti=True
                while sousConti:
                    choix=input("Choix?:")
                    if choix=="a":
                        print("Test d'alliance entre carte1 et carte2:")
                        if fonctions.alliance(carte1,carte2):
                            print("Alliance possible entre 'carte1' et 'carte2'.")
                        else:
                            print("Alliance impossible entre 'carte1' et 'carte2'.")
                        sousConti=False
                        input("(Appuyer sur entrer pour revenir au menu)")
                    elif choix=="b":
                        chVar=choixVar("lc")
                        if chVar=="lc1":
                            li=liCartes 
                        elif chVar=="lc2":
                            li=liCartes2
                        elif chVar=="lc3":
                            li=liCartes3
                        else:
                            print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        entier=int(input("Choisissez l'index (attention à ne pas faire de sortie d'index):"))
                        if fonctions.saut_si_possible(li,entier):
                            print("Saut possible et effectué")
                        else:
                            print("Saut impossible")
                        sousConti=False
                        input("(Appuyer sur entrer pour revenir au menu)")
                    elif choix=="c":
                        print("Choisissez la pioche:")
                        chPioche=choixVar("lc")
                        if chPioche=="lc1":
                            pioche=liCartes 
                        elif chPioche=="lc2":
                            pioche=liCartes2
                        elif chPioche=="lc3":
                            pioche=liCartes3
                        else:
                            print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        print("Choisissez la liste dans laquelle la carte piochée ira:")
                        chVar=choixVar("lc")
                        if chVar=="lc1":
                            li=liCartes 
                        elif chVar=="lc2":
                            li=liCartes2
                        elif chVar=="lc3":
                            li=liCartes3
                        else:
                            print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        fonctions.piocher(li,pioche)
                        sousConti=False
                        input("(Appuyer sur entrer pour revenir au menu)")
                    elif choix=="r":
                        sousConti=False
                    else:
                        print("Veuillez entrer un carractère valide.") 
                conti=False
            elif choix=="5":
                print("Choisissez la pioche:")
                chPioche=choixVar("lc")
                if chPioche=="lc1":
                    pioche=liCartes 
                elif chPioche=="lc2":
                    pioche=liCartes2
                elif chPioche=="lc3":
                    pioche=liCartes3
                else:
                    print("Erreur: variable inconnue, code retour choixVar() inconnu")
                print("Choisissez la liste représentant le jeu:")
                chVar=choixVar("lc")
                if chVar=="lc1":
                    li=liCartes 
                elif chVar=="lc2":
                    li=liCartes2
                elif chVar=="lc3":
                    li=liCartes3
                else:
                    print("Erreur: variable inconnue, code retour choixVar() inconnu")
                chAffich=input("Afficher? (o pour oui):")
                affich=False
                if chAffich=="o":
                    affich=True
                fonctions.une_etape_reussite(li,pioche,affich)
                input("(Appuyer sur entrer pour revenir au menu)")
                conti=False
            elif choix=="6":
                print(
                    main.tab+"a.reussite_mode_auto",
                    main.tab+"b.reussite_mode_manuel",
                    main.tab+"c.lance_reussite",
                    main.tab+"r.Retour",
                    sep="\n"
                )
                sousConti=True
                while sousConti:
                    choix=input("Choix?:")
                    if choix=="a":
                        print("Choisissez la pioche:")
                        chPioche=choixVar("lc")
                        if chPioche=="lc1":
                            pioche=liCartes 
                        elif chPioche=="lc2":
                            pioche=liCartes2
                        elif chPioche=="lc3":
                            pioche=liCartes3
                        else:
                            print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        chAffich=input("Afficher? (o pour oui):")
                        affich=False
                        if chAffich=="o":
                            affich=True
                        flash=fonctions.reussite_mode_auto(pioche,affich)
                        chSauv=input("Voulez-vous sauvegarder la réussite ? (o pour oui):")
                        if chSauv=="o":
                            print("Choisissez la variable de sauvegarde:")
                            chVar=choixVar("lc")
                            if chVar=="lc1":
                                liCartes=flash 
                            elif chVar=="lc2":
                                liCartes2=flash
                            elif chVar=="lc3":
                                liCartes3=flash
                            else:
                                print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        input("(Appuyer sur entrer pour revenir au menu)")
                        sousConti=False
                        conti=False
                    elif choix=="b":
                        print("Choisissez la pioche:")
                        chPioche=choixVar("lc")
                        if chPioche=="lc1":
                            pioche=liCartes 
                        elif chPioche=="lc2":
                            pioche=liCartes2
                        elif chPioche=="lc3":
                            pioche=liCartes3
                        else:
                            print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        chNum=int(input("Chiffre palier pour victoire?:"))
                        flash=fonctions.reussite_mode_manuel(pioche,chNum)
                        chSauv=input("Voulez-vous sauvegarder la réussite ? (o pour oui):")
                        if chSauv=="o":
                            print("Choisissez la variable de sauvegarde:")
                            chVar=choixVar("lc")
                            if chVar=="lc1":
                                liCartes=flash 
                            elif chVar=="lc2":
                                liCartes2=flash
                            elif chVar=="lc3":
                                liCartes3=flash
                            else:
                                print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        input("(Appuyer sur entrer pour revenir au menu)")
                        sousConti=False
                        conti=False
                    elif choix=="c":
                        chChar=input("mode manuel ou automatique ? (m pour manuel, a pour auto):")
                        if chChar=="m":
                            chChar="manuel"
                        else: #a
                            chChar="auto"
                        flash=fonctions.lance_reussite(chChar)
                        chSauv=input("Voulez-vous sauvegarder la réussite ? (o pour oui):")
                        if chSauv=="o":
                            print("Choisissez la variable de sauvegarde:")
                            chVar=choixVar("lc")
                            if chVar=="lc1":
                                liCartes=flash 
                            elif chVar=="lc2":
                                liCartes2=flash
                            elif chVar=="lc3":
                                liCartes3=flash
                            else:
                                print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        input("(Appuyer sur entrer pour revenir au menu)")
                        sousConti=False
                        conti=False
                    elif choix=="r":
                        sousConti=False
                        conti=False
                    else:
                        print("Veuillez entrer un carractère valide.")
            elif choix == "e":
                sousConti = True
                while sousConti:
                    print(
                        main.tab+"a.verifier_pioche",
                        main.tab+"b.res_multi_simulation",
                        main.tab+"c.statistiques_nb_tas",
                        main.tab+"d.proba",
                        main.tab+"e.affiche_proba",
                        main.tab+"r.retour",
                        sep="\n"
                    )
                    choix = input("Choix?:")
                    if choix == "a":
                        chVar=choixVar("lc")
                        print("Jeu à 32 cartes ou 52 cartes ?")
                        nb_cartes=int(input("(ecrivez 32 pour le jeu à 32, n'importe quelle autre nombre pour le jeu à 52)"))
                        if nb_cartes!=32:
                            nb_cartes=52
                        if chVar=="lc1":
                            if fonctions.verifier_pioche(liCartes,nb_cartes):
                                print("Le jeu de carte est bon.")
                            else :
                                print("Le jeu de carte n'est pas bon")
                        elif chVar=="lc2":
                            if fonctions.verifier_pioche(liCartes2,nb_cartes):
                                print("Le jeu de carte est bon.")
                            else :
                                print("Le jeu de carte n'est pas bon")
                        elif chVar=="lc3":
                            if fonctions.verifier_pioche(liCartes3,nb_cartes):
                                print("Le jeu de carte est bon.")
                            else :
                                print("Le jeu de carte n'est pas bon")
                        else:
                            print("Erreur: variable inconnue, code retour choixVar() inconnu")
                        sousConti = False
                        conti = False
                        input("(Appuyer sur entrer pour revenir au menu)")
                    elif choix == "b":
                        print("Jeu à 32 cartes ou 52 cartes ?")
                        nb_cartes=int(input("(ecrivez 32 pour le jeu à 32, n'importe quelle autre nombre pour le jeu à 52)"))
                        if nb_cartes!=32:
                            nb_cartes=52
                        nb_sim = int(input("Combien de simulation voulez vous ?:"))
                        print(fonctions.res_multi_simulation(nb_sim,nb_cartes))
                        sousConti = False
                        conti = False
                        input("(Appuyer sur entrer pour revenir au menu)")
                    elif choix == "c":
                        print("Jeu à 32 cartes ou 52 cartes ?")
                        nb_cartes=int(input("(ecrivez 32 pour le jeu à 32, n'importe quelle autre nombre pour le jeu à 52)"))
                        if nb_cartes!=32:
                            nb_cartes=52
                        nb_sim = int(input("Combien de simulation voulez vous ?:"))
                        fonctions.statistiques_nb_tas(nb_sim,nb_cartes)
                        sousConti = False
                        conti = False
                        input("(Appuyer sur entrer pour revenir au menu)")
                    elif choix == "d":
                        print("Jeu à 32 cartes ou 52 cartes ?")
                        nb_cartes=int(input("(ecrivez 32 pour le jeu à 32, n'importe quelle autre nombre pour le jeu à 52)"))
                        if nb_cartes!=32:
                            nb_cartes=52
                        print(fonctions.proba(nb_cartes))
                        sousConti = False
                        conti = False
                        input("(Appuyer sur entrer pour revenir au menu)")
                    elif choix == "e":
                        print("Jeu à 32 cartes ou 52 cartes ?")
                        nb_cartes=int(input("(ecrivez 32 pour le jeu à 32, n'importe quelle autre nombre pour le jeu à 52)"))
                        if nb_cartes!=32:
                            nb_cartes=52
                        fonctions.affiche_proba(nb_cartes)
                        sousConti = False
                        conti = False
                        input("(Appuyer sur entrer pour revenir au menu)")
                    elif choix == "r":
                        sousConti = False
                        conti = False
                    else:
                        print("Veuillez entrer un carractère valide.")
            elif choix=="q":
                conti=False
                conti_prog=False
            else:
                print("Veuillez entrer un carractère valide.")