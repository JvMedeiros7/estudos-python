n1 = int(input('digite um n1: '))
n2 = int(input('digite um n2: '))

opcao = 0

while opcao != 5:
    print ('(1)Somar (2) Multiplica (3) Maior (4) Novos Números (5) Sair ')
    opcao = int(input('digite sua opcao: '))
    if opcao == 1:
        soma = n1 + n2
        print (f' A {n1} + {n2} = {soma}')
    elif opcao == 2:
        multiplicar = n1 * n2
        print (f' A {n1} * {n2} = {multiplicar}')
    elif opcao == 3:
        maior = n1 > n2
        print (f' A {n1} é maior que {n2} = {maior}')
        maior = n2 > n1
        print (f'A {n2} é maior que {n1} = {maior}')
    elif opcao == 4:
        n1 = int(input('digite um n1: '))
        n2 = int(input('digite um n2: '))
    elif opcao == 5:
        print('finalizando...')




