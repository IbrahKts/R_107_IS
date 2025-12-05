def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst


lst1 = [0, 1, 2]


lst2 = ajouter_elt(lst1, len(lst1))


for lst in (lst1, lst2):
    print(lst, type(lst), id(lst))
