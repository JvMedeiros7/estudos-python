from rich.panel import Panel
from rich.align import Align
from rich import print  

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}"

    def __rich__(self):
        return str(self)

    def etiqueta(self):
        return Panel(
            Align.center(f"{f' {self.nome} ':.^36}\n{f' {self.preco} ':-^36}"),
            title="Etiqueta do Produto",
            style="bold green",
            width=40,
            subtitle="Informações do Produto",
            title_align="center",
            subtitle_align="center",
        )

produto1 = Produto("Camiseta", 49.90)
print(produto1.etiqueta())