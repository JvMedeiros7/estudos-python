from escola import Escola


class Aluno(Escola):                                    # SUBCLASSE - o "(Escola)" é a HERANÇA
    def __init__(self, nome, idade, curso, turma):      # Recebe os do pai (nome, idade) + os próprios (curso, turma)
        super().__init__(nome, idade)                   # super() chama o __init__ da SUPERCLASSE -> cria nome e idade
        self.curso = curso                              # Atributos NOVOS, existem só em Aluno (especialização)
        self.turma = turma

    def matricular(self):                               # Método NOVO, só Aluno tem
        return f"{self.nome} foi matriculado no curso de {self.curso}, turma {self.turma}."