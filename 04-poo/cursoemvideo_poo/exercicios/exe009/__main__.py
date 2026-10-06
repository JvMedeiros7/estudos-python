from rich import print
from rich.panel import Panel
from rich.traceback import install
from poligono import Poligono, Quadrado, Circulo

install()

def main():
    p1 = Quadrado(12)
    
    print(f"Perímetro do círculo: {p1.perimetro():.1f}")
    print(f"Área do círculo: {p1.area():.1f}")


if __name__ == "__main__":
    main()