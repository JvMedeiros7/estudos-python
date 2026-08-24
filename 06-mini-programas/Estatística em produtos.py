total = totmil = menor = cont = 0
barato = ' '

while True:
    produto = str(input('Qual o produto?'))
    preco = float(input('Qual o preço?'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print (f'O total da compra foi R${total:.2f}')
print (f' Temos {totmil} produtos custando mais de R$ 1000')
print (f'O produto mais barato é {barato} e custa R${menor:.2f}')