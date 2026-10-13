from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome,sal_bruto, salario, sal_min = 1612, inss = 7.5):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = sal_min
        self.inss = inss

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        if self.salario < self.sal_min:
            return f"O salário do funcionário {self.nome} está abaixo do salário mínimo."
        else:
            return f"O salário do funcionário {self.nome} está acima do salário mínimo."


class Horista(Funcionario):
    def __init__(self, nome, sal_bruto, salario, sal_min = 1612, inss = 7.5, horas_trabalhadas = 0, valor_hora = 0):
        super().__init__(nome, sal_bruto, salario, sal_min, inss)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * (self.inss / 100))
        return f"O salário do funcionário {self.nome} é de R${self.salario:.2f}."

    
class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto, salario, sal_min = 1612, inss = 7.5):
        super().__init__(nome, sal_bruto, salario, sal_min, inss)

    def calcular_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * (self.inss / 100))
        return f"O salário do funcionário {self.nome} é de R${self.salario:.2f}."