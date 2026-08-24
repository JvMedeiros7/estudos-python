#Desafio 76 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ("Arroz", 5.50, "Feijão", 7.30, "Macarrão", 3.20, "Óleo", 4.80, "Açúcar", 2.90)

print("=" * 40)
print("LISTAGEM DE PREÇOS")
print("=" * 40)

for i in range(0, len(produtos), 2):
    produto = produtos[i]
    preco = produtos[i + 1]
    print(f"{produto:<20} R$ {preco:>6.2f}")
