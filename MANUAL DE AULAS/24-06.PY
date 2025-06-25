#VETORES - 24/06
#aluno = ["Thales", "Victor", "Gabriel"] * 3

#quantidade = int(input("Qual a quantidade de alunos sua sala tem: "))
#lista = [""] * quantidade
#lista[0] = "Thales"
#print("Na posição", 0, "está o aluno" , lista[0])


#1) 
#a)
valores = [9 , 18, 41, 65, 88, 121] * 6

#b)
professores = ["Rafael" , "Ayslan" , "Daniela" , "Frank"] * 4

#c)
valoresfloat = [3290.90, 128.50, 85.90, 789,31] * 4

#d) 
numeros = [0.0] * 5
numeros[0] = int(input("Insira um valor: "))
numeros[1] = int(input("Insira um valor: "))
numeros[2] = int(input("Insira um valor: "))
numeros[3] = int(input("Insira um valor: "))
numeros[4] = int(input("Insira um valor: "))
print("\n")

#2)
#a)
print(numeros)
print("\n")

#b)
invertido = [0.0] * 5
invertido[0] = numeros[4]
invertido[1] = numeros[3]
invertido[2] = numeros[2]
invertido[3] = numeros[1]
invertido[4] = numeros[0]
print(invertido)
print("\n")

#c)
dobro = [0.0] * 5
dobro[0] = numeros[0] * 2
dobro[1] = numeros[1] * 2
dobro[2] = numeros[2] * 2
dobro[3] = numeros[3] * 2
dobro[4] = numeros[4] * 2
print(dobro)
print("\n")

#d)
metade = [0.0] * 5
metade[0] = numeros[0] / 2
metade[1] = numeros[1] / 2
metade[2] = numeros[2] / 2
metade[3] = numeros[3] / 2
metade[4] = numeros[4] / 2
print(metade)
print("\n")

#3)
#a)
vetorstring = [0] * 4
vetorstring[0] = input("Nome completo: ")
vetorstring[1] = input("Endereço: ")
vetorstring[2] = input("Telefone: ")
vetorstring[3] = input("E-mail: ")

print("\n")
print(f"Nome Completo:\t\t\t" ,vetorstring[0])
print(f"Endereço:\t\t\t" ,vetorstring[1])
print(f"Telefone:\t\t\t" ,vetorstring[2])
print(f"E-mail:\t\t\t" ,vetorstring[3])
print("\n")

#4)
vetor = [0] * 4
vetor[0] = float(input("Insira um valor: "))
vetor[1] = float(input("Insira um valor: "))
vetor[2] = float(input("Insira um valor: "))
vetor[3] = float(input("Insira um valor: "))
print("\n")

#a)
soma = vetor[0] + vetor[1] + vetor[2] + vetor[3]
print(f"Soma:{soma}")
print("\n")

#b)
media =  soma / 4
print(f"Média:{media}")
print("\n")

#c)
produto = vetor[0] * vetor[1] * vetor[2] * vetor[3]
print(f"Produto: {produto}")
print("\n")

#d)
maiores_que_1000 = 0
if(vetor[0] > 1000): maiores_que_1000 += 1
if (vetor[1] > 1000): maiores_que_1000 += 1
if (vetor[2] > 1000): maiores_que_1000 += 1
if (vetor[3] > 1000): maiores_que_1000 += 1
print(f"Quantos valores são maiores do que 1000: {maiores_que_1000}")
print("\n")

#e)
maiores_que_zero = 0
if(vetor[0] > 0): maiores_que_zero += 1
if(vetor[1] > 0): maiores_que_zero += 1
if(vetor[2] > 0): maiores_que_zero += 1
if(vetor[3] > 0): maiores_que_zero += 1
print(f"Quantos valores são maiores do que zero: {maiores_que_zero}")
print("\n")

#f)
pares = 0
if(vetor[0] % 2 == 0):
    pares += 1
if(vetor[1] % 2 == 0):
    pares += 1
if(vetor[2] % 2 == 0):
    pares += 1 
if(vetor[3] % 2 == 0):
    pares += 1
print(f"Quantos valores são pares: {pares}")
print("\n")

#g)
maior_valor = vetor[0]
if (vetor[1] > maior_valor): maior_valor = vetor[1]
if (vetor[2] > maior_valor): maior_valor = vetor[2]
if (vetor[3] > maior_valor): maior_valor = vetor[3]
print(f"Maior valor do vetor: {maior_valor}")
print("\n")

#h)
indice_maior_valor = 0
if (vetor[1] == maior_valor): indice_maior_valor = 1
if (vetor[2] == maior_valor): indice_maior_valor = 2
if (vetor[3] == maior_valor): indice_maior_valor = 3
print(f"Índice do maior valor: {indice_maior_valor}")
print("\n")

# i)
menor_valor = vetor[0]
if (vetor[1] < menor_valor): menor_valor = vetor[1]
if (vetor[2] < menor_valor): menor_valor = vetor[2]
if (vetor[3] < menor_valor): menor_valor = vetor[3]
print(f"Menor valor do vetor: {menor_valor}")
print("\n")

#j)
indice_menor_valor = 0
if (vetor[1] == menor_valor): indice_menor_valor = 1
if (vetor[2] == menor_valor): indice_menor_valor = 2
if (vetor[3] == menor_valor): indice_menor_valor = 3
print(f"Índice do menor valor: {indice_menor_valor}")
print("\n")