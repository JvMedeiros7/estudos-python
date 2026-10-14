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
        self.golpes = golpes

    def atacar(self, alvo: "Personagem"):
        dano = randint(0, self.golpes)
        alvo.vida -= dano

    def receber_dano(self, dano: int):
        self.vida -= dano

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def curar(self):
        self.vida += randint(1, 100)

class Mago(Personagem):
    def curar(self):
        self.vida += randint(1, 100)