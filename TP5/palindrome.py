
chaine = input("Entrez un mot ou une phrase : ")

filtre = ""
for c in chaine:
    if c.isalpha():
        filtre += c.lower()

if filtre == filtre[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
