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
import random
X = int(input("Informe um valor inicial: "))
Y = int(input("Informe um valor final: "))
sorteio = int(input("Informe quantos números você quer sortear: "))
soma = 0

if(X > Y):
    Z = random.randint(Y, X)
else:
    Z = random.randint(X, Y)

menor = maior = Z

print(Z)
soma += Z

for i in range(1, sorteio):
    if(X > Y):
        Z = random.randint(Y, X)
    else:
        Z = random.randint(X, Y)

    print(Z)
    soma += Z

    if(Z < menor):
        menor = Z
    if (Z > maior):
        maior = Z

print("------ RELATÓRIO ------")
print(f"O menor valor gerado foi {menor}")
print(f"O maior valor gerado foi {maior}")
print(f"A soma dos números gerados é {soma}")