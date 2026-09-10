from rich import print
from rich.table import Table

tabela = Table(title="Tabela de exemplo", show_header=True, header_style="bold magenta")

tabela.add_column("Nome", style="dim", width=12)
tabela.add_column("Idade", justify="right")
tabela.add_row("[bold red]Alice[/]", "30")

print(tabela)