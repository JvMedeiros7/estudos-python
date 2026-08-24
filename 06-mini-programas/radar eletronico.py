velocidade = int(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print ('Você foi multado')
    print (f'A multa é de R${(velocidade - 80) * 7}')

else:
    print ('você não foi multado')