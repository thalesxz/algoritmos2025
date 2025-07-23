#EXERCIOS LISTA

#1)
# numeros = [0] * 100
# for i in range(0, len(numeros)):
#     numeros[i] = i + 1

# for i in range(0, len(numeros)):
#     print(f"{numeros[i]}")
# print("\n")


# #b)
# for i in range(len(numeros) - 1, -1, -1):
#     print(f"{numeros[i]}")
# print("\n")


# #c)
# for i in range(0, len(numeros)):
#     numeros[i] = (i + 1) * 2

# for i in range(0, len(numeros)):
#     print(f"{numeros[i]}")
# print("\n")


# #d) e e)
# soma = 0 
# for i in range(0, len(numeros) + 1):
#     soma = soma + i
# media = soma / 100
# print(soma)
# print(media)
# print("\n")


# #f)
#pares = 0
# for i in range(0, len(numeros)):
#     if(i % 2 == 0):
#         pares = pares + 1
# print(f"Quantidade de pares: {pares}")


# #2)
# armazenar = [0] * 6
# for i in range(0, len(armazenar)):
#     armazenar[i] = int(input(f"ME INFORME VALOR {i+1} PARA LOTERIA: "))
# print("Obrigado por informar os números!")
# print(f"Números sorteados para a loteria: {armazenar}")


# # #3)
# nomes = [""] * 5
# for i in range(0, len(nomes)):
#     nomes[i] = input(f"Aluno {i + 1}: ")
# print(f"Alunos presentes: {nomes}")


# #4)
# tamanho = int(input("Me informe um número para ser o tamanho do vetor: "))
# vetor = [0] * tamanho
# for i in range(0, len(vetor)):
#     vetor[i] = int(input(f"Valor {i + 1}: ")) 
# print(f"Números digitados: {vetor}")


# #5) (vetor utilizado no ex anterior)
vetor = [3, 6, 1, 3, 6, 7]
print("Números em ordem inversa:")
for i in range(len(vetor) - 1, -1, -1):  
    print(vetor[i])

soma = 0
for i in range(0, len(vetor)):
    soma += vetor[i]

print("\nSoma de todos os elementos:", soma)

media = soma / len(vetor)  
print("Média aritmética dos valores:", media)

print("\nNúmeros nas posições pares:")
for i in range(0, len(vetor), 2):
    print(vetor[i])