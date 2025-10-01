# MANIPULAÇÃO DE ARQUIVOS -- 30/09/25
 #Escrita e Leitura de arquivos
    # 3 MODOS de trabalhar com arquivo
    # R = leitura(lê o que tem no arquivo, não modifica)
    # W = escrita(escreve no arquivo, quando abre ele apaga tudo e comeca em branco, cria o arquivo se não tiver) (guardar coisas rápidas)
    # A = escrita(acrescentar coisas no arquivo, quando abre mantem tudo e começa o cursor no final, cria o arquivo se não tiver)

#modo de arbertura do arquivo
  # tem que ser igual r não pode usar o write e sim read
arquivo = open("dados.txt", "a", encoding="utf8") #nos parênteses = 1° nome do arquivo em aspas, 2° o modo em aspas(r,w,a), 3° se quiser conjunto de caracteres enconding = "utf8"
# para abrir um arquivo que não está localizado junto usar o endereço completo primeiro do nome do arquivo
# com mais 1 contra barra no lugar onde tem contra barra EX: open("\\Users\\Aluno\\Downloads\\algoritmos2025\\dados.txt", "r")


#váriavel para usar na função write
texto = 10
nome = input("Digite seu nome: ")

#função write escreve no arquivo uma string
arquivo.write(f"{nome}\n") #só aceia string e um parámetro por vez, se quiser por número utiliza aspas no número ou cria uma váriavel que armazena número ou string formatada
                           #colocar \n para pular a linha caso esteja no modo A

# lê todas as linhas e gurda o conteúdo dentro de uma váriavel
conteudo = arquivo.readlines()

# exibe na tela o conteúdo lido
print(conteudo)

#sempre fechar o arquivo, caso 2 ou mais pessoas abrir pode dar erro/problema
arquivo.close()

#Quantas linhas tem o arquivo?
qtde = len(conteudo)
print(f"O arquivo tem {qtde} linhas")

#Percorre a lista de strings com o conteúdo
for i in range(0, len(conteudo)):
    print(conteudo[i], end="") # o end = "" serve para nao quebrar linha ja que ta quebrando no arquivo


