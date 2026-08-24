peso = float(input('Qual seu peso?'))
altura = float(input('Qual sua altura?'))

imc = peso / (altura ** 2)

print (f'O seu imc é{imc:.2f}')

if imc < 18.5:
    print ('Abaixo do peso')
elif imc <25:
    print ('Peso ideal')
elif imc <30:
    print ('Sobrepeso')
elif imc <40:
    print ('Obesidade')
else:
    print ('Obesidade Mórbida')