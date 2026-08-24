num = 0
cont = 0
soma = 0
num = int(input('digite um numero [999 PARA PARAR]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('digite um numero [999 PARA PARAR]: '))
print (f'Você digitou {cont} numeros e a soma entre eles é {soma}')
