"""Enregistrer etudiant"""
def enregistrer_nom_et_prenom():
    liste_Nom = list()
    liste_Prenom = list()

    while True:
        nom = input("Entrer le nom : ")
        if not nom.isalpha():
            print("Veuillez saisir une chaîne de caractères. Réessayer svp...")
        else:
            liste_Nom.append(nom)
            break

    while True:
        prenom = input("Entrer le prenom : ")
        if not prenom.isalpha():
            print("Veuillez saisir une chaîne de caractères. Réessayer svp...")
        else:
            liste_Prenom.append(prenom)
            break

    print("  Nom \t\t  Prenom")
    print("{} \t {}".format(liste_Nom,liste_Prenom))

enregistrer_nom_et_prenom()

while True:
    reponse = input("Voulez-vous faire un autre enregistrement ? (oui/non) :  ")
    if not reponse.isalpha():
            print("Veuillez saisir (oui/non). Réessayer svp...")
    else:
        if reponse.lower() != "oui":
            break
        enregistrer_nom_et_prenom()