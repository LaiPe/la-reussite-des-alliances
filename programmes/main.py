import fnc
import test
if __name__ == "__main__":
    print("Bonjour")
    carte1={"valeur":"A","couleur":"C"}
    carte2={"valeur":"R","couleur":"T"}
    liCartes=[{"valeur":9,"couleur":"C"},{"valeur":10, "couleur":"K"},{"valeur":9,"couleur":"T"}]
    
    fnc.afficher_reussite(liCartes)
    print(fnc.carte_to_chaine(carte1))
    
    #jeu=fnc.init_pioche_fichier("../ressources/data_init.txt")
    #fnc.afficher_reussite(jeu)
    #fnc.ecrire_fichier_reussite("../ressources/test.txt",jeu)
    #jeu=fnc.init_pioche_fichier("../ressources/test.txt")
    #fnc.afficher_reussite(jeu)
    
    #jeu2 = fnc.init_pioche_alea()
    #fnc.afficher_reussite(jeu2)
    
    #a=fnc.alliance(carte1,carte2)
    #if a:
    #    print("il y a une alliance")
    #else:
    #    print("y'a pas d'alliance")
    #print(fnc.saut_si_possible(liCartes,2))
    #print(liCartes)
    """
    pioche=fnc.init_pioche_alea()
    liCartes2=[]
    for i in range(6):
        fnc.piocher(liCartes2,pioche)
    print("INIT:",end=" ")
    fnc.afficher_reussite(liCartes2)
    fnc.une_etape_reussite(liCartes2,pioche,True)
    print("FIN DE L'ETAPE:",end=" ")
    fnc.afficher_reussite(liCartes2)
    """
    #test.test()
