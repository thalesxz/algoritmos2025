import math
import random
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
    
def numerosaleatorios(x: int):
    x = 0
    while(x <= 1):
        x = int(input("Digite um número maior que 1: "))      
        if(x <= 1):
            print("Número Inválido!")
    aleatorio = random.randint(1, x)
    return aleatorio

def sorteiopar(min: int, max: int):
    if(min > max):
        a = max 
        max = min
        min = a
    resultado = random.randint(min, max)
    while(resultado % 2 != 0):
        resultado = random.randint(min, max)
    return resultado

def sorteiosimpar(min: int, max: int):
    if(min > max):
        a = max 
        max = min
        min = a
    resultado = random.randint(min, max)
    while(resultado % 2 == 0):
        resultado = random.randint(min, max)
    return resultado

def mes(x: int):
    meses = ["Janeiro" , "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    if(x >= 1 and x <= 12):
        return meses[x - 1]
    else:
        print("Mês inválido")

def areaquadrado(x: int):
    resultado = math.pow(x, 2)
    return resultado

def arearetangulo(x: int, y: int):
    resultado = x * y
    return resultado

def areatriangulo(x: int, y:int):
    resultado = (x * y) / 2
    return resultado

def areatrapezio(x: int,  y:int, z:int):
    resultado = ((x + y)  * z)/ 2
    return resultado

def fatorial(x:int):
    resultado = x
    for i in range(x-1, 0, -1):
        resultado *= i
    return resultado

def maiorvetor(vetor):
    maior = vetor[0]
    for i in range(1, len(vetor)):
        if(vetor[i] > maior):
            maior = vetor[i]
    return maior