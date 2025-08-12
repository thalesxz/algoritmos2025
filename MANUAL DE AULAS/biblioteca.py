def ola():
    print("Olá, Bem Vindo!")
    if(True):
        print("Função Válida")
    else:
        print("Erro")

def inputInt():
    x = input("Digite um número: ")
    try:
        x = int(x)
    except:
        print("Valor informado é inválido!")
        x = inputInt()
    return x

def pedirFloat():
    while(True):
        try:
            x = float(input("Número: "))
            break
        except:
            print("Float inválido!")
    return x
        