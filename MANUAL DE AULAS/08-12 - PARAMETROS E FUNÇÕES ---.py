#12/08 CONTEUDO P/ PROVA

#PARAMETROS = virgulas(,) separa um parametro.
#PROCEDIMENTOS = não tem retorno. (print)
#FUNÇÃO = tem retorno. (int, input)
#TODOS ELES TEM EM COMUM PARENTESES.

#Variavél toda maiúscula(ABC, PI, etc.) não pode ser mudada é constante sempre.
#CLASSE = primeira letra em maiúsculo(Abc)
#Primeira letra minúscula sempre variável.
#TRY e EXCEPT: tenta executar o try, se não der faz o codigo do Except, utiliza para testar o código sem dar erro.

import biblioteca as bib
# bib.ola()

# num = bib.inputInt("Digite um número: ")    
# num2 = bib.inputInt("Digite outro: ")
# print("Os números são:", num, "e",num2)

#EX1 (PEDIR 2 NUMEROS USAR FUNÇÃO APRESENTAR NA TELA) PARA ELES FACA A POTENCIA E A RAIZ E APRESENTE NA TELA
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro: "))

res = bib.somar2(num1, num2)
print(f"{num1} + {num2} = {res}")

potencia = bib.pot(num1, num2)
print(f"{num1} na potência {num2} = {potencia}")

raiz = bib.raiz(num1, num2)
print(f"{num1} na raiz {num2} = {raiz}")


#EX2 (PEDIR 3 NUMEROS USAR FUNCAO APRESENTAR NA TELA)




#EX3 (PEDIR VALOR E MOSTRAR SE É PAR OU IMPAR)