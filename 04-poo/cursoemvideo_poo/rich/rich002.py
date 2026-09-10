from rich import print
from rich.panel import Panel
from rich.align import Align

caixa = Panel(
    Align.center("Este é um painel de exemplo criado com o Rich!"),
    title="Mensagem",
    style="bold red",
    width=100,
    subtitle="Sucesso",
    title_align="right",
    subtitle_align="right",
)

print(caixa)