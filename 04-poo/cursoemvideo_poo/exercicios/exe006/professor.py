from escola import Escola

class Professor(Escola):                                # SUBCLASSE - herda de Escola
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)                   # Reaproveita o construtor da SUPERCLASSE
        self.especialidade = especialidade              # Atributos NOVOS, só de Professor
        self.nivel = nivel

    def dar_aula(self):                                 # Método NOVO, só Professor tem
        return f"{self.nome} está dando aula de {self.especialidade}, nível {self.nivel}."