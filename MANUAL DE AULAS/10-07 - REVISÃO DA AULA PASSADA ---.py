# 07/10/25 - REVISÃO DA AULA
# arq = open("arquivo", "mode(r,w,a)")


# "r" x = arq.read()
#     x = arq.readline()
#     x = arq.readlines()
      
# "w"     arq.write("valor")
#         arq.writelines("lista de valores")

# "a"     arq.write("valor")
#         arq.writelines("lista de valores")


# PEGAR OS NÚMEROS DO ARQUIVO E SOMAR(tudo que vem do arquivo é STRING)

# arq = open("aulas.txt", "r")


# conteudo = arq.readlines()

# soma = 0
# for i in range(0, len(conteudo))
#   soma += int(conteudo[i].strip()) o strip() REMOVE todo o espaço em branco do ínicio ao fim
# print(soma)

# arq.close()