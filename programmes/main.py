import nfnc
import test
tab="    "
if __name__ == "__main__":
    print("Bonjour")
    carte1={"valeur":"A","couleur":"C"}
    carte2={"valeur":"R","couleur":"T"}
    liCartes=[{"valeur":9,"couleur":"C"},{"valeur":10, "couleur":"K"},{"valeur":9,"couleur":"T"}]
    
    #nfnc.afficher_reussite(liCartes)
    #print(nfnc.carte_to_chaine(carte1))
    
    #jeu=nfnc.init_pioche_fichier("../ressources/data_init.txt")
    #nfnc.afficher_reussite(jeu)
    #nfnc.ecrire_fichier_reussite("../ressources/test.txt",jeu)
    #jeu=nfnc.init_pioche_fichier("../ressources/test.txt")
    #nfnc.afficher_reussite(jeu)
    
    #jeu2 = nfnc.init_pioche_alea()
    #nfnc.afficher_reussite(jeu2)
    
    #a=nfnc.alliance(carte1,carte2)
    #if a:
    #    print("il y a une alliance")
    #else:
    #    print("y'a pas d'alliance")
    #print(nfnc.saut_si_possible(liCartes,2))
    #print(liCartes)
    """
    pioche=nfnc.init_pioche_alea()
    liCartes2=[]
    for i in range(6):
        nfnc.piocher(liCartes2,pioche)
    print("INIT:",end=" ")
    nfnc.afficher_reussite(liCartes2)
    nfnc.une_etape_reussite(liCartes2,pioche,True)
    print("FIN DE L'ETAPE:",end=" ")
    nfnc.afficher_reussite(liCartes2)
    """
    #test.test()
    print(test.tab)
