import prog
def test():
    carte1={"valeur":"A","couleur":"C"}
    carte2={"valeur":"R","couleur":"T"}
    liCartes=[{"valeur":9,"couleur":"C"},{"valeur":10, "couleur":"K"},{"valeur":9,"couleur":"T"}]
    
    prog.afficher_reussite(liCartes)
    print(prog.carte_to_chaine(carte1))

