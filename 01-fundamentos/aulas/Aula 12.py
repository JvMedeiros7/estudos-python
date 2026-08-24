fim = '\033[m'
azulnegrito = '\033[1;34m'
amarelo = '\033[1;33m'


print (f'{amarelo}hello world{fim}')
n1 = float(input('Digite n1:'))

if n1 == 10:
    print ('Aprovado com excelência')
elif n1 >= 7 and n1 < 10:
    print ('Aprovado')
elif n1 >= 5 and n1 < 7:
    print('dar para estudar mais para chegar')
else:
    print ('reprovado')