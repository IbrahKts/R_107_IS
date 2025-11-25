nbEtudiants = int(input("Donnez le nombre d'étudiants :"))

notes = []

for i in range(nbEtudiants):
    note = float(input(f"note étudiants {i} : "))

    notes.append(note)

moyenne = sum(notes) / nbEtudiants

print("\nMoyenne de classe :", moyenne)

print("\nNumero de l'etudiant  note  ecart a la moyenne")
for i in range(nbEtudiants):
    ecart =notes[i] - moyenne
    print(f"{i:>10}|{notes[i]:>4}|{ecart:>8.3f}")