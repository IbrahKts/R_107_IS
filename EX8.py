x = float(input("Entrez un nombre décimal : "))

in_2_3 = (x >= 2 and x < 3)
in_0_1 = (x > 0 and x <= 1)
in_m10_m2 = (x >= -10 and x <= -2)

if in_2_3 or in_0_1 or in_m10_m2:
    print("x appartient à  I")
else:
    print("x n'appartient pas à  I")