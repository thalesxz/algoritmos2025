import os
tamanho = 0
while(tamanho <= 5):
    nome = input("Informe seu nome para email(até o @): ")
    tamanho = len(nome)
    if(tamanho <= 5):
        print("Informe um nome maior que 5 caracteres.")

opc1 = print("1 - @ifpr.edu.br")
opc2 = print("2 - @gmail.com")
opc3 = print("3 - @hotmail.com")
opc4 = print("4 - Outro")
opcao = int(input("\nOPÇÃO: "))

if(opcao == 1):
    opc1 = "@ifpr.edu.br"
    email = nome + opc1
    print("Seu EMAIL é: " , email)
elif(opcao == 2):
    opc2 = "@gmail.com"
    email = nome + opc2
    print("Seu EMAIL é: " , email)
elif(opcao == 3):
    opc3 = " @hotmail.com"
    email = nome + opc3
    print("Seu EMAIL é: " , email)
elif(opcao == 4):
    opc4 = input("Me informe o @ do destino de email: ")
    while(not(".com" in opc4 and "@" in opc4)):
        opc4 = input("Me informe o @ do destino de email (utilizando .com e @): ")
        email = nome + opc4
    print("Seu EMAIL é: " , email)
else:
    print("Opção inválida!!!!")

commit = input("Qual é a sua mensagem para o commit: ")
while(len(commit) <= 10):
    print("Detalhe mais a sua mensagem ela está muito pequena.")
    commit = input("\nQual é a sua mensagem para o commit: ")

#Configurar email
c = f"git config user.email \"{email}\""
os.system(c)

#Indentificar as novidades e incluir no commit
c = f"git add * "
os.system(c)

#Registrar o commit com uma mensagem
c = f"git commit -m \"{commit}\" "
os.system(c)

#Enviar para os servidores do GitHub
c = "git push"
os.system(c)