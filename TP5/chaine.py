
T = list(input("Entrez une chaîne : "))


taille = 0
for _ in T:
    taille += 1

print("Taille :", taille)


voyelles = "aeiouy"
nb_voyelles = 0

for c in T:
    if c.lower() in voyelles:
        nb_voyelles += 1

pourcentage = nb_voyelles * 100 / taille if taille > 0 else 0
print(f"Pourcentage de voyelles : {pourcentage:.2f}%")


mot = list("wagon")
taille_mot = 5

def est_egal(T, i, mot):
    for k in range(taille_mot):
        if T[i + k].lower() != mot[k]:
            return False
    return True


premiere = -1
for i in range(taille - taille_mot + 1):
    if est_egal(T, i, mot):
        premiere = i
        break

if premiere == -1:
    print("La chaîne 'wagon' n'apparaît pas.")
else:
    print(f"Premier 'wagon' trouvé à l'indice {premiere}")


nb = 0
for i in range(taille - taille_mot + 1):
    if est_egal(T, i, mot):
        nb += 1

print(f"Nombre d'occurrences de 'wagon' : {nb}")
