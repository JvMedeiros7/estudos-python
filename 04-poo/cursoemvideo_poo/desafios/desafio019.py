from rich import print
from rich.panel import Panel

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.paginas_atual = 1

        print(Panel(f"[bold cyan]Livro '{self.titulo}' criado com sucesso![/bold cyan]\nTotal de páginas: [bold yellow]{self.paginas}[/bold yellow]\nVocê está na página: [bold green]{self.paginas_atual}[/bold green]", title="[bold green]Informações do Livro[/bold green]", border_style="green"))

    def avancar_paginas(self, quantidade):
        if self.paginas_atual + quantidade > self.paginas:
            print(Panel(f"[bold red]Você não pode avançar {quantidade} páginas. O livro tem apenas {self.paginas} páginas.[/bold red]", title="[bold red]Erro[/bold red]", border_style="red"))
        else:
            inicio = self.paginas_atual  # guarda a página em que você está antes de somar
            self.paginas_atual += quantidade  # o estado que persiste entre chamadas fica em self, não em variável local
            for pagina in range(inicio, self.paginas_atual):  # percorre exatamente as páginas lidas (ex.: 1→4 imprime 1, 2, 3)
                print(f"Você leu a página {pagina}...")
            print(Panel(f"[bold green]Você avançou {quantidade} páginas. Agora você está na página {self.paginas_atual}.[/bold green]", title="[bold green]Avanço de Páginas[/bold green]", border_style="green"))

    def avanco(self):
        while True:
            try:
                quantidade = int(input("Quantas páginas você quer avançar? "))
                if quantidade == 00:
                    break
                l1.avancar_paginas(quantidade)
            except ValueError:
                print(Panel("[bold red]Por favor, insira um número válido.[/bold red]", title="[bold red]Erro[/bold red]", border_style="red"))
            if self.paginas_atual == self.paginas:
                print(Panel(f"[bold green]Parabéns! Você terminou de ler o livro '{self.titulo}'![/bold green]", title="[bold green]Fim do Livro[/bold green]", border_style="green"))
                break


l1 = Livro("O Senhor dos Anéis", 1000)
l1.avanco()



