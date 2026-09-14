from rich import print
from rich.panel import Panel
from rich.traceback import install

install()

class Caneta:
    def __init__(self, cor = "azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[bold blue]"
            case "vermelho" | "vermelha":
                escolha = "[bold red]"
            case "verde":
                escolha = "[bold green]"
            case _:
                escolha = "[bold white]"
                print(Panel(f"[bold red]Cor inválida![/bold red]\nA cor da caneta será definida como [bold white]branca[/bold white].", title="[bold red]Erro[/bold red]", border_style="red"))
        self.nome_cor = cor
        self.cor = escolha
        self.tampada = True


    def escrever(self, msg):
        if self.tampada:
            print(Panel(f"[bold red]ERRO![/bold red]\nA caneta {self.cor}{self.nome_cor} está tampada, não é possível escrever.", title="[bold red]Erro[/bold red]", border_style="red"))
            return
        print(f"{self.cor}{msg}", end ="")
        pass 

    def quebrar_linha(self, qtd = 1):
        for _ in range(qtd):

            print()

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False



c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")


c1.destampar()
c2.destampar()
c3.destampar()


c1.escrever("Olá, mundo!")
c1.quebrar_linha(2)
c2.escrever("Olá, mundo!")
c2.quebrar_linha(2)
c3.escrever("Olá, mundo!")
c3.quebrar_linha(2) 

c1.tampar()
c1.escrever("Tentando escrever com a caneta tampada.")


c1.destampar()
c1.escrever(input("Digite algo para escrever com a caneta azul: "))
#Escreve com o que usuário digitar, com a cor azul, pois a caneta foi destampada.