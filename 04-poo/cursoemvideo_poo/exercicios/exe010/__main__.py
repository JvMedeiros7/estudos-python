from rich import print
from rich.panel import Panel
from rich.traceback import install
from cafeteria import BebidaQuente, Cafe, Cha, Leite

install()

def main():
    bebida = Cafe("Café Expresso")
    bebida.preparar()

    bebida2 = Cha("Chá de Camomila")
    bebida2.preparar()

    bebida3 = Leite("Leite Quente")
    bebida3.preparar()

if __name__ == "__main__":
    main()