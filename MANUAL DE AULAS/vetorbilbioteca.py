#recebe um vetor e retorna ele ordenado pelo algoritmo de bolha
def bolha(vetor):
    for ciclo in range(0, len(vetor)-1):
        for i in range(0, len(vetor)-1):
            if(vetor[i] >= vetor[i+1]):
                copia = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = copia
    return vetor

#recebe um vetor e retorna ele ordenado pelo algoritmo de inserção
def insercao(vetor):
    for i in range(1, len(vetor)):
        temp = vetor[i] #armazena o valor
        j = i - 1 #guarda o i anterior
        while(j >= 0 and temp < vetor[j]):  #tem que parar antes de -1 ou se tiver um menor
            vetor[j+1] = vetor[j] #j representa possição anterior então, guarda na posição da frente
            j = j - 1 #e conta um pra trás
        vetor[j+1] = temp #se não funcionar mantém ele na mesma posição
    return vetor

#recebe um vetor e retorna ele ordenado pelo algoritmo de seleção
def selecao(vetor):
    for i in range(0, len(vetor)-1):
        menor = vetor[i]
        imenor = i
        for j in range(i+1, len(vetor)):
            if(vetor[j] < menor):
                vetor[j] = menor
                imenor = j
    vetor[imenor] = vetor[i] #valor com o menor indicie recebe
    vetor[i] = menor # valor com os primeiros indicies recebe o menor
    return vetor


#recebe um vetor e um número (valor) e retorna o índice daquele valor no vetor usando a busca sequencial ou retorna -1 se não tiver o valor
def buscasequencial(vetor, valor:int):
    for i in range(0, len(vetor)):
        if(valor == vetor[i]):
            return i
    return -1


#recebe um vetor e um número (valor) e retorna o índice daquele valor no vetor usando a busca binária ou retorna -1 se não tiver o valor
def buscabinaria(vetor, valor:int):
    inicio = 0
    fim = len(vetor)-1
    while(inicio <= fim):
        meio = (inicio+fim)//2
        if(vetor[meio] == valor):
            return meio
        elif(vetor[meio] > valor):
            fim = meio-1
        else:
            inicio = meio+1
    return -1
        



