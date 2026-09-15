from rich import print
from rich.panel import Panel
from rich.traceback import install

install()

# ============================================================
#  EXEMPLO - Uma SUPERCLASSE, várias SUBCLASSES (Escola)
# ============================================================
# Aqui a generalização fica clara: Aluno, Professor e Funcionario têm
# nome e idade em comum -> isso sobe para a superclasse Escola.
# Cada subclasse adiciona o que é SÓ dela (especialização).
#
#                        Escola             <- SUPERCLASSE (genérica)
#                   /       |        \
#              Aluno    Professor   Funcionario   <- SUBCLASSES (específicas)

# Criando objetos a partir das SUBCLASSES


class Escola:                                           # SUPERCLASSE (classe pai) - o que é comum a todos
    def __init__(self, nome, idade):                    # Construtor da superclasse
        self.nome = nome                                # Atributos que TODAS as subclasses vão HERDAR
        self.idade = idade

    def fazer_aniversario(self):                        # Método definido SÓ aqui...
        self.idade += 1                                 # ...mas Aluno, Professor e Funcionario podem usar
        return f"{self.nome} agora tem {self.idade} anos."


class Aluno(Escola):                                    # SUBCLASSE - o "(Escola)" é a HERANÇA
    def __init__(self, nome, idade, curso, turma):      # Recebe os do pai (nome, idade) + os próprios (curso, turma)
        super().__init__(nome, idade)                   # super() chama o __init__ da SUPERCLASSE -> cria nome e idade
        self.curso = curso                              # Atributos NOVOS, existem só em Aluno (especialização)
        self.turma = turma

    def matricular(self):                               # Método NOVO, só Aluno tem
        return f"{self.nome} foi matriculado no curso de {self.curso}, turma {self.turma}."


class Professor(Escola):                                # SUBCLASSE - herda de Escola
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)                   # Reaproveita o construtor da SUPERCLASSE
        self.especialidade = especialidade              # Atributos NOVOS, só de Professor
        self.nivel = nivel

    def dar_aula(self):                                 # Método NOVO, só Professor tem
        return f"{self.nome} está dando aula de {self.especialidade}, nível {self.nivel}."


class Funcionario(Escola):                              # SUBCLASSE - herda de Escola
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)                   # Reaproveita o construtor da SUPERCLASSE
        self.cargo = cargo                              # Atributos NOVOS, só de Funcionario
        self.setor = setor

    def bater_ponto(self):                              # Método NOVO, só Funcionario tem
        return f"{self.nome} bateu o ponto como {self.cargo} no setor {self.setor}."
