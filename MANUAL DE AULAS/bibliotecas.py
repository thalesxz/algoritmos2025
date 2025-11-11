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


def cadastrar():
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
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    data = input("Data de validade: ")
    valores = [(f"{nome}"), (f"{preco}"), (f"{data}")]
    cursor.execute(sql, valores)
    con.commit()
    cursor.close()
    con.close()
    



def alterar():
    con = psycopg2.connect(
    host = "localhost",
    database = "algoritmos",
    user = "postgres",
    password = "postgres",
    port = 5432
    )
    cursor = con.cursor()
    id = int(input("Informe o id do produto que quer alterar: "))
    sql = """UPTADE produtos(nome, preco, data_validade)