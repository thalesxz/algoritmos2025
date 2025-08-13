import math
def ola():
    print("Olá, Bem Vindo!")
    if(True):
        print("Função Válida")
    else:
        print("Erro")

def inputInt(msg:str): #Parametro tem que ser uma string
    x = input(f"{msg}")
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


def somar2(num1: int, num2:int):
    soma = num1 + num2 
    return soma

def somar3(num1: int, num2: int, num3:int):
    soma = num1 + num2 + num3
    return soma

def pot(v1:int,potencia:int):
    resultado = v1 ** potencia
    return resultado


def raiz(valor:float, grau:int):
    resultado = valor ** (1/grau)
    return resultado

def multiplicar(v1: int, v2: int):
    mult = v1 * v2
    return mult

def ePar(v1: int):
    if(v1 % 2 == 0):
        return True
    else:
        return False