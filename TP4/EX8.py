etu1 = {
    "firstname": "titi",
    "name": "toto",
    "promo": 2022,
    "group": 202
}

etu2 = {
    "firstname": "tutu",
    "name": "tata",
    "promo": 2022,
    "group": 102
}

binome = {
    "id1": etu1,
    "id2": etu2
}

print("Les clés du dictionnaire sont :")
for k in etu1.keys():
    print("-", k)

print("\nLes valeurs du dictionnaire sont :")
for v in etu1.values():
    print("-", v)

print("\nLes tuplets du dictionnaire sont :")
for item in etu1.items():
    print("-", item)

print("\nLes étudiants formants le binôme sont :")
for id, etu in binome.items():
    print(f"- L'étudiant {etu['name']} {etu['firstname']} du groupe {etu['group']}")
