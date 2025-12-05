import unicodedata

def nettoyer(texte):
    propre = ""
    for c in texte:
        if c.isalnum():
            propre += c
    return propre

def enlever_accents(texte):
    nfkd = unicodedata.normalize("NFKD", texte)
    return "".join([c for c in nfkd if not unicodedata.combining(c)])

def est_palindrome(texte):
    texte = texte.lower()
    texte = enlever_accents(texte)
    texte = nettoyer(texte)
    return texte == texte[::-1]


phrase = input("Entrez un mot ou une phrase : ")

if est_palindrome(phrase):
    print("C’est un palindrome")
else:
    print("Ce n’est pas un palindrome")
