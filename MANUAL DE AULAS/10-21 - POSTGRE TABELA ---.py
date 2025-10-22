#21/10 - AULA

# PGADMIN 4
# create table alunos(
# 	id serial,
# 	nome varchar(150),
# 	idade int
# ):


#ou 127.0.0.1 é a mesma coisa
#port = 5432 #posso e devo colocar caso eu use uma diferente da padrão! como usa-se a padrão não tem problema

import psycopg2
conexao = psycopg2.connect(
    host = "localhost", 
    database = "algoritmos",
    user = "postgres",
    password = "postgres",
    
)

# #dentro do banco de dados na conexao é o que manipula o banco de dados
# cursor = conexao.cursor()

# #comando para inserir valores no banco de dados
# #SQL = o comando a ser exectutado
# #VALORES = uma tupla os valores a serem subistituidos no comando
# sql = "insert into alunos(nome, idade)" \
#     " values(%s, %s) RETURNING id" 
# valores = [('Maria', 20),
#             ('Carlos', 30), 
#             ('José', 18)]

# #para executar o comando criado em cima com os valores que queremos tambem criados acima!
# cursor.executemany(sql, valores) 
# #para salvar/confirmar/autorizar a execução do comando pelo cursor
# conexao.commit() 


# #fechar o manipulador do banco de dados
# cursor.close()


# #para se fechar uma conexão, pois mexer com banco de dados ocorre após abrir e antes de fechar
# conexao.close()
