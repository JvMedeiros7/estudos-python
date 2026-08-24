lanches = { "cachorro-quente": 10.00, "hambúrguer": 15.00, "batata-frita": 8.00 }

print("Bem-vindo ao restaurante!")
print("Aqui estão os lanches disponíveis:")     

for lanche, preco in lanches.items():
    print(f"{lanche}: R${preco:.2f}")

print(lanches["hambúrguer"])

def calcular_total(lanche, quantidade):
    if lanche in lanches:
        preco_unitario = lanches[lanche]
        total = preco_unitario * quantidade
        return total
    else:
        return None

lanche_escolhido = input("Digite o nome do lanche que deseja comprar: ").lower()
quantidade = int(input("Digite a quantidade de hambúrgueres que deseja comprar: "))

total_hamburguer = calcular_total(lanche_escolhido, quantidade)
if total_hamburguer is not None:
    print(f"O total a pagar pelos {quantidade} {lanche_escolhido}(s) é: R${total_hamburguer:.2f}")