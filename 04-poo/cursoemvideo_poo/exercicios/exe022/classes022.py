from rich import print
from enum import Enum


# ---------------------------------------------------------------
# STATUS DO PEDIDO (Enum)
# Enum evita "strings mágicas" soltas pelo código: em vez de comparar
# com "pronto" ou "Pronto " (e errar), usamos Status.PRONTO.
# ---------------------------------------------------------------
class Status(Enum):
    ABERTO = "Aberto"
    PREPARANDO = "Preparando"
    PRONTO = "Pronto"
    EM_ENTREGA = "Em entrega"
    ENTREGUE = "Entregue"
    CANCELADO = "Cancelado"


# ---------------------------------------------------------------
# HERANÇA: Item é a classe base; Lanche e Bebida especializam.
# ---------------------------------------------------------------
class Item:
    """Classe base de qualquer produto vendido na cantina."""

    def __init__(self, nome: str, preco: float):
        self._nome = nome
        self._preco = preco  # protegido (_): convenção de "não mexa de fora"

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    def descricao(self):
        """Método que as filhas podem sobrescrever (polimorfismo)."""
        return self._nome

    def __str__(self):
        return f"{self.descricao()} - R${self._preco:,.2f}"


class Lanche(Item):
    """Lanche pode ter adicionais (ex.: bacon, queijo extra)."""

    def __init__(self, nome: str, preco: float, adicionais: list[str] = None):
        super().__init__(nome, preco)  # reaproveita o __init__ da classe mãe
        self._adicionais = adicionais or []

    # Sobrescrita: mesmo nome do método da mãe, comportamento próprio
    def descricao(self):
        if self._adicionais:
            return f"{self._nome} (+ {', '.join(self._adicionais)})"
        return self._nome


class Bebida(Item):
    """Bebida tem tamanho em ml e pode ser gelada."""

    def __init__(self, nome: str, preco: float, ml: int = 300, gelada: bool = True):
        super().__init__(nome, preco)
        self._ml = ml
        self._gelada = gelada

    def descricao(self):
        temp = "gelada" if self._gelada else "natural"
        return f"{self._nome} {self._ml}ml ({temp})"


# ---------------------------------------------------------------
# COMPOSIÇÃO: um Pedido "tem" vários Itens (relação tem-um).
# ---------------------------------------------------------------
class Pedido:
    """Pedido de um cliente: guarda itens e controla o status."""

    _proximo_numero = 1  # atributo de CLASSE: compartilhado por todos os pedidos

    def __init__(self, cliente: str):
        self._numero = Pedido._proximo_numero
        Pedido._proximo_numero += 1
        self._cliente = cliente
        self._itens: list[Item] = []
        self._status = Status.ABERTO

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def status(self):
        return self._status

    @property
    def total(self):
        """Propriedade calculada: sempre reflete os itens atuais."""
        return sum(item.preco for item in self._itens)

    def adicionar(self, item: Item):
        # Só dá para mexer no pedido enquanto ele está aberto
        if self._status != Status.ABERTO:
            print(f"[red]Pedido #{self._numero} não aceita mais itens ({self._status.value}).[/red]")
            return
        self._itens.append(item)
        print(f"+ {item}")

    def avancar(self, novo_status: Status):
        """Muda o status. Protege contra alterar pedido finalizado."""
        if self._status in (Status.ENTREGUE, Status.CANCELADO):
            print(f"[red]Pedido #{self._numero} já foi finalizado.[/red]")
            return
        self._status = novo_status

    def cancelar(self):
        # Não dá para cancelar o que já saiu para entrega
        if self._status in (Status.EM_ENTREGA, Status.ENTREGUE):
            print(f"[red]Pedido #{self._numero} não pode mais ser cancelado.[/red]")
            return
        self._status = Status.CANCELADO
        print(f"[yellow]Pedido #{self._numero} cancelado.[/yellow]")

    def __str__(self):
        linhas = [f"[bold]Pedido #{self._numero}[/bold] - {self._cliente} ({self._status.value})"]
        linhas += [f"  • {item}" for item in self._itens]
        linhas.append(f"  [bold blue]Total: R${self.total:,.2f}[/bold blue]")
        return "\n".join(linhas)


# ---------------------------------------------------------------
# HERANÇA + COMPOSIÇÃO: PedidoEntrega é um Pedido com endereço e taxa.
# ---------------------------------------------------------------
class PedidoEntrega(Pedido):
    """Pedido que será entregue: soma a taxa de entrega ao total."""

    TAXA_ENTREGA = 5.00  # constante de classe

    def __init__(self, cliente: str, endereco: str):
        super().__init__(cliente)
        self._endereco = endereco

    # Sobrescreve a propriedade: total dos itens + taxa
    @property
    def total(self):
        return super().total + self.TAXA_ENTREGA

    def __str__(self):
        base = super().__str__()
        return f"{base}\n  Entrega em: {self._endereco} (taxa R${self.TAXA_ENTREGA:,.2f})"


class Entregador:
    """Pessoa que leva os pedidos. Só leva um pedido por vez."""

    def __init__(self, nome: str):
        self._nome = nome
        self._pedido_atual: PedidoEntrega | None = None

    @property
    def disponivel(self):
        return self._pedido_atual is None

    def sair_para_entrega(self, pedido: PedidoEntrega):
        if not self.disponivel:
            print(f"[red]{self._nome} já está em uma entrega.[/red]")
            return
        if pedido.status != Status.PRONTO:
            print(f"[red]Pedido #{pedido.numero} ainda não está pronto.[/red]")
            return
        self._pedido_atual = pedido
        pedido.avancar(Status.EM_ENTREGA)
        print(f"{self._nome} saiu com o pedido #{pedido.numero}.")

    def concluir_entrega(self):
        if self.disponivel:
            print(f"[red]{self._nome} não tem entrega em andamento.[/red]")
            return
        self._pedido_atual.avancar(Status.ENTREGUE)
        print(f"[green]Pedido #{self._pedido_atual.numero} entregue por {self._nome}![/green]")
        self._pedido_atual = None  # fica livre de novo


# ---------------------------------------------------------------
# CLASSE "GERENTE": organiza cardápio, pedidos e entregadores.
# ---------------------------------------------------------------
class Cantina:
    """Coordena o funcionamento da cantina."""

    def __init__(self, nome: str):
        self._nome = nome
        self._cardapio: dict[str, Item] = {}
        self._pedidos: list[Pedido] = []
        self._entregadores: list[Entregador] = []

    def cadastrar_item(self, item: Item):
        self._cardapio[item.nome.lower()] = item

    def contratar(self, entregador: Entregador):
        self._entregadores.append(entregador)

    def mostrar_cardapio(self):
        print(f"\n[bold]Cardápio - {self._nome}[/bold]")
        for item in self._cardapio.values():
            print(f"  {item}")

    def buscar_item(self, nome: str):
        return self._cardapio.get(nome.lower())

    def novo_pedido(self, cliente: str, endereco: str = None):
        """Cria pedido comum (retirada) ou de entrega, se houver endereço."""
        pedido = PedidoEntrega(cliente, endereco) if endereco else Pedido(cliente)
        self._pedidos.append(pedido)
        return pedido

    def entregador_livre(self):
        # next() devolve o primeiro que satisfaz a condição (ou None)
        return next((e for e in self._entregadores if e.disponivel), None)

    def faturamento(self):
        """Soma só o que foi entregue (ou retirado/pronto) e não cancelado."""
        return sum(
            p.total for p in self._pedidos
            if p.status in (Status.PRONTO, Status.ENTREGUE)
        )
