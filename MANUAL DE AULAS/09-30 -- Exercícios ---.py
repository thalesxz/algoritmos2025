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

arquivo = open("notas.txt", "w", encoding="utf8")
for i in range(0, 4):
    nome = input("NOME: ")
    nota = float(input(f"Nota de {nome}: "))
    arquivo.write(f"{nome}, {nota}\n")
arquivo.close()

arquivo = open("notas.txt", "r", encoding="utf8")
conteudo = arquivo.readlines()
arquivo.close()

for j in range(0, len(conteudo)):
    dados = conteudo[j].split(",")
    print(f"NOME: {dados[0]}     NOTA: {dados[1]}", end="")