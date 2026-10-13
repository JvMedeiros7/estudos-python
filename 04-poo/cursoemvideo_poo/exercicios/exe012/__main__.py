from rich import inspect
from salarios import Funcionario, Horista, Mensalista

def main():
    # Horista: 200 horas a R$12 por hora
    f1 = Horista("Paulo" , valor_hora = 12 , horas_trabalhadas = 200)
    # Primeiro calcula o salário líquido (preenche self.salario)
    f1.calcular_salario()
    # Depois analisa e imprime tudo dentro do Panel
    f1.analisar_salario()

    # Mensalista: salário bruto de R$9000
    f2 = Mensalista("Amanda", sal_bruto = 9000)
    # Primeiro calcula o salário líquido (preenche self.salario)
    f2.calcular_salario()
    # Depois analisa e imprime tudo dentro do Panel
    f2.analisar_salario()


if __name__ == "__main__":
    main()