'''lanche = [ 'Hambúrguer', 'Suco',
 'Pizza', 'Pudim' ]

print(f"na posição {1} {lanche[1]}") # Suco
print(f"na posição {0} {lanche[0]}") # Hambúrguer

#Listas são mutáveis, ou seja, podemos alterar seus elementos. Por exemplo:
lanche[3] = 'Sorvete' # Substitui o Pudim por Sorvete

#Listas.append() - Adiciona um elemento no final da lista
lanche.append('Bolo') # Adiciona o Bolo no final da lista

#Listas.insert() - Adiciona um elemento em uma posição específica da lista
lanche.insert(0, 'Cachorro Quente') # Adiciona o Cachorro Quente na posição 0 da lista



for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') # Eu vou comer Hambúrguer, etc.



lanche.remove('Pizza') # Remove o elemento 'Pizza' da lista
print(lanche) # Imprime a lista atualizada

lanche.pop(2) # Remove o elemento na posição 2 da lista
print(lanche) # Imprime a lista atualizada

del lanche[0] # Exclui o elemento na posição 0 da lista

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') # Eu vou comer Suco, etc.

if 'Pizza' in lanche:
    lanche.remove('Pizza') # Remove o elemento 'Pizza' da lista
else:    print('Não achei a Pizza') # Imprime 'Não achei a Pizza' se a Pizza não estiver na lista

print(f"A lista atualmente está: {lanche}") # Imprime a lista atualizada

valores = list(range(4, 11)) # Cria uma lista de números de 4 a 10
print(sorted(valores)) # Imprime a lista de valores

valores.sort() # Ordena a lista de valores em ordem crescente
reverse = sorted(valores, reverse=True) # Cria uma nova lista de valores ordenada em ordem decrescente
print(valores) # Imprime a lista de valores ordenada
print(reverse) # Imprime a lista de valores ordenada em ordem decrescente

num = [2, 5, 9, 1]
num[2] = 3 # Substitui o elemento na posição 2 por
print(num) # Imprime a lista atualizada

#num[4] = 7 # Tenta atribuir um valor à posição 4, mas isso gera um erro porque a posição 4 não existe na lista
num.append(7) # Adiciona o número 7 no final da lista

print(f"Essa lista tem {len(num)} elementos") # Imprime o número de elementos na lista

num.insert(2, 0) # Insere o número 0 na posição 2 da lista
print(num) # Imprime a lista atualizada

if 5 in num:
    num.remove(5) # Remove o número 5 da lista
else:    print('O número 5 não foi encontrado na lista') # Imprime 'O número 5 não foi encontrado na lista' se o número 5 não estiver na lista

for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}') # Imprime a posição e o valor de cada elemento na lista'''

'''valores = []
x = 0
while x < 5:
    valores.append(int(input('Digite um valor: '))) # Solicita ao usuário que digite um valor e o adiciona à lista de valores
    x += 1

for c, valor in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {valor}') # Imprime a posição e o valor de cada elemento na lista
print('Cheguei ao final da lista.') # Imprime 'Cheguei ao final da lista.' após percorrer todos os elementos da lista

a = [2, 3, 4, 7]
b = a # A variável b recebe a referência da lista a, ou seja, ambas as
# variáveis apontam para a mesma lista na memória
b[2] = 8 # Altera o valor na posição 2 da lista, o que afeta ambas as variáveis a e b

# O python faz uma cópia da lista a para a variável c, ou seja, c aponta para uma nova lista na memória que é uma cópia de a
c = a[:] # A variável c recebe uma cópia da lista a, ou seja, c aponta para uma nova lista na memória que é uma cópia de a
c[2] = 10 # Altera o valor na posição 2 da lista c

print(f'Lista A: {a}') # Imprime a lista A
print(f'Lista B: {b}') # Imprime a lista B
print(f'Lista C: {c}') # Imprime a lista C'''


'''dados = ['Pedro', 25, 'M', 75.5] # Cria uma lista de dados com informações sobre uma pessoa
print(dados) # Imprime a lista de dados

pessoas = list() # Lista de listas: cada elemento será uma lista com dados de uma pessoa
pessoas.append(dados)    # pessoas[0] aponta para o mesmo objeto que dados (referência)
pessoas.append(dados[:]) # pessoas[1] é uma cópia independente de dados
print(pessoas) # Ambas as entradas têm os mesmos valores, mas pessoas[0] e dados compartilham a mesma memória

pessoas = [['Pedro', 25, 'M', 75.5], ['Maria', 30, 'F', 65.0] , ['João', 35, 'M', 80.0]] # Cria uma lista de listas com dados de duas pessoas

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade, é do sexo {p[2]} e pesa {p[3]} kg.') # Imprime as informações de cada pessoa na lista de pessoas

print(f"Nome da primeira pessoa: {pessoas[0][0]}") # Imprime o nome da primeira pessoa na lista de pessoas
print(f"Idade da segunda pessoa: {pessoas[1][1]}") # Imprime a idade da segunda pessoa na lista de pessoas
print(f"Sexo da terceira pessoa: {pessoas[2][2]}") # Imprime o sexo da terceira pessoa na lista de pessoas

print(pessoas[0]) # Imprime a lista de dados da primeira pessoa
print(pessoas[1]) # Imprime a lista de dados da segunda pessoa
print(pessoas[2]) # Imprime a lista de dados da terceira pessoa
'''

'''lista_dados = []

while True:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: ')
    peso = float(input('Digite o peso: '))

    pessoa = [nome, idade, sexo, peso] # Cria uma lista com os dados da pessoa
    lista_dados.append(pessoa) # Adiciona a lista de dados da pessoa à lista de dados

    r = input('Quer continuar? [S/N] ').strip().upper()[0] # Solicita ao usuário se deseja continuar
    if r == 'N': # Se a resposta for 'N', encerra o loop
        break
    for c, p in enumerate(lista_dados):
        print(f" {c} Pessoa: {p[0]} tem {p[1]} anos de idade, é do sexo {p[2]} e pesa {p[3]} kg.") # Imprime as informações de cada pessoa na lista de dados

for p in lista_dados:
    if p[1] >= 18: # Verifica se a idade da pessoa é maior ou igual a 18
        print(f' A pessoa {p[2]}, tem idade de : {p[0]} =  maior de idade.') # Imprime que a pessoa é maior de idade
        tot += 1 # Incrementa o contador de pessoas maiores de idade
    else:
        print(f' A pessoa {p[2]}, tem idade de : {p[0]} =  menor de idade.') # Imprime que a pessoa é menor de idade
        tot += 1 # Incrementa o contador de pessoas menores de idade

for c,p in enumerate(lista_dados):
    print(f'Na posição {c} encontrei o valor {p}') # Imprime a posição e os dados de cada pessoa na lista de dados  

print(lista_dados)

lista_dados.clear() # Limpa a lista de dados, removendo todos os elementos
print(lista_dados) # Imprime a lista de dados vazia'''

