# ALGORITMOS DE BUSCA 
    # BUSCA LINEAR/PESQUISA SEQUENCIAL(funciona ordenado e não ordenado):
    # Complexidade = O(n)
vetor = [15, 10, 3, 12, 5, 7, 1]
valor = int(input("Informe um número: "))

#VERSÃO 1: Vetor não ordenado
encontrei = False 
posicao = None
for i in range(0, len(vetor)):
    if(valor == vetor[i]):
        encontrei = True
        posicao = i
        break
if(encontrei):
    print(f"Encontrado no vetor no indice {posicao}°.")

else:
    print("Não encontrado no vetor.")

#VERSÃO 2: Vetor ordenado
vet = [1, 3 ,5 ,7, 10, 12, 15]
encontrei = False 
posicao = None
for i in range(0, len(vet)):
    if(valor == vet[i]):
        encontrei = True
        posicao = i
        break
    elif(valor < vet[i]):
        break
if(encontrei):
    print(f"Encontrado no vetor no indice {posicao}°.")

else:
    print("Não encontrado no vetor.")


    #BUSCA BINÁRIA(funciona só com vetor ordenado)
        #3 váriaveis auxiliares inicio(regiao de busca), meio(regiao de busca), fim(regiao de busca) SÃO INDICIES E NÃO OS VALORES

        # inicio = 0 (caso seja mais que o meio) depois se torna i = m+1
        # meio = int((inicio + fim)/2)
        # fim = len(vetor)-1 (caso seja menor que o meio) depois se torna f= m-1
        # Complexidade = O(log n base 2)
print("Busca binária")
encontrei = False
posicao = -1 #-None
inicio = 0
fim = len(vet) - 1
while(inicio <= fim):
    meio = int((inicio + fim) / 2)

    if(vet[meio] == valor):
        encontrei = True
        posicao = meio
        break
    elif(vet[meio] > valor):
        fim = meio - 1
    else:
        inicio = meio + 1
        
if(encontrei):
    print(f"Encontrado no vetor no indice {posicao}°.")

else:
    print("Não encontrado no vetor.")