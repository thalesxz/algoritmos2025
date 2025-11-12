import psycopg2
def incluir():
    conexao = psycopg2.connect(
    host = "localhost", 
    database = "algoritmos",
    user = "postgres",
    password = "postgres",
    
    )
    cursor = conexao.cursor()

    sql = "insert into livros(titulo, autor, data_lancamento)" \
    " values(%s, %s, %s) RETURNING id"
    titulo = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    data_lancamento = input("Digite a data de lancamento(YY-MM-DD): ")
    data = data_lancamento.split("-")
    data_certa = (f"{data[2]}/{data[1]}/{data[0]}")
    valores = [(f"{titulo}"), (f"{autor}"), (f"{data_certa}")]
    cursor.execute(sql, valores)
    conexao.commit()


def cadastrar(nome, preco, data):
    con = psycopg2.connect(
        host = "localhost",
        database = "algoritmos",
        user = "postgres",
        password = "postgres",
        port = 5432
    )
    cursor = con.cursor()
    sql ="""INSERT INTO produtos(nome, preco, data_validade)"
    VALUES (%s, %s, %s)
    """
    valores = [(nome, preco, data)]
    cursor.execute(sql, valores)
    con.commit()

def alterar(id, nome, preco, data):
    con = psycopg2.connect(
    host = "localhost",
    database = "algoritmos",
    user = "postgres",
    password = "postgres",
    port = 5432
    )
    cursor = con.cursor()
    sql = """UPDATE produtos
    SET nome = %s, 
        valor= %s, 
        data_validade= %s
    WHERE id= %s ;
    """
    cursor.execute(sql)
    con.commit()

def excluir(id):
    con = psycopg2.connect(
    host = "localhost",
    database = "algoritmos",
    user = "postgres",
    password = "postgres",
    port = 5432
    )
    cursor = con.cursor()
    sql ="""DELATE FROM produtos(nome, preco, data_validade)"
    """
    valores = [(f"{nome}"), (f"{preco}"), (f"{data}")]
    cursor.execute(sql, valores)
    con.commit()
    cursor.close()
    con.close()