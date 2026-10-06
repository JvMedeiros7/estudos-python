from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    def __init__(self, nome):
        self.nome = nome

    def iniciar_preparo(self):
        return f"\n--- Iniciando o preparo de {self.nome} ---\n"

    def ferver_agua(self):
        return "1. Fervendo água."

    def servir(self):
        return f"\n--- Bebida {self.nome} servida. Aproveite! ---\n"

    @abstractmethod
    def preparar(self):
        pass


class Cafe(BebidaQuente):
    def __init__(self, nome):
        super().__init__(nome)

    def preparar(self):
        print(self.iniciar_preparo())
        print(self.ferver_agua())
        print("2. Passando água presurizada pelo pó de café.")
        print("3. Servindo em xícara pequena.")
        print(self.servir())

    
class Cha(BebidaQuente):
    def __init__(self, nome):
        super().__init__(nome)

    def preparar(self):
        print(self.iniciar_preparo())
        print(self.ferver_agua())
        print("2. Mergulhando o sachê de ervas na água.")
        print("3. Servindo na caneca de porcelana com limão.")
        print(self.servir())    


class Leite(BebidaQuente):
    def __init__(self, nome):
        super().__init__(nome)

    def preparar(self):
        print(self.iniciar_preparo())
        print(self.ferver_agua())
        print("2. Adicionando leite à água fervida.")
        print("3. Servindo em copo grande.")
        print(self.servir())

