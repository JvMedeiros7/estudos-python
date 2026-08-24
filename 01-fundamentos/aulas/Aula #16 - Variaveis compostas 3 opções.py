'''
lanche = ('Hamburguer ', 'Suco' , 'Pizza', 'Pudim')

#1

for pos, comida in enumerate(lanche):
    print(f' Eu vou comer {comida} na posição {pos}')

# 2

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# 3

for comida in lanche:
    print(f'Eu vou comer {comida}')'''

p1 = str(input('Diga seu Nome: '))
p2 = str(input('Diga seu sexo: '))

pessoa = (p1, p2)
print(pessoa[1])


