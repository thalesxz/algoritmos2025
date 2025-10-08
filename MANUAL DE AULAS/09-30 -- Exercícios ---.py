import random
#1)

# arquivo = open("frutas.txt", "w", encoding="utf8")

# for i in range(0, 5):
#     frutas = input("Digite o nome de uma fruta: ")
#     arquivo.write(f"{frutas}\n")

# arquivo.close()

#2)

# arquivo = open("frutas.txt", "r", encoding="utf8")

# conteudo = arquivo.readlines()

# arquivo.close()

# quantidade = len(conteudo)

# for i in range(0, len(conteudo)):
#     print(f"Eu adoro a fruta: {conteudo[i]}", end="")

#3)

# arquivo = open("frutas.txt", "a", encoding="utf8")

# for i in range(0, 3):
#     frutas = input("Digite mais 3 frutas: ")
#     arquivo.write(f"{frutas}\n")

# arquivo.close()

# arquivo = open("frutas.txt", "r", encoding="utf8")
# conteudo = arquivo.readlines()
# arquivo.close()

# quantidade = len(conteudo)

# for j in range(0, len(conteudo)):
#     print(conteudo[j], end="")

#4)

# arquivo = open("frutas.txt", "w", encoding="utf8")
# arquivo.close()
# print("Desculpa esqueci tudo...")

#5)

# arquivo = open("compras.txt", "w", encoding="utf8")
# for i in range(0, 5):
#     compras = input("Digite cada item de compra: ")
#     arquivo.write(f"{compras}\n")

# arquivo.close()

#6)

# arquivo = open("compras.txt", "r", encoding="utf8")
# conteudo = arquivo.readlines()
# arquivo.close()

# quantidade = len(conteudo)
# for i in range(0, len(conteudo)):
#     print(f"{i+1}° - {conteudo[i]}", end="")

#7)
# resposta = input("Deseja adicionar mais itens? (s/n): ").lower()

# while(resposta == 's'):
#     qtd = int(input("Quantos itens deseja adicionar: "))
#     arquivo = open("compras.txt", "a", encoding="utf8")
#     for i in range(qtd):
#         compras = input("Digite o item para adicionar: ")
#         arquivo.write(f"{compras}\n")
#     arquivo.close()


#     arquivo = open("compras.txt", "r", encoding="utf8")
#     conteudo = arquivo.readlines()
#     arquivo.close()

#     for i in range(0, len(conteudo)):
#         print(f"{i+1}° - {conteudo[i]}", end="")


#     resposta = input("\nDeseja adicionar mais itens? (s/n): ").lower()


#8)

# arquivo = open("notas.txt", "w", encoding="utf8")
# for i in range(0, 4):
#     nome = input("NOME: ")
#     nota = float(input(f"Nota de {nome}: "))
#     arquivo.write(f"{nome}, {nota}\n")
# arquivo.close()

# arquivo = open("notas.txt", "r", encoding="utf8")
# conteudo = arquivo.readlines()
# arquivo.close()

# soma = 0
# maiornota = 0
# alunomaiornota = ""
# for j in range(0, len(conteudo)):
#     dados = conteudo[j].split(",")
#     nome = dados[0]
#     nota = float(dados[1])
#     soma += float(dados[1])
#     print(f"NOME: {dados[0]}     NOTA: {dados[1]}", end="")

#     if(nota > maiornota):
#         maiornota = nota
#         alunomaiornota = nome

#     if(nota < 8.0):
#         print(f"{nome} ficou com a nota menor que 8.0 !")

# media = soma/len(conteudo)
# print(f"A média da turma foi {media}")
# print(f"A maior nota foi {maiornota} e foi tirada por {alunomaiornota}")

#9)
# arquivo = open("compras_clientes.txt", "w", encoding="utf8")
# for i in range(0, 5):
#     nome = input("Nome: ")
#     valor = float(input("Valor: "))
#     arquivo.write(f"{nome}, {valor}\n")
# arquivo.close()

# arquivo = open("compras_clientes.txt", "r", encoding="utf8")
# conteudo = arquivo.readlines()
# arquivo.close()

# relatorio = input("Informe o nome do cliente que quer consultar: ")

# gasto = 0
# for j in range(0, len(conteudo)):
#     dados = conteudo[j].split(",")
#     nome = dados[0]
#     valor = float(dados[1])
#     if(nome == relatorio):
#         gasto += valor

# if(gasto > 0):
#     print(f"{relatorio} - Total: R${gasto:.2f}")
# else:
#     print(f"Não há compras registradas para o cliente {relatorio}.")

