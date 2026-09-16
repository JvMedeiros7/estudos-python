from rich import print
from rich.panel import Panel

# ============================================================
#  Agencia (MI6) - o CADASTRO de missões
# ============================================================
# A Agencia NÃO herda de Missao (ela não É uma missão).
# Ela apenas GUARDA missões numa lista - qualquer objeto que seja
# uma Missao (ou filha dela) pode ser cadastrado aqui.


class Agencia:
    def __init__(self, nome):
        self.nome = nome                                # Ex.: "MI6"
        self.missoes = []                               # Lista vazia: o cadastro começa sem nenhuma missão

    def cadastrar(self, missao):                        # Recebe QUALQUER Missao (Espionagem, Resgate, Sabotagem...)
        self.missoes.append(missao)                     # Guarda o objeto na lista
        return f"Missão {missao.codigo} cadastrada no {self.nome}."

    def listar(self):                                   # Mostra todas as missões cadastradas
        print(Panel(f"Missões cadastradas no {self.nome}", style="bold green"))
        for missao in self.missoes:
            print(f"  {missao}")                        # print(missao) usa o __str__ HERDADO de Missao

    def buscar_por_status(self, status):                # Filtra o cadastro pelo status ("Pendente", "Concluída"...)
        encontradas = []
        for missao in self.missoes:
            if missao.status == status:                 # .status existe em TODAS, porque veio da superclasse Missao
                encontradas.append(missao)
        return encontradas
