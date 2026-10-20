from termostato import Termostato
from rich import inspect, print

def main():
    t = Termostato()
    escolha = float(input("Digite a temperatura desejada (entre 10 e 30 graus Celsius, incrementos de 0.5): "))
    t.temperatura = escolha 
    print(f"[bold red]Temperatura atual: {t.ftemperatura}[/bold red]")

    #print(t.ftemperatura)
    #inspect(t, private=True, methods=True, help=True)

if __name__ == "__main__":
    main()