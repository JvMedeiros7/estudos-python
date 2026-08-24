num = int(input('Digite um número: '))

print ('''Escolha uma das bases para conversão:
(1) Converter para binário
(2) Converter para octal
(3) Converter para hexadecimal''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print (f'{num} convertido para binário é igual a {bin(num)[2:]}')
elif opcao == 2:
    print (f'{num} convertido para octal é igual a {oct(num)[2:]}')
elif opcao == 3:
    print (f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')

else:
    print ('Opção invalida. tente novamente')