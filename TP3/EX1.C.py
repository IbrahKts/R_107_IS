cmp=0
cmp1=0
cmp2=0
n = int(input("Donnez un nombre entre 0 et 20:"))
for i in range (20):
    while not (0<= n <=20):
       n = int(input("Donnez un nombre :"))
    if i < 10:
        cmp+=1
    elif i >= 10 and i < 15:
        cmp1+=1
    elif i >= 15:
        cmp2+=1
    print(cmp)
    print(cmp1)
    print(cmp2)
