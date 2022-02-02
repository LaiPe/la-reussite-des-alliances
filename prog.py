def carte_to_chaine(carte):
    dico=dict(carte)
    if type(carte["valeur"])=="int":
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
if __name__ == "__main__":
    print("Bonjour")
    carte1={"valeur":"3","couleur":"C"}
    print(carte_to_chaine(carte1))
    
