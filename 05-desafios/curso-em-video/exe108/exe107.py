import uteis

p = float(input('Digite o preço: R$ '))

print(f'O dobro de {p} é R$ {uteis.dobro_moeda(p, True):.2f}')
print(f'A metade de {p} é R$ {uteis.metade_moeda(p, True):.2f}')
print(f'O preço com 10% de aumento é R$ {uteis.moeda_10(p, True):.2f}')
print(f'O preço com 20% de aumento é R$ {uteis.moeda_20(p, True):.2f}')