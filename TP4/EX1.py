x = float(input("Vous cherchez la table de multiplication de quel nombre:"))

table = []

for i in range (10):
    resultat = round (x * i, 1)
    table.append(resultat)

for i in range(10):
    print(f"{x} * {i} = {table[i]}")
