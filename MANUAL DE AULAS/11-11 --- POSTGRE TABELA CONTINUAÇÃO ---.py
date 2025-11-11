# AULA 11/11 - CONTINUAÇÃO POSTGRE

# Antes de tudo no prompt de comando escrever pip install psycopg2
import psycopg2

#PASSO 1: conectar no Banco de Dados
con = psycopg2.connect(
    host = "localhost",
    database = "algoritmos",
    user = "postgres",
    password = "postgres",
    port = 5432
)

#PASSO 2: obter o manipulador do dados
cursor = con.cursor()

#PASSO 3: definir comando SQL e dados (em datas use parenteses)
sql = """
    SELECT * FROM produtos 
    """

#PASSO 4: executar o comando SQL (salvar as coisas no banco de dados con.commit() em um SELECT * FROM produtos não precisa salvar)
#cursor.fetchall() me retorna a lista
cursor.execute(sql)

resultado = cursor.fetchall()

for linha in resultado:
    print("ID: ", linha[0])
    print("Nome: ", linha[1])
    print("Preço: ", linha[2])
    print("Data de Validade: ", linha[3])
    print("\n")

if(cursor.rowcount > 0):
    print("Registro inserido com sucesso!")
else:
    print("Um erro ocorreu e nada for inserido!")

####
import bibliotecas as bib

while(True):
    print("1. Cadastrar produto")
    print("2. Alterar produto")
    print("3. Excluir produto")
    print("4. Listar todos os produtos")
    print("5. Sair")
    opcao = int(input("OPÇÃO: "))

    if(opcao == 1):
        bib.cadastrar()
    if(opcao == 2)





    if(opcao == 5):
        break