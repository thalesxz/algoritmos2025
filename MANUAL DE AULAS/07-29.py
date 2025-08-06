#CONTINUAÇÃO DOS EXECÍCIOS DA AULA PASSADA
#6)
# quantidade = int(input("Quantos números você deseja adicionar à lista para calcular a tabuada? "))

# vetor = [0] * quantidade 

# for i in range(0, len(vetor)):
#     vetor[i] = int(input(f"Informe o {i + 1}º número: "))

# print("\nNúmeros e seus respectivos dobros:")
# for i in range(0, len(vetor)):
#     print(f"{vetor[i]} -> {vetor[i] * 2}")

# for i in range(0, len(vetor)):
#     numero = vetor[i]
#     print(f"\nTabuada do {numero}:")
#     for j in range(1, 11):  # Corrigido o segundo índice para 'j' para não sobrescrever 'i'
#         print(f"{numero} x {j} = {numero * j}")

#7)

# quantidade = int(input("INFORME QUAL A QUANTIDADE DE CONVIDADOS PARA A FESTA: "))
# convidados = [''] * quantidade
# for i in range(0, len(convidados)):
#     convidados[i] = str(input(f"Convidado {i + 1}(nome completo): "))

# print("\nLista de Convidados:")
# for i in range(0, len(convidados)):
#     print(convidados[i]) 

#8)

# vendas = int(input("Número de vendas: "))
# vetor = [0] * vendas
# for i in range(0, len(vetor)):
#     vetor[i] = float(input(f"{i + 1}ª VENDA (valor): R$ "))

# soma = 0 
# for i in range(0, len(vetor)):
#     venda = vetor[i]
#     if(venda <= 999.99):
#         soma += venda * 0.05
#     if(venda >= 1000 and venda <= 1999.99):
#         soma += venda * 0.04
#     if(venda >= 2000):
#         soma += venda * 0.03
# print(f"\nA comissão total de Roberto é: R$ {soma:.2f}")

#8)
# quantidade = int(input("INFORME A QUANTIDADE DE ALUNOS: "))
# vetor_alunos = [''] * quantidade
# vetor_conceitos = [''] * quantidade

# for i in range(0, quantidade):
#     vetor_alunos[i] = input(f"Informe o nome do {i + 1}º aluno: ")
#     vetor_conceitos[i] = input(f"Informe o conceito de {vetor_alunos[i]} (A, B, C, D, F): ")

# print("\nLista de alunos e seus conceitos:")
# for i in range(0, quantidade):
#     print(f"{vetor_alunos[i]} -> {vetor_conceitos[i]}")

#9)
# sorteio = [0] * 6  
# print("Informe os 6 números sorteados para a loteria: ")
# for i in range(0, len(sorteio)):
#     sorteio[i] = int(input(f"Digite o {i + 1}º número sorteado: "))

# aposta = [0] * 6 
# print("\nInforme os 6 números que você apostou:")
# for i in range(0, len(aposta)):
#     aposta[i] = int(input(f"Digite o {i + 1}º número apostado: "))


# acertos = 0
# for i in range(0, 6):
#     for cont in range(0, 6):
#         if (aposta[i] == sorteio[cont]):
#             acertos += 1
#             break  

# print(f"\nVocê acertou {acertos} números.")

# if acertos == 6:
#     print("Parabéns! Você ganhou o prêmio principal! Nunca mais vai precisar trabalhar!")
# elif acertos == 5:
#     print("Você acertou a quina! Parabéns!")
# elif acertos == 4:
#     print("Você acertou a quadra! Parabéns!")
# elif acertos >= 0 and acertos <= 3:
#     print("Você não ganhou nada dessa vez. Tente novamente!")

#10)
# import random

# sorteio = [0] * 6

# i = 0
# while i < 6:
#     num = random.randint(1, 10)
#     repetido = 0  
#     for j in range(i):
#         if(sorteio[j] == num):
#             repetido = 1
#             break
#     if(repetido == 0):
#         sorteio[i] = num
#         i += 1

# aposta = [0] * 6
# print("\nInforme os 6 números que você apostou (entre 1 e 10, sem repetir): ")

# for i in range(0, 6):
#     num = int(input(f"Digite o {i + 1}º número apostado: "))
    
#     while(num < 1 or num > 10):
#         print("Número fora do intervalo! Digite novamente.")
#         num = int(input(f"Digite o {i + 1}º número apostado: "))
    
