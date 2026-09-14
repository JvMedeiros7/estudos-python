from rich import print
from rich.panel import Panel
from rich.traceback import install

install()


class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 6

    volume_min: int = 0
    volume_max: int = 8

    def __init__(self, canal: int = 1, volume: int = 1):
        self.canal_atual: int = canal
        self.volume_atual: int = volume
        self.ligado: bool = False

    def ligar(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1


    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1

    def mostrar_tv(self):
        conteudo = ""
        if not self.ligado:
            print(Panel("[bold white]TV desligada![/bold white]", title="[bold red]TV[/bold red]", border_style="white"))
        else:
            conteudo = f" Canal = " 
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f" [black on yellow] {canal} [/] "
                else:
                    conteudo += f"{canal} "

            conteudo += f"\n \n Volume = "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f"[black on cyan] [/]"
                else:
                    conteudo += f"[black on white] [/]"
            tv = Panel(conteudo, title="TV", width= 40)
            print(tv)




c = ControleRemoto(2, 3)
while True:
    c.mostrar_tv()
    comando = str(input(f"Digite um comando (@ - lig/deslig, + - VOL ({c.volume_atual}), < > - CH ({c.canal_atual}), s - sair): ")).strip().lower()
    match comando:
        case "@":
            c.ligar()
        case "+":
            c.volume_mais()
        case "-":
            c.volume_menos()
        case ">":
            c.canal_mais()
        case "<":
            c.canal_menos()
        case "s":
            print(Panel("[bold white]Saindo do programa...[/bold white]", title="[bold red]TV[/bold red]", border_style="white"))
            break   
    print("\n" * 10)


