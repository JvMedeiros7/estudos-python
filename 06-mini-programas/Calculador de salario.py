salarioatual = float(input('Qual é o salário do funcionário? R$'))

limite = 1250.0

if salarioatual > limite:
    percentual = 0.10
else:
    percentual = 0.20

aumento = salarioatual * percentual
novosalario = salarioatual + aumento

print (f'Quem ganhava R$ {salarioatual:.2f} passa a ganhar R$ {novosalario:.2f}')
print (f'O aumento foi de R$ {aumento:.2f}')