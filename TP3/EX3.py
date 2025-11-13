from random import *
essais = 0
N = randint(0, 100)
x = int(input("Devinez le nombre:"))
while x != N:
    essais +=1
    if x < N:
        print("le nombre est plus grand")
    elif x > N:
        print("Le nombre est plus petit")

    x = int(input("Devinez le nombre"))
essais+=1
print("bien jouer vous avez réussi")
