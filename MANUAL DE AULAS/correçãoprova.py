notas = [0.0] * 7

while(True):
    notas[0] = float(input("Digite sua nota: "))

    maior = notas[0]
    menor = notas[0]

    notas[1] = float(input("Digite sua nota: "))
    if(notas[1] > maior):
        maior = notas[1]
    if(notas[1] < menor):
        menor = notas[1]

    notas[2] = float(input("Digite sua nota: "))
    if(notas[2] > maior):
        maior = notas[2]
    if(notas[2] < menor):
        menor = notas[2]

    notas[3] = float(input("Digite sua nota: "))
    if(notas[3] > maior):
        maior = notas[3]
    if(notas[3] < menor):
        menor = notas[3]

    notas[4] = float(input("Digite sua nota: "))
    if(notas[4] > maior):
        maior = notas[4]
    if(notas[4] < menor):
        menor = notas[4]

    notas[5] = float(input("Digite sua nota: "))
    if(notas[5] > maior):
        maior = notas[5]
    if(notas[5] < menor):
        menor = notas[5]

    notas[6] = float(input("Digite sua nota: "))
    if(notas[6] > maior):
        maior = notas[6]
    if(notas[6] < menor):
        menor = notas[6]

    soma = notas[0] + notas[1] + notas[2] + notas[3] + notas[4] + notas[5] + notas[6] - menor - maior
    media = soma/5
    print(f"Notas descartas {maior} e {menor}" )
    print(f"Média: {media}")
    continuar = input("CONTINUAR?(S/N): ").upper()

