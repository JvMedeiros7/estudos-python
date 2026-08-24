distancia = float(input('Qual é a distancia da sua viagem? '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da sua passagem é : {preco:.2f}')