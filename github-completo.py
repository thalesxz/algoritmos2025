import os
email = "thalesmauriciojodar@gmail.com"
print(f"Seu email é: {email}")
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