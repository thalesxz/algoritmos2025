# 11/11/2025 --- 2° AULA 
# ESTRUTURA DE DADOS HETEROGENEAS
# Toda classe é uma representação, novo tipo de dado definido programador

class Data:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.ano = 0

class Aluno:
    def __init__(self):
        self.data_nasc = Data()
        self.nome = ""
        self.idade = 0
        self.curso = "ES"
        self.conceitos = [""] * 3

alu1 = Aluno()
alu1.data_nasc.dia = 19
alu1.nome = "Ayslan"
alu1.idade = int(input("Informe sua idade: "))
alu1.conceitos[0] = 'A'

class Ventilador:
    def __init__(self):
        self.marca = ""
        self.voltagem = 0
        self.numero_velocidades = 0
        self.velocidade_atual = 0
def aumentarVelocidade(ventilador):
    if(ventilador.velocidade_atual < ventilador.numero_velocidades):
        ventilador.velocidade_atual += 1

vent = Ventilador()
vent.marca = "Delta Premium"
vent.voltagem = 110
vent.numero_velocidades = 4
vent.velocidade_atual = 0

aumentarVelocidade(vent)