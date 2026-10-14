from rich import print
from rich.panel import Panel
from rich.traceback import install

install()
from rpg import Personagem, Guerreiro, Mago

def main():
    guerreiro = Guerreiro("Asta", 80, 60)
    mago = Mago("Frieren", 150, 30)

    guerreiro.rodada(mago)


if __name__ == "__main__":
    main()