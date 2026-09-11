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

def adicionar_jogos(gamer):
    while True:
        jogo = input("Digite o nome de um jogo favorito (ou 'sair' para encerrar): ")
        if jogo.lower() == 'sair':
            break
        gamer.jogos_favoritos.append(jogo)
        print(Panel(f"[bold green]Jogo '{jogo}' adicionado aos favoritos de {gamer.nome}![/bold green]", title="[bold green]Jogo Adicionado[/bold green]", border_style="green"))

def cadastro():
    while True:
        nome = input("Digite o nome do gamer: ")
        nick = input("Digite o nick do gamer: ")
        jogos_favoritos = []
        adicionar_jogos(Gamer(nome, nick, jogos_favoritos)) 
        opcao = input("Deseja exibir a ficha do gamer? (s/n): ")
        if opcao.lower() == 's':
            print(Panel(f"[bold cyan]Ficha do Gamer[/bold cyan]\nNome: [bold yellow]{nome}[/bold yellow]\nNick: [bold yellow]{nick}[/bold yellow]\nJogos Favoritos: [bold green]{', '.join(self.jogos_favoritos)}[/bold green]", title="[bold green]Informações do Gamer[/bold green]", border_style="green"))
        elif opcao.lower() == 'n':
            print(Panel(f"[bold red]Cadastro encerrado sem exibir a ficha do gamer.[/bold red]", title="[bold red]Cadastro Encerrado[/bold red]", border_style="red"))
            break
        else:
            print(Panel(f"[bold red]Opção inválida. Encerrando o cadastro.[/bold red]", title="[bold red]Erro[/bold red]", border_style="red"))
            break


g1 = cadastro()

