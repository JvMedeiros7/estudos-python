#Cardapio Restaurante 

cardapio = {
    "Entradas": { "pastel" : "R$ 10,00", "Salada": "R$ 8,00", "Sopa": "R$ 12,00" },
    "Pratos Principais": { "Feijoada": "R$ 25,00", "Churrasco": "R$ 30,00", "Peixe Grelhado": "R$ 28,00" },
    "Sobremesas": { "Pudim": "R$ 6,00", "Sorvete": "R$ 5,00", "Bolo": "R$ 7,00" },
    "Bebidas": { "Refrigerante": "R$ 4,00", "Suco": "R$ 5,00", "Água": "R$ 3,00" }
}

def exibir_cardapio():
    print("Bem-vindo ao restaurante!")
    print("Aqui está o cardápio disponível:")
    
    for categoria, itens in cardapio.items():
        print(f"\n{categoria}:")
        for item, preco in itens.items():
            print(f"{item}: {preco}")

def calcular_total(lanche, quantidade):
    for categoria, itens in cardapio.items():
        if lanche in itens:
            preco_unitario = float(itens[lanche].replace("R$", "").replace(",", "."))
            total = preco_unitario * quantidade
            return total
    return None

resposta_cardapio = input("Você deseja ver o cardápio? (Sim/Não): ").lower()

if resposta_cardapio == "sim":
    exibir_cardapio()
    lanche_pedido = input("Qual lanche você deseja pedir? ")
    quantidade_pedido = int(input("Quantos lanches você deseja pedir? "))
    total_pedido = calcular_total(lanche_pedido, quantidade_pedido)
    if total_pedido is not None:
        print(f"O total do seu pedido é: R$ {total_pedido:.2f}")
    novo_pedido = input("Deseja fazer outro pedido? (Sim/Não): ").lower()
    if novo_pedido == "sim":
        exibir_cardapio()
        lanche_pedido2 = input("Qual lanche você deseja pedir? ")
        quantidade_pedido2 = int(input("Quantos lanches você deseja pedir? "))
        total_pedido2 = calcular_total(lanche_pedido2, quantidade_pedido2)
        if total_pedido2 is not None:
            print(f"O total do seu pedido é: R$ {total_pedido2:.2f}")
    else:
        print("Obrigado por visitar nosso restaurante! Volte sempre!")    
else:
    print("Tudo bem! Se mudar de ideia, é só pedir para ver o cardápio.")




