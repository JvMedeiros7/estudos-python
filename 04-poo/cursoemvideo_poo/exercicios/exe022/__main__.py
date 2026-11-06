from classes022 import Cantina, Lanche, Bebida, Entregador, Status
from rich import print


def main():
    cantina = Cantina("Cantina do Zé")

    # Cardápio (Lanche e Bebida são tratados como Item: polimorfismo)
    cantina.cadastrar_item(Lanche("X-Burger", 18.0, ["bacon"]))
    cantina.cadastrar_item(Lanche("Pão de queijo", 6.0))
    cantina.cadastrar_item(Bebida("Suco de laranja", 8.0, 500))
    cantina.cadastrar_item(Bebida("Café", 4.0, 100, gelada=False))
    cantina.mostrar_cardapio()

    cantina.contratar(Entregador("Marcos"))

    # Pedido para retirada
    print("\n[bold]--- Pedido 1 (retirada) ---[/bold]")
    p1 = cantina.novo_pedido("Ana")
    p1.adicionar(cantina.buscar_item("x-burger"))
    p1.adicionar(cantina.buscar_item("café"))
    p1.avancar(Status.PREPARANDO)
    p1.avancar(Status.PRONTO)
    print(str(p1))  # str() força o __str__; o rich só lê markup em texto

    # Pedido com entrega
    print("\n[bold]--- Pedido 2 (entrega) ---[/bold]")
    p2 = cantina.novo_pedido("Bruno", "Rua das Flores, 123")
    p2.adicionar(cantina.buscar_item("pão de queijo"))
    p2.adicionar(cantina.buscar_item("suco de laranja"))
    p2.avancar(Status.PREPARANDO)

    # Tenta sair antes de ficar pronto (deve recusar)
    entregador = cantina.entregador_livre()
    entregador.sair_para_entrega(p2)

    p2.avancar(Status.PRONTO)
    entregador.sair_para_entrega(p2)
    p2.adicionar(cantina.buscar_item("café"))  # recusado: já saiu
    p2.cancelar()                              # recusado: já saiu
    entregador.concluir_entrega()
    print(str(p2))

    # Pedido cancelado não entra no faturamento
    print("\n[bold]--- Pedido 3 (cancelado) ---[/bold]")
    p3 = cantina.novo_pedido("Carla")
    p3.adicionar(cantina.buscar_item("café"))
    p3.cancelar()

    print(f"\nFaturamento: [bold green]R${cantina.faturamento():,.2f}[/bold green]")


if __name__ == "__main__":
    main()
