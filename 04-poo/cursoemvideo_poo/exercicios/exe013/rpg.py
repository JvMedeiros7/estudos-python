from rich import print
from rich.panel import Panel
from rich.traceback import install
from abc import ABC, abstractmethod
from random import randint

install()

class Personagem(ABC):
    def __init__(self, nome: str, vida: int, golpes: ):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes

def atacar(self, alvo: "Personagem"):