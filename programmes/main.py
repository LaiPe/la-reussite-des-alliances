import fonctions
import test
tab="    "
if __name__ == "__main__":
    print("Bonjour")
    carte1={"valeur":"A","couleur":"C"}
    carte2={"valeur":"R","couleur":"T"}
    liCartes=[{"valeur":9,"couleur":"C"},{"valeur":10, "couleur":"K"},{"valeur":9,"couleur":"T"}]
    
    #fonctions.afficher_reussite(liCartes)
    #print(fonctions.carte_to_chaine(carte1))
    
    jeu=fonctions.init_pioche_fichier("../ressources/data_init.txt")
    print(jeu)
    fonctions.afficher_reussite(jeu)
    fonctions.ecrire_fichier_reussite("../ressources/test.txt",jeu)
    jeu=fonctions.init_pioche_fichier("../ressources/test.txt")
    fonctions.afficher_reussite(jeu)
    
    #jeu2 = fonctions.init_pioche_alea()
    #print(jeu2)
    #fonctions.afficher_reussite(jeu2)
    
    #a=fonctions.alliance(carte1,carte2)
    #if a:
    #    print("il y a une alliance")
    #else:
    #    print("y'a pas d'alliance")
    #print(fonctions.saut_si_possible(liCartes,2))
    #print(liCartes)
    """
    pioche=fonctions.init_pioche_alea()
    liCartes2=[]
    for i in range(6):
        fonctions.piocher(liCartes2,pioche)
    print("INIT:",end=" ")
    fonctions.afficher_reussite(liCartes2)
    fonctions.une_etape_reussite(liCartes2,pioche,True)
    print("FIN DE L'ETAPE:",end=" ")
    fonctions.afficher_reussite(liCartes2)
    """
    #test.test()

