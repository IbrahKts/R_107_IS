
somme = int(input("Entrez la somme en euros : "))

s100 = somme // 100
reste = somme % 100

s50 = reste // 50
reste = reste % 50

s10 = reste // 10
reste = reste % 10

p2 = reste // 2
p1 = reste % 2

print(f"{somme} euros, c’est donc {s100} billets de 100, {s50} de 50, {s10} de 10, "
      f"{p2} pièces de 2 et {p1} pièce 1.")
