#Desafio 078

'''numeros = list()

x = 0
for valor in range(0,5):

    numeros.append(int(input(f'Digite um valor na posição {x}: ')))
    x += 1
print(f'Você digitou os valores {numeros}')

print(f'O maior valor digitado foi {max(numeros)} na posição {numeros.index(max(numeros))}')
print(f'O menor valor digitado foi {min(numeros)} na posição {numeros.index(min(numeros))}')'''

#Desafio 079

'''valores = list()
soma = 0

while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += valores[-1]
    if resposta in 'N':
        break
print(f'Você digitou os valores {sorted(valores)}')
print(f'A soma dos valores digitados é {soma}')'''

#Desafio 080

'''numeros = list()

for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1

print(f'Os valores digitados em ordem são: {numeros}')'''

#Desafio 081

'''valores = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'N':
        break

print(f"Você digitou a quantidade de valores : {len(valores)}")

valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')

x = input('Digite um valor para saber se ele faz parte da lista: ')

if x in valores:
    print(f'O valor {x} faz parte da lista!')
else:
    print(f'O valor {x} não foi encontrado na lista!')

print('Fim do programa!')'''

#Desafio 082

'''valores_pares = []
valores_impares = []
valores_totais = []

while True:
    n = int(input('Digite um valor: '))
    valores_totais.append(n)
    if n % 2 == 0:
        valores_pares.append(n)
    else:
        valores_impares.append(n)
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'N':
        break
print(f'Os valores pares digitados foram: {valores_pares}')
print(f'Os valores ímpares digitados foram: {valores_impares}')
print(f'Os valores totais digitados foram: {sorted(valores_totais)}')'''

#Desafio 083

'''expr = str(input('Digite uma expressão: ')).strip()
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')'''
