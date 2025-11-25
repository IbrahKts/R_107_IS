L = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

max_occ = 0
most_frequent = L[0]

for i in range(len(L)):
    occ = 0
    for j in range(len(L)):
        if L[j] == L[i]:
            occ += 1
    if occ > max_occ:
        max_occ = occ
        most_frequent = L[i]

print(f"Le nombre le plus frequent dans la liste est le : {most_frequent} ({max_occ} x)")




L = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

max_occ = 0
most_frequent = L[0]

for x in L:
    if L.count(x) > max_occ:
        max_occ = L.count(x)
        most_frequent = x

print(f"Le nombre le plus frequent dans la liste est le : {most_frequent} ({max_occ} x)")