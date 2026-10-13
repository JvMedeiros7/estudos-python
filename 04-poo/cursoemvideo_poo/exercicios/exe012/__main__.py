from rich import inspect
from salarios import Funcionario, Horista, Mensalista

def main():
    f1 = Horista("Paulo" , valor_hora = 12 , horas_trabalhadas = 200)
    f1.calcular_salario()
    f1.analisar_salario()


if __name__ == "__main__":
    main()