n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print (f'O menor valor digitado foi {menor}')
print (f'O maior valor digitado foi {maior}')
