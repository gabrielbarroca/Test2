def demander_age():
    while True:
        try:
            age = int(input("Quel est votre âge ? "))
            return age
        except ValueError:
            print("ERREUR, vous devez entrer un nombre.")

def check_age(age):
    if isinstance(age, int):
        return None
    raise ValueError("ERROR, you have to put a number")
    
def demander_nom():
    nom_personne = ""
    while nom_personne == "":
        nom_personne = input("Quel est votre nom ? ").strip()
        check_nom(nom_personne)
    return nom_personne

def check_nom(nom_personne):
    if isinstance(nom_personne, str):
        return None
    raise ValueError("ERREUR, vous devez rentrer un nom")


if __name__ == "__main__":
    nom1 = demander_nom()
    age1 = demander_age()    

    nom2 = demander_nom()
    age2 = demander_age()
    
    print(f"Vous vous appelez {nom1} et vous avez {age1} ans.")
    print(f"L'an prochain, vous aurez {age1 + 1} ans.")

    print(f"Vous vous appelez {nom2} et vous avez {age2} ans.")
    print(f"L'an prochain, vous aurez {age2 + 1} ans.")
