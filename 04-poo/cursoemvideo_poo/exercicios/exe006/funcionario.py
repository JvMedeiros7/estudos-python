from escola import Escola

class Funcionario(Escola):                              # SUBCLASSE - herda de Escola
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)                   # Reaproveita o construtor da SUPERCLASSE
        self.cargo = cargo                              # Atributos NOVOS, só de Funcionario
        self.setor = setor

    def bater_ponto(self):                              # Método NOVO, só Funcionario tem
        return f"{self.nome} bateu o ponto como {self.cargo} no setor {self.setor}."