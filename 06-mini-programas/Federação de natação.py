anonasc=int(input('Qual seu ano de nascimento?'))

idade = 2025 - anonasc

if idade <= 20 and idade > 19 :
    print(f'sua é idade é \033[1;31m{idade}\033[m')
    print ('Sua categória é sênior')
elif idade <= 19 and idade > 14 :
    print(f'sua é idade é \033[1;32m{idade}\033[m')
    print ('Sua categória é junior')
elif idade <= 14 and idade > 9 :
    print(f'sua é idade é \033[1;33m{idade}\033[m')
    print ('Sua categória é mirim')
elif idade > 20:
    print(f'sua é idade é \033[1;34m{idade}\033[m')
    print ('Você está acima da idade')
else:
    print(f'sua é idade é \033[1;35m{idade}\033[m')
    print ('tente novamente, %%ERROR 404%%')

