# 26/08 estudo prova
import biblioteca as bib
# opcao = 0
# while(opcao != 6):
#     print("1. Soma")
#     print("2. Multiplicação")
#     print("3. Raiz")
#     print("4. Tabuada")
#     print("5. Potencia")
#     print("6. Sair")
#     opcao = int(input("OPÇÃO: "))
#     if(opcao == 1):
#         num1 = int(input("Digite um número: "))
#         num2 = int(input("Digite outro número: "))
#         print(f"A soma do número {num1} e {num2} é {bib.somar2(num1, num2)} ")
#     if(opcao == 2):
#         num1 = int(input("Digite um número: "))
#         num2 = int(input("Digite outro número: "))
#         print(f"A multiplicação do número {num1} e {num2} é {bib.multiplicar(num1, num2)} ")
#     if(opcao == 3):
#         num1 = int(input("Digite um número: "))
#         print(f"A raiz do número {num1} é {bib.raizquadrada(num1)}")
#     if(opcao == 4):
#         num1 = int(input("Digite um número: "))
#         print(bib.calculartabuada(num1))
#     if(opcao == 5):
#         num1 = int(input("Digite um número para base: "))
#         num2 = int(input("Digite outro número para potencia: "))
#         print(f"O número {num1} elevado a {num2} é {bib.pot(num1, num2)}")

# numeros = [0] * 6
# for i in range(0, len(numeros)):
#     numeros[i] = int(input(f"Digite o {i + 1} valor: "))
# bib.imprimerVetor(numeros)
# print(f"Maior valor: {bib.maiorvetor(numeros)}")
# print(f"Menor valor: {bib.menorvetor(numeros)}")

vetor1 = [1, 2, 3, 5]
vetor2 = [4, 5, 6, 2]
print(bib.multiplicar_vetores(vetor1, vetor2))