date = input("Entrez une date au format jjmmaaaa : ")

if len(date) != 8 or not date.isdigit():
    print("Format incorrect, veuillez saisir 8 chiffres.")
else:
    jour = int(date[0:2])
    mois = int(date[2:4])
    annee = int(date[4:8])


    bissextile = (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)


    mois31 = [1, 3, 5, 7, 8, 10, 12]
    mois30 = [4, 6, 9, 11]

    valide = True

    if mois < 1 or mois > 12:
        valide = False
    elif mois in mois31 and not (1 <= jour <= 31):
        valide = False
    elif mois in mois30 and not (1 <= jour <= 30):
        valide = False
    elif mois == 2:
        if bissextile and not (1 <= jour <= 29):
            valide = False
        elif not bissextile and not (1 <= jour <= 28):
            valide = False

    if valide:
        print("Date correcte")
    else:
        print("Date incorrecte")