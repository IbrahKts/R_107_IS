n = int(input("Entrez un nombre entier: "))

if n == 0:
    print("Le nombre est zéro (et il est pair)")
else:
    signe = "positif" if n > 0 else "négatif"
    parite = "pair" if n % 2 == 0 else "impair"
    print(f"Le nombre est {signe} et {parite}")