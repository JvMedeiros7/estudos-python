anonasc = int(input('Qual seu ano de nascimento?'))

idade = 2025 - anonasc
print(f'Sua idade é : {idade}')

if idade > 18:
    print('Já passou do tempo, corra para se alistar!')
elif idade == 18:
    print('É hora de se alistar!')
elif idade < 18:
    print ('Voce ainda vai se alistar')



