from rich import print
from rich.panel import Panel
from rich.traceback import install
from abc import ABC, abstractmethod
from random import randint

install()

class Personagem(ABC):
    def __init__(self, nome: str, vida: int, golpes: int):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo: "Personagem"):
        dano = randint(0, self.golpes)
        alvo.vida -= dano
        # Mostra quanto de dano foi sorteado pelo randint neste golpe
        print(f"{self.nome} atacou {alvo.nome} e causou {dano} de dano!")
        if dano >= self.golpes * 0.8:  # Se o dano for maior ou igual a 80% do máximo de golpes
            print(f"[bold red]Golpe crítico![/bold red]")
        # Devolve o dano para quem chamou usar o valor (ex.: dano = heroi.atacar(vilao))
        return dano

    def receber_dano(self, dano: int):
        self.vida -= dano

    @abstractmethod
    def curar(self):
        pass

    def rodada(self, alvo: "Personagem"):
        # Roda até alguém ficar sem vida (antes o range(self.vida) fixava o nº de rodadas)
        i = 0
        while self.vida > 0 and alvo.vida > 0:
            i += 1
            print(f"Rodada {i}:")
            self.atacar(alvo)
            alvo.atacar(self)
            # Só cura quem ainda está vivo (curar usa metade da vida atual no randint)
            if self.vida > 0:
                self.curar()
            else:
                print(f"{self.nome} foi derrotado!")
            if alvo.vida > 0:
                alvo.curar()
            else:
                print(f"{alvo.nome} foi derrotado!")
            print(f"{self.nome} tem {self.vida} de vida restante.")
            print(f"{alvo.nome} tem {alvo.vida} de vida restante.")
            print("-" * 30)
    
class Guerreiro(Personagem):
    def curar(self):
        # Guarda o sorteio em uma variável (antes ele era somado direto na vida e se perdia).
        # max(1, ...) evita erro do randint quando a vida é 1 (1 // 2 = 0 -> randint(1, 0)).
        cura = randint(1, max(1, self.vida // 2))
        self.vida += cura
        # Mostra quanto de vida foi curado no sorteio
        print(f"{self.nome} se curou e recuperou {cura} de vida!")
        # Devolve o valor curado para quem chamou
        return cura

class Mago(Personagem):
    def curar(self):
        # Guarda o sorteio em uma variável (antes ele era somado direto na vida e se perdia).
        # max(1, ...) evita erro do randint quando a vida é 1 (1 // 2 = 0 -> randint(1, 0)).
        cura = randint(1, max(1, self.vida // 2))
        self.vida += cura
        # Mostra quanto de vida foi curado no sorteio
        print(f"{self.nome} se curou e recuperou {cura} de vida!")
        # Devolve o valor curado para quem chamou
        return cura
