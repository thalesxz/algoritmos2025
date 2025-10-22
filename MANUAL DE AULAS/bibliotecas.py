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
