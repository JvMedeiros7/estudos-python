from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calcular_frete(self):
        pass

class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        self.frete = self.distancia * self.fator
        return f"O frete do transporte de Moto é de R${self.frete:.2f}."

class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia >= 50:
            self.frete = self.distancia * 1.20
            return f"O frete do transporte Caminhão é de R${self.frete:.2f}."
        else:
            return f"O frete do transporte Caminhão não pode ser calculado, pois a distância percorrida é menor que 50 km."

class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia >= 50:
            self.frete = self.distancia * 1.20
            return f"O frete do transporte Caminhão é de R${self.frete:.2f}."
        else:
            return f"O frete do transporte Caminhão não pode ser calculado, pois a distância percorrida é menor que 50 km."


class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia >= 50:
            self.frete = self.distancia * 1.20
            return f"O frete do transporte Caminhão é de R${self.frete:.2f}."
        else:
            return f"O frete do transporte Caminhão não pode ser calculado, pois a distância percorrida é menor que 50 km."


dist = 50
entrega = Moto(dist)
print(f"Frete de {type(entrega).__name__} para {entrega.distancia} km: {entrega.calcular_frete()}")

entrega2 = Caminhao(dist)
print(f"Frete de {type(entrega2).__name__} para {entrega.distancia} km: {entrega2.calcular_frete()}")