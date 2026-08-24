nome = str(input('Digite seu nome: ')).strip()

print(f'Analisando seu nome...')

print (f'Seu nome em maiúscula é: {nome.upper()}')
print (f'seu nome em minuscúla é: {nome.lower()}')

totalletras = len(nome) - nome.count(' ')
print(f'Seu nome tem {totalletras} letras')

primeironome = nome.split()[0]
print(f'Seu primeiro nome é: {primeironome} e ele tem {len(primeironome)} letras')