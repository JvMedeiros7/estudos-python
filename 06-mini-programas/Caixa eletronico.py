print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedula = 50  # Começamos sempre com a maior nota
totced = 0  # Quantas notas dessa cédula atual nós usamos

while True:
    if total >= cedula:
        # Se o valor total ainda é maior que a nota atual (ex: 130 >= 50)
        total -= cedula  # Tira 50 do total
        totced += 1  # Conta +1 nota de 50 usada
    else:
        # Se o total ficou menor que a nota atual (ex: sobrou 30, e a nota é 50)
        # Significa que não dá mais para usar nota de 50.

        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedula}')

        # Agora vamos TROCAR a cédula para a próxima disponível
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        totced = 0  # Zeramos o contador para contar as notas da NOVA cédula

        # Se não sobrou nada para pagar, encerra o programa
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')








