#Tupla: Imutável, não pode ser alterada, mas pode ser consultada. Utiliza parênteses.

'''name = ("Joao", "Maria", "Ana", "Pedro")

print(name[0])

x = 0 

for i in name:
    x += 1
    print(f"{x}: {i}")

print(name[1:3])

print(name[-1])

print(name[1:])

print(len(name))

while True:
    print("Digite um nome: ")
    n = input()
    if n in name:
        print(f"{n} encontrado!")
    else:
        print(f"{n} nao encontrado!")''',


'''lanche = ("Hamburguer", "Suco", "Pizza", "Pudim" , "Batata Frita")

print("Lance na 2a posição" , lanche[1])
print("Lancha na posição -2 " , lanche[-2])

print("Quantidade de lanches " , len(lanche))

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {cont}°: {lanche[cont]}")

x = 0

for pos, comida in enumerate(lanche):
    x += 1
    print(f"Eu vou comer {x}°: {comida} na posição {pos}")

for comida in lanche:
    print(f"Eu vou comer {comida}")

print(sorted(lanche)) #Ordena a tupla, mas não altera a tupla original
print(lanche) '''

'''a = (2, 5, 9, 1)
b = (5, 7, 4, 2)
c = a + b #Concatenação de tuplas
print(c)

c = b + a #Ordem importa, então o resultado é diferente da linha anterior
print(c) 

print(len(c)) #Quantidade de elementos na tupla c
print(c.count(5)) #Quantidade de vezes que o número 5 aparece na tupla c    
print(c.index(9)) #Posição do número 9 na tupla c
print(c.index(5)) #Posição do número 5 na tupla c, retorna a posição do primeiro número 5 encontrado  
print(c.index(5, 1)) #Posição do número 5 na tupla c, a partir da posição 5'''

'''pessoa = ("Gustavo", 39, "M", 99.88)
print(pessoa)
del(pessoa) #Deleta a tupla, não é possível acessar a tupla depois disso
print(pessoa) #Erro, a tupla foi deletada

#Dados podem ser de tipos diferentes, como string, inteiro, float, etc.'''


