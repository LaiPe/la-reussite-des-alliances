def carte_to_chaine(carte):
    dico=dict(carte)
    if not(carte["valeur"] in ["A","V","D","K"]):
        dico["valeur"]=str(carte["valeur"])
    if dico["valeur"]!="10":
        dico["valeur"]=" "+dico["valeur"]
       
    if dico["couleur"]=="C":
        return dico["valeur"]+chr(9825)
    elif dico["couleur"]=="P":
        return dico["valeur"]+chr(9824)
    elif dico["couleur"]=="P":
        return dico["valeur"]+chr(9826)
    else:
        return dico["valeur"]+chr(9827)
def afficher_reussite(liCartes):
    for carte in liCartes:
        print((carte_to_chaine(carte)),end=" ")
    print("\n")
if __name__ == "__main__":
    print("Bonjour")
    carte={"valeur":3,"couleur":"C"}
    liCartes=[{"valeur":3,"couleur":"C"},{"valeur":10, "couleur":"K"},{"valeur":9,"couleur":"T"}]
    afficher_reussite(liCartes)
    #print(carte_to_chaine(carte))
    
