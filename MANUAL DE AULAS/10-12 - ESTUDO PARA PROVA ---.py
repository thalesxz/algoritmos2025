#1) BOLHA
def bolha(vetor):
    for ciclo in range(0, len(vetor)-1):
        for i in range(0, len(vetor)-1):
            if(vetor[i] > vetor[i+1]):
                copia = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = copia



#2) INSERÇÃO




#3) SELEÇÃO