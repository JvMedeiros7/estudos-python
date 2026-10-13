from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
from rich.traceback import install
from rich.console import Console


install()

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
        # Quantos salários mínimos o salário líquido representa
        analise_sal = self.salario / self.sal_min
        # Monta o texto completo (salário + análise) em uma única string
        texto = (f"O salário do funcionário {self.nome} é de R${self.salario:.2f}\n"
                 f"e corresponde a {analise_sal:.1f} salários mínimos.")
        # print do rich (importado acima) renderiza o Panel; expand=False ajusta ao texto
        print(Panel(texto, title="Cálculo de Salário", expand=False))


class Horista(Funcionario):
    def __init__(self, nome, horas_trabalhadas = 0, valor_hora = 0):
        super().__init__(nome, sal_bruto = 0, salario = 0)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
        self.sal_bruto = self.horas_trabalhadas * self.valor_hora

    def calcular_salario(self):
        # Salário líquido = bruto - desconto do INSS (apenas calcula, quem imprime é analisar_salario)
        self.salario = self.sal_bruto - (self.sal_bruto * (self.inss / 100))


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto, sal_min = 1612, inss = 7.5):
        super().__init__(nome, sal_bruto, salario = 0, sal_min = sal_min, inss = inss)

    def calcular_salario(self):
        # Mesmo cálculo do Horista: bruto - INSS
        self.salario = self.sal_bruto - (self.sal_bruto * (self.inss / 100))