#     repetido = 0
#     for j in range(i):
#         if aposta[j] == num:
#             repetido = 1
#             break
#     while(repetido == 1):
#         print("Número repetido! Digite outro número.")
#         num = int(input(f"Digite o {i + 1}º número apostado: "))
#         repetido = 0
#         for j in range(i):
#             if aposta[j] == num:
#                 repetido = 1
#                 break
    
#     aposta[i] = num

# acertos = 0
# for i in range(6):
#     for j in range(6):
#         if aposta[i] == sorteio[j]:
#             acertos += 1
#             break

# print(f"\nNúmeros sorteados: {sorteio}")
# print(f"Sua aposta:        {aposta}")
# print(f"\nVocê acertou {acertos} número(s).")

# if(acertos == 6):
#     print("Parabéns! Você ganhou o prêmio principal! Nunca mais vai precisar trabalhar!")
# elif(acertos == 5):
#     print("Você acertou a quina! Parabéns!")
# elif(acertos == 4):
#     print("Você acertou a quadra! Parabéns!")
# else:
#     print("Você não ganhou nada dessa vez. Tente novamente!")

#11)
# nome = input("Digite seu nome: ")

# nome_invertido = ""

# for i in range(len(nome) - 1, -1, -1):
#     nome_invertido += nome[i]

# print("Nome invertido:", nome_invertido)

#12)
# import random

# pessoas = [0] * 10

# print("Digite os nomes de 10 pessoas:")

# for i in range(0, len(pessoas)):
#     pessoas[i] = input(f"Nome da pessoa {i + 1}: ")

# indice_sorteado = random.randint(0, 9)
# pessoa_sorteada = pessoas[indice_sorteado]

# print(f"\nA pessoa sorteada foi: {pessoa_sorteada}")

#13)
# import random

# palavras = [0] * 10

# print("Digite 10 palavras:")

# for i in range(0, len(palavras)):
#     palavras[i] = input(f"Palavra {i + 1}: ")

# indice_sorteado = random.randint(0, 9)
# palavra_sorteada = palavras[indice_sorteado]

# print(f"\nPalavra sorteada: {palavra_sorteada}")
# letra = input("Digite uma letra para verificar quantas vezes ela aparece na palavra sorteada: ")

# contador = 0
# for i in range(0, len(palavra_sorteada)):
#     if (palavra_sorteada[i] == letra):
#         contador += 1

# print(f"A letra '{letra}' aparece {contador} vez(es) na palavra sorteada.")


#14)
# perguntas = [
#     "Telefonou para a vítima?",
#     "Esteve no local do crime?",
#     "Mora perto da vítima?",
#     "Devia para a vítima?",
#     "Já trabalhou com a vítima?"
# ]

# respostas = [0] * 5  
# soma = 0

# print("Responda com S (sim) ou N (não):\n")

# for i in range(0, len(respostas)):
#     resposta = input(perguntas[i] + " ").strip().upper()
#     if(resposta == "S"):
#         respostas[i] = 1
#         soma += 1

# if(soma == 5):
#     classificacao = "Assassino"
# elif(soma >= 3):
#     classificacao = "Cúmplice"
# elif(soma == 2):
#     classificacao = "Suspeita"
# else:
#     classificacao = "Inocente"

# print(f"\nClassificação: {classificacao}")

#15)
# n = int(input("Quantos times vão participar do campeonato? "))

# nomes = [0] * n
# pontos = [0] * n

# for i in range(0, len(nomes)):
#     nomes[i] = input(f"Digite o nome do {i + 1}º time: ")
#     pontos[i] = int(input(f"Digite a pontuação final do time {nomes[i]}: "))

# indice_campeao = 0
# indice_vice = -1

# for i in range(1, n):
#     if(pontos[i] > pontos[indice_campeao]):
#         indice_vice = indice_campeao
#         indice_campeao = i
#     elif(indice_vice == -1 or pontos[i] > pontos[indice_vice]):
#         if(i != indice_campeao):
#             indice_vice = i

# print("\nResultado Final:")
# print(f"Campeão: {nomes[indice_campeao]} com {pontos[indice_campeao]} pontos.")
# print(f"Vice-campeão: {nomes[indice_vice]} com {pontos[indice_vice]} pontos.")

