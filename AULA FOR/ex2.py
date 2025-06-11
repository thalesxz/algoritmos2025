numero = int(input("Digite um número para tabuada: "))
X = int(input("Digite um número para inicio da tabuada(X): "))
Y = int(input("Digite um número para final da tabuada(Y): "))
while(X > Y):
    if(X > Y):
        print("O valor de X não poder ser menor que o de Y.")
        X = int(input("Digite um número para inicio da tabuada(X): "))
        Y = int(input("Digite um número para final da tabuada(Y): "))
for i in range (X, Y+1):
    if(X >= Y):
        print("O valor de X não poder ser menor que o de Y.")
    print(f"{i} x {numero} = {i*numero}")