# #10)
# arquivo = open("vendas.txt", "w", encoding="utf8")
# for i in range(0, 4):
#     data = input("Informe uma data(ANO-MES-DIA): ")
#     nome = input("Nome do cliente: ")
#     total = float(input("Total: "))
#     arquivo.write(f"{data},{nome},{total}\n")
# arquivo.close()

# arquivo = open("vendas.txt", "r", encoding="utf8")
# conteudo = arquivo.readlines()
# arquivo.close()

# relatorio = input("Me informe o data de consulta(ANO-MES-DIA): ")

# soma = 0

# for j in range(0, len(conteudo)):
#     dados = conteudo[j].split(",")
#     data = dados[0]
#     nome = dados[1]
#     total = float(dados[2])
#     if(relatorio == data):
#         print(f"DATA: {data}, NOME: {nome}, TOTAL:{total}")
#         soma += total

# print(f"O total feito foi {soma}")

# #11)
    
# arquivo = open("vendas.txt", "w", encoding="utf8")
# for i in range(0, 4):
#     data = input("Informe uma data(ANO-MES-DIA): ")
#     nome = input("Nome do cliente: ")
#     total = float(input("Total: "))
#     arquivo.write(f"{data},{nome},{total}\n")
# arquivo.close()

# arquivo = open("vendas.txt", "r", encoding="utf8")
# conteudo = arquivo.readlines()
# arquivo.close()

# cliente = input("Me informe o cliente: ")

# soma = 0
# cont = 0

# for j in range(0, len(conteudo)):
#     dados = conteudo[j].strip().split(",")
#     data = dados[0]
#     nome = dados[1]
#     total = float(dados[2])
#     if(cliente == nome):
#         print(f"DATA: {data}, NOME: {nome}, TOTAL:{total}")
#         soma += total
#         cont += 1
# print(f"O gasto foi R${soma}")
# print(f"Você comprou {cont} vezes.")

# if(cont > 0):
#     media = soma / cont
#     print(f"Média de gasto: R${media}")
# else:
#     print("Este cliente não fez compras.")

#12)

# arquivo = open("vendas.txt", "w", encoding="utf8")
# for i in range(0, 4):
#     data = input("Informe uma data(ANO-MES-DIA): ")
#     nome = input("Nome do cliente: ")
#     total = float(input("Total: "))
#     arquivo.write(f"{data},{nome},{total}\n")
# arquivo.close()

# arquivo = open("vendas.txt", "r", encoding="utf8")
# conteudo = arquivo.readlines()
# arquivo.close()

# relatorio = input("Deseja que faça um relatório(s/n): ").lower()
# cont = 0
# totalvendas = 0
# clientemaisgasto = ""
# gastomax = 0
# maiorfaturamento = 0
# datamaiorfaturamento = ""

# if(relatorio == "s"):
#     for j in range(len(conteudo)): 
#         dados = conteudo[j].strip().split(",")
#         data = dados[0]
#         nome = dados[1]
#         total = float(dados[2])

#         print(f"DATA: {data}, NOME: {nome}, TOTAL: R${total}")
        
#         cont += 1
#         totalvendas += total
    
#         if(total > gastomax):
#             gasto_max = total
#             clientemaisgasto = nome
        
#         if(total > maiorfaturamento):
#             maiorfaturamento = total
#             datamaiorfaturamento = data

#     print("Relatório Geral:")
#     print(f"Total de vendas: R${totalvendas}")
#     print(f"Número de vendas: {cont}")
#     print(f"Cliente que mais gastou: {clientemaisgasto} (R${gastomax})")
#     print(f"Dia com maior faturamento: {datamaiorfaturamento} (R${maiorfaturamento})")

# else:
#     print("Relatório não gerado.")

#13)
arquivo = open("adivinhação.txt", "w", encoding="utf8")
sorteio = random.randint(0, 20)
arquivo.write(f"{sorteio}")
arquivo.close()

arquivo = open("adivinhação.txt", "r", encoding="utf8")
conteudo = arquivo.readline()
arquivo.close()

tentativa = None
cont = 0
while(tentativa != sorteio):
    tentativa = int(input("Informe qual o valor sorteado(0,20): "))
    cont += 1
    if(tentativa > sorteio):
        print("Errou")
        print("Menor")
    if(tentativa < sorteio):
        print("Errou")
        print("Maior")
print("Você acertou!!!")
print(f"{cont} foi o total de tentativa necessária para o acerto!!!")