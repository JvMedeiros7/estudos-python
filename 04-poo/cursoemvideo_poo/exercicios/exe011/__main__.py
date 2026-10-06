from rich import print
from rich.panel import Panel
from rich.traceback import install
from rich.table import Table

install()

from transporte import Transporte, Caminhao, Moto, Drone

def main():
    dist = 55

    viagem = [Caminhao(dist), Moto(dist), Drone(dist)]

    tabela = Table(title="Tabela de Frete", show_header=True, header_style="bold magenta")
    tabela.add_column("Distância (km)", style="dim", width=12)
    tabela.add_column("Tipo", justify="right")
    tabela.add_column("Frete (R$)", justify="right")

    for item in viagem:
        tabela.add_row(f"{item.distancia}", f"{type(item).__name__}", f"{item.calcular_frete()}")

    print(tabela)

if __name__ == "__main__":
    main()