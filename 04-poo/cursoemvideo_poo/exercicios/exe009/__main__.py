from rich import print
from rich.panel import Panel
from rich.traceback import install
from poligono import Poligono, Quadrado, Circulo

install()

def main():
    p1 = Circulo(20)
    
    print(f"Perímetro do círculo: {p1.perimetro()}")
    print(f"Área do círculo: {p1.area()}")


if __name__ == "__main__":
    main()