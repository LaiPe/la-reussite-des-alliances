import main
import fnc
def tabVar():
    fnc.texte_encadre("TABLEAU DES VARIABLES")
    print(main.tab+"carte1:",carte1)
    print(main.tab+"carte2:",carte2)
    print(main.tab+"liCartes:",liCartes)
    print(main.tab+"liCartes2:",liCartes2)
    print(main.tab+"liCartes3:",liCartes3)
    print(main.tab+"car:",car)
    print(main.tab+"int:",int)

def choixVar(type):
    tabVar()
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
                return carte1
            elif choix=="2":
                return carte2
            else:
                print("Veuillez enter un carractère valide.") 
    elif type=="rc":
        if print("Voulez-vous modifier la valeur de cette variable? (o pour oui, n pour non):")=="o":
            car=input("Entrez une chaine de caractère")
        return car
    elif type=="ri":
        if print("Voulez-vous modifier la valeur de cette variable? (o pour oui, n pour non):")=="o":
            int=input("Entrez un entier")
        return int
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
                return liCartes
            elif choix=="2":
                return liCartes2
            elif choix=="3":
                return liCartes3
            else:
                print("Veuillez enter un carractère valide.")
                
def menuDeb():
    fnc.texte_encadre("MENU DE DEBOGAGE")
    print(
        main.tab+"1.Fonctions d'affichage",
        main.tab+"2.Fonctions de lecture/ecriture",
        main.tab+"3.Création de pioche",
        main.tab+"4.Fonctions de règles",
        main.tab+"5.Fonction étape",
        main.tab+"m.Modifier une variable",
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
                    choixVar("c")
                elif choix=="b":
                    choixVar("c")
                elif choix=="c":
                    choixVar("rc")
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
                    choixVar("lc")
                elif choix=="b":
                    choixVar("lc")
                elif choix=="r":
                    sousConti=False
                else:
                    print("Veuillez enter un carractère valide.") 
            conti=False
        elif choix=="3":
            print("oui")
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
            choixVar()
        elif choix=="q":
            return "q"
        else:
            print("Veuillez enter un carractère valide.")

if __name__=="__main__":
    print("Bienvenue dans le mode de débug. Cet environnement permet aux développeurs de tester et déboger leurs fonctions")
    carte1={"valeur":"A","couleur":"C"}
    carte2={"valeur":"R","couleur":"T"}
    liCartes=[{"valeur":9,"couleur":"C"},{"valeur":10, "couleur":"K"},{"valeur":9,"couleur":"T"}]
    liCartes2=[]
    liCartes3=[]
    car="random"
    int=3
    conti=True
    while conti:
        tabVar()
        if menuDeb()=="q":
            conti=False
