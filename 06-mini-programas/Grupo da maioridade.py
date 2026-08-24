from datetime import date
atual =  date.today().year
c = 0
for pess in range (1,8):
    c= c+1
    anonasc = int(input('Digite o ano de nascimento: '))
    idade = atual - anonasc
    print(f'Essa pessoa tem {idade} anos')
    if idade >= 21:
        print ('Essa pessoa é de maior')
    else:
            print('Essa pessoa é menor')
