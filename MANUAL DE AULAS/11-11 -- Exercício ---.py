import psycopg2
import bibliotecas as bib

"""
CADASTRO DE PRODUTOS
1. Cadastrar produto
2. Alterar produto
3. Excluir produto
4. Listar todos os produtos
5. Sair


Em 1: pedir pelos dados e incluir
Em 2: pedir pelo ID do produto e pelos novos dados e salvar
Em 3: pedir pelo nome do produto e excluir
Em 4: listar os produtos ordenados pelo nome

Se digitar uma opção inválida, informar ao usuário que a opção é inválida.
Repetir até que o usuário digite 5.

Banco de dados: mauricio
tabela: produtos
id: serial PK
nome: varchar(100)
valor: money
data_validade: date
"""


import psycopg2
import os

def menu():
    os.system("cls")
    print("""
CADASTRO DE PRODUTOS
1. Cadastrar produto
2. Alterar produto
3. Excluir produto
4. Listar todos os produtos
5. Sair""")
    opcao = int(input("OPÇÃO: "))
    return opcao

def cadastrar(nome, valor, data):
    sql = """
    INSERT INTO produtos (nome, valor, data_validade)
    VALUES (%s, %s, %s)
    """
    valores = (nome, valor, data)
    cursor.execute(sql, valores) 
    con.commit()
    return cursor.rowcount

def alterar(id, nome, valor, data):
    sql = """
    UPDATE produtos 
    SET nome=%s, valor=%s, data_validade=%s
    WHERE id=%s
    """
    valores = (nome, valor, data, id)
    cursor.execute(sql, valores) 
    con.commit()
    return cursor.rowcount

def excluir(id):
    sql = """
    DELETE FROM produtos 
    WHERE id=%s
    """
    valores = (id, )  #se tiver só um valor, colocar ,
    cursor.execute(sql, valores) 
    con.commit()
    return cursor.rowcount

def listar():
    sql = """
    SELECT * FROM produtos ORDER BY nome
    """
    cursor.execute(sql) 
    resultado = cursor.fetchall()
    return resultado

con = psycopg2.connect(
    host = "localhost",
    database = "mauricio",
    user = "postgres",
    password = "postgres",
    port = 5432    
)
cursor = con.cursor()


while(True):
    opcao = menu()
    if(opcao == 1):
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        data = input("Data de validade: ")
        total = cadastrar(nome, preco, data) 
        print()
        if(total > 0):
            print("Cadastrado com sucesso!")
        else:
            print("Erro ao cadastrar.") 
        input("Pressione uma tecla para continuar.")
    elif(opcao == 2):
        id = int(input("Código do produto a ser alterado: "))
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        data = input("Data de validade: ")
        total = alterar(id, nome, preco, data) 
        print()
        if(total > 0):
            print("Alterado com sucesso!")
        else:
            print("Erro ao alterar.") 
        input("Pressione uma tecla para continuar.") 
    elif(opcao == 3):
        id = int(input("Código do produto a ser excluído: "))
        total = excluir(id)
        print()
        if(total > 0):
            print("Excluído com sucesso!")
        else:
            print("Erro ao excluir.") 
        input("Pressione uma tecla para continuar.")  
    elif(opcao == 4):
        print()
        resultado = listar() 
        for linha in resultado:
            print(f"{linha[0]}: {linha[1]}")
            print(f"Preço: {linha[2]}")
            print(f"Data de Validade: {linha[3]}")
            print()
        input("Pressione uma tecla para continuar.")  
    elif(opcao == 5):
        print("Obrigado por usar nosso sistema!")
        break 
    else:
        print("\nOpção inválida. Tente novamente")
        input("Pressione uma tecla para continuar.")
    print()
con.close()
cursor.close()