nomecompleto = str (input ('Digite seu nome completo: ')).strip()

nomes = nomecompleto.split()

primeironome = nomes [0]

ultimo = nomes [-1]

print(f'Muito prazer em te conhecer!')
print(f'Seu primeiro nome é: {primeironome}')
print(f'Seu último nome é: {ultimo}')
