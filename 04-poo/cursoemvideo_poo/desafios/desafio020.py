from rich import print
from rich.panel import Panel
from rich.traceback import install

install()

class Gamer:
    def __init__(self, nome, nick, jogos_favoritos):
        ## 'self' é o objeto que está sendo criado. Só existe AQUI DENTRO da classe.
        ## Cada 'self.algo = ...' guarda um dado dentro do objeto.
        self.nome = nome
        self.nick = nick
        ## O [:] faz uma CÓPIA da lista. A lista dentro do objeto é uma lista nova,
        ## separada da que foi passada. Por isso, mais abaixo, sempre usamos
        ## gamer.jogos_favoritos (a lista do objeto), e não a lista original.
        self.jogos_favoritos = jogos_favoritos[:]
        print(Panel(f"[bold cyan]Gamer '{self.nome}' criado com sucesso![/bold cyan]\nNick: [bold yellow]{self.nick}[/bold yellow]\nJogos Favoritos: [bold green]{', '.join(self.jogos_favoritos)}[/bold green]", title="[bold green]Informações do Gamer[/bold green]", border_style="green"))

def adicionar_jogos(gamer):
    ## 'gamer' é um objeto Gamer. Aqui fora da classe ele NÃO se chama 'self',
    ## ele se chama pelo nome do parâmetro que recebeu.
    while True:
        jogo = input("Digite o nome de um jogo favorito (ou 'sair' para encerrar): ")
        if jogo.lower() == 'sair':
            break
        ## Adiciona na lista que está DENTRO do objeto.
        gamer.jogos_favoritos.append(jogo)
        print(Panel(f"[bold green]Jogo '{jogo}' adicionado aos favoritos de {gamer.nome}![/bold green]", title="[bold green]Jogo Adicionado[/bold green]", border_style="green"))

def cadastro():
    while True:
        nome = input("Digite o nome do gamer: ")
        nick = input("Digite o nick do gamer: ")

        ## CORREÇÃO 1: antes o objeto era criado e passado direto para
        ## adicionar_jogos(Gamer(...)), sem ser guardado em nenhuma variável.
        ## Ele recebia os jogos e depois era perdido. Agora guardamos em 'gamer'.
        gamer = Gamer(nome, nick, [])
        adicionar_jogos(gamer)

        opcao = input("Deseja exibir a ficha do gamer? (s/n): ")
        if opcao.lower() == 's':
            ## CORREÇÃO 2: aqui estava 'self.jogos_favoritos', mas 'self' não existe
            ## fora da classe (dava NameError). Fora da classe, acessamos os dados
            ## do objeto pela variável que guarda ele: gamer.nome, gamer.nick, etc.
            print(Panel(f"[bold cyan]Ficha do Gamer[/bold cyan]\nNome: [bold yellow]{gamer.nome}[/bold yellow]\nNick: [bold yellow]{gamer.nick}[/bold yellow]\nJogos Favoritos: [bold green]{', '.join(gamer.jogos_favoritos)}[/bold green]", title="[bold green]Informações do Gamer[/bold green]", border_style="green"))
            ## CORREÇÃO 3: antes não tinha 'break' aqui, então depois de exibir a ficha
            ## o while voltava e pedia um cadastro novo. 'return' encerra a função
            ## E devolve o objeto para quem chamou (a linha g1 = cadastro()).
            return gamer
        elif opcao.lower() == 'n':
            print(Panel("[bold red]Cadastro encerrado sem exibir a ficha do gamer.[/bold red]", title="[bold red]Cadastro Encerrado[/bold red]", border_style="red"))
            return gamer
        else:
            print(Panel("[bold red]Opção inválida. Encerrando o cadastro.[/bold red]", title="[bold red]Erro[/bold red]", border_style="red"))
            return gamer


## CORREÇÃO 4: a função original usava 'break' e não devolvia nada, então g1
## ficava como None. Agora g1 recebe o objeto Gamer criado no cadastro.
g1 = cadastro()
