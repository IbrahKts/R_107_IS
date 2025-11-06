BASE = 4
fromage = 800.0
eau = 2.0
ail = 2.0
pain = 400.0

nbConvives = int(input("Entrez le nombre de personne(s) conviÃ©es Ã  la fondue : "))

coef = nbConvives / BASE
q_fromage = fromage * coef
q_eau = eau * coef
q_ail = ail * coef
q_pain = pain * coef

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous")
print("faut :")
print(f"- {q_fromage} gr de fromage")
print(f"- {q_eau} dl d'eau")
print(f"- {q_ail} gousse(s) d'ail")
print(f"- {q_pain} gr de pain")