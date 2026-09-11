from rich import print
from rich.panel import Panel
from rich.traceback import install

install()

class Gamer:
    def __init__(self, nome, nick, jogos_favoritos):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = jogos_favoritos[:]

        print(Panel(f"[bold cyan]Gamer '{self.nome}' criado com sucesso![/bold cyan]\nNick: [bold yellow]{self.nick}[/bold yellow]\nJogos Favoritos: [bold green]{', '.join(self.jogos_favoritos)}[/bold green]", title="[bold green]Informações do Gamer[/bold green]", border_style="green"))

def cadastro:
    nome = input("Digite o nome do gamer: ")
    nick = input("Digite o nick do gamer: ")
    return nome, nick, jogos_favoritos = []

def adicionar_jogos(gamer):
    while True:
        jogo = input("Digite o nome de um jogo favorito (ou 'sair' para encerrar): ")
        if jogo.lower() == 'sair':
            break
        gamer.jogos_favoritos.append(jogo)
        print(Panel(f"[bold green]Jogo '{jogo}' adicionado aos favoritos de {gamer.nome}![/bold green]", title="[bold green]Jogo Adicionado[/bold green]", border_style="green"))
