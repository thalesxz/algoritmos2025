import psycopg2
import bibliotecas as bib 
conexao = psycopg2.connect(
    host = "localhost", 
    database = "algoritmos",
    user = "postgres",
    password = "postgres",
    
)
cursor = conexao.cursor()
while(True):
    print("MENU DE LIVROS")
    print("1 - Incluir")
    print("2 - Alterar")
    print("3 - Excluir")
    print("4 - Sair")
    opcao = int(input("OPÇÃO: "))
    if(opcao == 1):
        bib.incluir()
    if(opcao == 2):
        print("")
