from rich import print
from rich.panel import Panel
from rich.traceback import install

install()

class Termostato:
    def __init__ (self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError("A temperatura deve ser incrementada de 0.5 em 0.5.")
        if valor < 16:
            valor = 16
        elif valor > 30:
            valor = 30
        self.__temperatura = valor

    @property
    def ftemperatura(self):
        return f"[bold blue] A tempera atual é: {self.__temperatura}°C [/bold blue]"

    

    