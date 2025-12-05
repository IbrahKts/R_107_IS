import random

def generer(nbr, vmin, vmax):
    tab = []
    for _ in range(nbr):
        tab.append(random.randint(vmin, vmax))
    return tab

def combienInferieur(table, vseuil):
    cpt = 0
    for val in table:
        if val < vseuil:
            cpt += 1
    return cpt


nb = int(input("Nombre d’éléments à générer : "))
vmin = int(input("Valeur min : "))
vmax = int(input("Valeur max : "))

tab = generer(nb, vmin, vmax)
tab.sort()
print(tab)

rep = input("Voulez-vous préciser le seuil ? (O/N) : ").upper()

if rep in ("O", "OUI"):
    seuil = int(input("Seuil : "))
else:
    seuil = 30

total = combienInferieur(tab, seuil)
print(f"Il y en a {total} inférieurs à {seuil}")
