from abc import ABC, abstractmethod

class Poligono(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class Circulo(Poligono):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14159 * (self.raio ** 2)

    def perimetro(self):
        return 2 * 3.14159 * self.raio