nom1 = input("Nom de la première personne :")
prenom1 = input("Prénom de la première personne :")

nom2 = input("Nom de la deuxième personne :")
prenom2 = input("Prénom de la deuxième personne :")

aff1 = prenom1.capitalize() + " " + nom1.upper()
aff2 = prenom2.capitalize() + " " + nom2.upper()

personne1 = (nom1.lower(), prenom1.lower(), aff1)
personne2 = (nom2.lower(), prenom2.lower(), aff2)

liste = [personne1, personne2]
liste.sort()

print(liste[0][2])
print(liste[1][2])