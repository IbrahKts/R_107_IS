
notes = []
coeffs = []

for i in range(1, 6):
    s = input(f"Veuillez entrer la note du module {i} et son coefficient : ")
    n, c = s.split()
    notes.append(float(n))
    coeffs.append(int(c))

total = sum(notes[i] * coeffs[i] for i in range(5))
coef_total = sum(coeffs)
moyenne = total / coef_total

admis = moyenne >= 10 and all(n >= 8 for n in notes)

print(f"Moyenne générale : {moyenne:.2f}")

if admis:
    print("L'étudiant est admis.")
else:
    print("L'étudiant n'est pas admis.")
