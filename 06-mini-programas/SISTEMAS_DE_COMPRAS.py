# Dicionario unico com todos os dados: nome do item como chave e preco como valor
# Nao precisamos de lista separada para nomes e outra para precos
cardapio = {
    'Arroz':    5.00,
    'Feijao':   2.50,
    'Macarrao': 9.99,
    'Oleo':     1.50,
    'Acucar':   3.75,
}

# Lista que vai acumular os itens escolhidos pelo cliente (o "carrinho")
carrinho = []

# Variavel que vai somar os precos conforme o cliente escolhe
total = 0

# Loop principal: continua ate o cliente digitar 0 para finalizar
while True:

    # Exibe o cardapio numerado usando enumerate
    # start=1 faz a contagem comecar em 1 (em vez de 0)
    # cardapio.items() retorna pares (chave, valor) = (nome, preco)
    print("\n===== CARDAPIO =====")
    for i, (item, preco) in enumerate(cardapio.items(), start=1):
        print(f"  {i} - {item}: R$ {preco:.2f}")
    print("  0 - Finalizar pedido")

    opcao = int(input("\nDigite o numero do item: "))

    # Se o cliente digitar 0, sai do loop e vai para o resumo
    if opcao == 0:
        break

    # Converte o dicionario em lista para acessar pelo indice numerico
    itens = list(cardapio.items())

    # Valida se o numero digitado existe no cardapio
    if opcao < 1 or opcao > len(itens):
        print("Opcao invalida. Tente novamente.")
        continue

    # Pega o nome e preco do item escolhido
    # opcao - 1 porque a lista comeca no indice 0, mas o menu mostra a partir de 1
    nome, preco = itens[opcao - 1]

    quantidade = int(input("Digite a quantidade: "))
    if quantidade <= 0:
        print("Quantidade invalida. Tente novamente.")
        continue

    # Multiplica o preco pela quantidade e acumula no total
    # 'quantidade' precisa ser salva no dicionario para poder ser acessada no resumo final (entrada['quantidade'])
    carrinho.append({'item': nome, 'quantidade': quantidade, 'preco': preco * quantidade})
    total += preco * quantidade
    print(f"{quantidade} x {nome} adicionado ao carrinho. Total parcial: R$ {total:.2f}")

# Exibe o resumo do pedido percorrendo o carrinho com for
print("\n===== PEDIDO FINAL =====")
for entrada in carrinho:
    print(f"  - {entrada['item']} na quantidade {entrada['quantidade']}: R$ {entrada['preco']:.2f}")

print(f"\nTOTAL: R$ {total:.2f}")
