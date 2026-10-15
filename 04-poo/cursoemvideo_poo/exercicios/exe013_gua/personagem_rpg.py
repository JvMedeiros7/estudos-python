import random
from rich import print
from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome 
        self.vida = vida
        self.golpes = []
        

    def atacar(self, alvo, forca = 100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]

            print(f"[green]{self.nome}[/green] atacou [red]{alvo.nome}[/red] com o golpe [blue]{golpe}[/blue] causando [red]{forca} [/red] de dano.")
            alvo.receber_dano(forca)

        else:
            print(f" O ataque {self.nome} -> {alvo.nome} não pode acontecer neste momento.")

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida = self.vida - fator
        if self.vida < 0:
            self.vida = 0
            print(f"{self.nome} morreu!")
        print(f"{self.nome} recebeu {fator} de dano e agora tem {self.vida} de vida.")
        

    @abstractmethod
    def curar(self):
        pass    

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Golpe de Machado" , "Pulo Giratório"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida = self.vida + fator
        print(f"{self.nome} usou uma atadura e recuperou {fator} pontos de vida \n[bold red]HP: {self.vida} [/bold red]")

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de fogo", "Raio de Luz" , "Mágia estática"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida = self.vida + fator
        print(f"{self.nome} usou uma mágia e curou  {fator} pontos de vida! \n[bold green]HP: {self.vida} [/bold green]")


