from rich import print
from rich.panel import Panel
from rich.traceback import install

install()

class Termostato:
    def __init__ (self, temperatura = 24.0):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 == 0 and 10 <= valor <= 30:
            self.__temperatura = valor
        else:
            raise ValueError("A temperatura deve estar entre 10 e 30 graus Celsius e ser incrementada de 0.5 em 0.5.")

    @property
    def ftemperatura(self):
        return f"[bold blue] {self.__temperatura}°C [/bold blue]"

    

    