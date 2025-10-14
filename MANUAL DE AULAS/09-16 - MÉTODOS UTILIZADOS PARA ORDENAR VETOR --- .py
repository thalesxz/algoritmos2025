#16/09 -- MÉTODOS UTILIZADOS PARA ORDENAR VETOR
#BOLHA
#VALORES PRIMITIVOS: int, float, str, bool
def bolha(vetor):
    for ciclo in range(0, len(vetor)-1 ):
        for i in range(0, len(vetor)-1):
            if(vetor[i] > vetor[i+1]):  #DECRESCENTE = (vetor[i] < vetor[i+1])
                copia = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = copia

vet = [10, 9, 8, 7, 6, 7, 8]
print(vet) #Envia o valor original de referência
bolha(vet) #A função muda o original por referência
print(vet) #Envia o valor modificado pela função



# #INSERÇÃO

def insercao(vetor):
    for i in range(1, len(vetor)):
        temp = vetor[i] #armazena o valor
        j = i - 1 #guarda o i anterior
        while(j >= 0 and temp < vetor[j]):  #tem que parar antes de -1 ou se tiver um menor
            vetor[j+1] = vetor[j] #j representa possição anterior então, guarda na posição da frente
            j = j - 1 #e conta um pra trás
        vetor[j+1] = temp #se não funcionar mantém ele na mesma posição
    
        
vetor = [15, 10, 3, 12, 5, 7, 1]
print(vetor)
insercao(vetor)
print(vetor)


#SELEÇÃO
#2 variaveis controle MENOR e INDICIE DO MENOR VALOR
def selecao(vetor):
    for i in range(0, len(vetor)-1):
        menor = vetor[i]
        imenor = i
        for j in range(i+1, len(vetor)):
            if(vetor[j] < menor):
                menor = vetor[j]
                imenor = j
        vetor[imenor] = vetor[i]
        vetor[i] = menor

print(vetor)
selecao(vetor)
print(vetor)
