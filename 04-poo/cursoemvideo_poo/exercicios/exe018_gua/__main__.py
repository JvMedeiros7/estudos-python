from rich import print, inspect
from classes018 import Diario

def main():

    d = Diario()
    d.escrever("Este é um segredo.")
    d.escrever("Outro segredo.")

    try:
        d.ler("CeV!@")
    except PermissionError as e:
        print(f"[red]Erro: {e}[/red]")
    

if __name__ == "__main__":
    main()

