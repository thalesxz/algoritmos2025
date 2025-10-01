# ORDENAÇÃO DOS VETORES


def ordenarvetor(vetor):
    for i in range(0, len(vetor) - 1):
        for x in range(0, len(vetor) - 1):
            if(vetor[x] > vetor[x + 1]):
                a = vetor[x + 1]
                vetor[x + 1] = vetor[x]
                vetor[x] = a
    return(vetor)






##
vetor = [130, 97, 86, 72, 43, 22]

for i in range(0, len(vetor) - 1):
    for x in range(0, len(vetor) - 1):
        if(vetor[x] > vetor[x + 1]):
            a = vetor[x + 1]
            vetor[x + 1] = vetor[x]
            vetor[x] = a
    print(vetor)
