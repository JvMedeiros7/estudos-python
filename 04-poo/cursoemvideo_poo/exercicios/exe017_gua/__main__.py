from termostato import Termostato
from rich import inspect, print

def main():
    t = Termostato()
    try:
        escolha = float(input("Digite a temperatura desejada (entre 10 e 30 graus Celsius, incrementos de 0.5): "))
        t.temperatura = escolha 
        print(f"[bold red]Temperatura atual: {t.ftemperatura}[/bold red]")
    except Exception as e:
        print(f"[bold red]Erro: {e}[/bold red]")
        print(f"[bold red]Temperatura atual: {t.ftemperatura}[/bold red]")


if __name__ == "__main__":
    main()