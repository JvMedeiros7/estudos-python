from personagem_rpg import Personagem, Guerreiro, Mago
from rich import inspect

def main():
    p1 = Guerreiro("Pikanocu", 1000)
    p2 = Mago("Alakacu", 1000)

    p1.atacar(p2, 200)
    p2.atacar(p1, 100)

    p1.curar()
    p2.curar()

if __name__ == "__main__":
    main()  