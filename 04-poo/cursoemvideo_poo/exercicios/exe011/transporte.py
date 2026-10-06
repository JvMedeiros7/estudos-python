from abc import ABC, abstractmethod

@abstractmethod
class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia

    @abstractmethod
    def calcular_frete(self):
        pass

class Caminhao(Transporte):
    def calcular_frete(self):
        if self.distancia >= 50:
            calc = self.distancia * 1.20
            return f"O frete do transporte Caminhão é de R${calc:.2f}."
        else:
            return f"O frete do transporte Caminhão não pode ser calculado, pois a distância percorrida é menor que 50 km."

class Moto(Transporte):
    def calcular_frete(self):
            calc = self.distancia * 0.50
            return f"O frete do transporte de Moto é de R${calc:.2f}."

class Drone(Transporte):
    def calcular_frete(self):
            if self.distancia <= 10:
                calc = self.distancia * 9.50
                return f"O frete do transporte de Drone é de R${calc:.2f}."
            else:
                return f"O frete do transporte de Drone não pode ser calculado, pois a distância percorrida é maior que 10 km."




        
