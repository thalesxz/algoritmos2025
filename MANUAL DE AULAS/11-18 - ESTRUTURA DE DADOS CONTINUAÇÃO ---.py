# 18/11/25 - 4 NOVAS ESTRUTURAS DE DADOS (aula passada CLASSES)
# DADO: valor qualquer
# ESTRUTURA DE DADOS: como organizar ou armazenar os dados no computador

#ESTRUTURA DE DADOS HOMOGENEAS
    # VETOR: uma dimensão, conjunto de dados, todos os valores tem que ser do mesmo tipo, tamanho fixo. 

    # MATRIZ: vetor bidimensional, todos os valores tem que ser do mesmo tipo e mesmo tamanho.
    #EX: 

linhas = 3
colunas = 4
matriz = [0] * linhas
for i in range(0, linhas):
    matriz[i] = [0] * colunas
matriz[1][2] = 5  #obs: seria na 1 linha e 2 coluna add


#ESTRUTURA DE DADOS HETEROGENEAS

    #CLASSES: tamanho váriavel, pode ter varias váriaves dentro e tipos diferentes.
    #EX: classe Disciplina(id: int, nome: string, ch: int, professor: string) METÓDO: __init__(self)

class Disciplina:
    def __init__(self):
        self.id = 0
        self.nome = ""
        self.ch = 0
        self.professor = ""

#OBJETO(instancia de uma classe):
d1 = Disciplina()
d1.nome = "Algoritmos"

d2= Disciplina()
d2.nome = "Engenharia de Software"

    #LIST(usamos em vetor): tamanho váriavel, pode ter valores de tipos diferentes.

lista = []
lista.append(5) #insere no fim
lista.append("Aula") 
lista.append(80.2)

lista.insert(1, "oi") # insere a váriavel "oi" no indice 1 e manda a outras("Aula", 80.2) variável pra frente (indice 2 e 3)


lista.pop(2) # exclui o valor do indice 2 e os valores da frente voltam para trás

lista.remove(80.2) # remove o primeiro valor(se tiver 3 váriaveis iguais remove a 1°)

lista.clear() #limpa toda a lista

#EX:
convidado = []
for i in range(0, 6):
    nome = input("Informe o seu nome: ")
    convidado.append(nome)

excluir = input("Nome para ser deletado: ")
convidado.remove(excluir)

for i in range(0, len(convidado)):
    print(lista[i])


    #TUPLA(usa parénteses() no lugar de []): são imutáveis, valores não podem ser alterados depois de criar, CRIAR com TUDO 
    #EX:

nome = input("Nome do produto: ")
preco = float(input("Valor produto: "))
quantidade = int(input("Quantidade do produto em estoque: "))

produto = (nome, preco, quantidade)
for i in range(0, len(produto)):
    print(produto[i])

# print(f"O tamanho da tupla é {len(produto)}")


    #CONJUNTOS(usar chaves{}) = valores não está em ordem de escrita, PODE INSERIR e REMOVER valor porém NÃO pode ALTERAR os valores
    #não consegue acessar os valores so usa em operações, não repete valores
a = set()
a = {1, 2, 5}

a.add(7) #inclui valores no conjunto

b = {7, 4, 8, 10, 2, 35.5}

uni = a.union(b) #UNIÃO A por B
inter = a.intersection(b) #INTERSEÇÃO A por B
difA = a - b #DIFERENÇA de A por B

x = {1, 2}
subc = x.issubset(a) # X está contido(subconjutno) em A (se sim True, se não False)
pert = 8 in b # 8 pertence em b (se sim True, se não False)

a.remove(1) # remove o valor do conjunto
    #EX:

turma_a = set({'Ana', 'Beto', 'Carlos', 'Duda'}) #set transforma conjunto em lista
turma_b = set({'Carlos', 'Edu', 'Fernanda', 'Ana'}) 

intersecao = set(turma_a.intersection(turma_b))
difeA = set(turma_a - turma_b)
uniao = set(turma_a.union(turma_b))
    
print(intersecao)
print(difeA)
print(uniao)

    #DICIONÁRIOS: armazenam valores em pares( CHAVE: indice do vetor nomeado, VALOR: valor armazenado na chave) tipos dados diferentes.
    # pode ter conjunto(set) e list, chaves vazias são dicionários, NÃO TEM METODÓS

pessoa = {
    "nome": "Alberto",
    "idade": 35,
    "filhos": {"Pedro", "Maria"},
    "formacao" : ["Informática", "Engenharia de Software"],
    "profissao" : {
        "empresa": "Google",
        "cargo": "Desenvolvedor"
        }
    }

print( pessoa["nome"] )
print( pessoa["filhos"] )
print( pessoa["formacao"][1] )
print( pessoa["profissao"]["empresa"] )

pessoa["Nova chave"] = "valor" # adicionar valores no dicionário
pessoa.pop["chave"] #  remover valores no dicionário

# para percorrer todas as chaves e valores do dicionário
for chave, valor in pessoa.items():
    print(chave)
    print(valor)

aluno = { 
    "nome" : "Thales",
    "idade" : 18,
    "curso" : "Engenharia de Software"
}

for chave, valor in aluno.items():
    print(f"{chave} : {valor}")

aluno["idade"] = "19"
aluno["nota"] = "75"
aluno.pop("curso")

for chave, valor in aluno.items():
    print(f"{chave} : {valor}")