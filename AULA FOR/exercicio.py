import random

#1)
for i in range(1, 6):
    num = int(input("NÚMERO: "))
print("\n")

#2)
for i in range(1,6):
    numerosorteado = random.randint(1,100)
    print(numerosorteado)
print("\n")

#3)
X = int(input("Informe um valor inicial: "))
Y = int(input("Informe um valor final: "))
sorteio = int(input("Informe quantos números você quer sortear: "))
if(X > Y):
    for i in range(0, sorteio):
        Z = random.randint(Y, X)
        print(Z)
else:
    for i in range(0, sorteio):
        Z = random.randint(X, Y)
        print(Z)
print("\n")