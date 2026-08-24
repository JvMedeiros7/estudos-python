numstr = str (input('Digite um número entre 0 e 9999:'))

numformatado = numstr.zfill(4)

print(f'analisando o número {numstr}')

print(f'Unidade: {numformatado[3]}')
print(f'Dezenas: {numformatado[2]}')
print(f'Centenas: {numformatado[1]}')
print(f'Milhar: {numformatado[0]}')
