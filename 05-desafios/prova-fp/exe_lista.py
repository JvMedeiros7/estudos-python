#Desafio 078 

'''lista = []

for c in range(5):
    num = int(input('Digite um número: '))

    if c == 0 or num > lista[-1]: # Verifica se é o primeiro número ou se o número é maior que o último número da lista
        lista.append(num) # Adiciona o número no final da lista
        print('Número adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]: # Verifica se o número é menor ou igual ao número na posição atual da lista
                lista.insert(pos, num) # Insere o número na posição atual da lista
                print(f'Número adicionado na posição {pos} da lista...')
                break
            pos += 1



for c, num in enumerate(lista):
    print(f'Na posição {c} encontrei o valor {num}') # Imprime a posição e o valor de cada elemento na lista'''

'''num = []
x = 0 
while True:
    n = int(input('Digite um valor: '))
    if n not in num: # Verifica se o número não está na lista
        num.append(n) # Adiciona o número à lista
        print(f' Na posição {x} : Valor adicionado com sucesso...')
        x += 1
    else:
        print('Valor duplicado! Não vou adicionar...') # Informa que o valor é duplicado e não será adicionado
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0] # Solicita ao usuário se deseja continuar
    if r == 'N': # Se a resposta for 'N', encerra o loop
        break'''

'''print('-='*30)
num.sort() # Ordena a lista em ordem crescente

for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}...') # Imprime a posição e o valor de cada elemento na lista'''

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
        print(f' A pessoa {p[0]}, tem idade de : {p[1]} =  maior de idade.') # Imprime que a pessoa é maior de idade
        tot += 1 # Incrementa o contador de pessoas maiores de idade
    else:
        print(f' A pessoa {p[0]}, tem idade de : {p[1]} =  menor de idade.') # Imprime que a pessoa é menor de idade
        tot += 1 # Incrementa o contador de pessoas menores de idade

for p in lista_dados:
    if p[3] >= 70: # Verifica se o peso da pessoa é maior ou igual a 70
        print(f' A pessoa {p[0]}, tem peso de : {p[3]} =  acima do peso.') # Imprime que a pessoa está acima do peso
        tot_70.append(p[0]) # Adiciona o nome da pessoa à lista de pessoas acima do peso
        tot_70 += 1 # Incrementa o contador de pessoas acima do peso
    else:
        print(f' A pessoa {p[0]}, tem peso de : {p[3]} =  abaixo do peso.') # Imprime que a pessoa está abaixo do peso
        tot_50.append(p[0]) # Adiciona o nome da pessoa à lista de pessoas abaixo do peso
        tot_50 += 1 # Incrementa o contador de pessoas abaixo do peso  
  
print(f'Foram cadastradas {tot} pessoas maiores de idade.') # Imprime o total de pessoas maiores de idade
print(f'Foram cadastradas {tot} pessoas menores de idade.') # Imprime o total de pessoas menores de idade
print(f"Pessoas acima do peso: {tot_70}") # Imprime o total de pessoas acima do peso
print(f"Pessoas abaixo do peso: {tot_50}") # Imprime o total de pessoas abaixo do peso


for c,p in enumerate(lista_dados):
    print(f'Na posição {c} encontrei o valor {p}') # Imprime a posição e os dados de cada pessoa na lista de dados  

print(lista_dados)

lista_dados.clear() # Limpa a lista de dados, removendo todos os elementos
print(lista_dados) # Imprime a lista de dados vazia'''


'''lista_dados = []
totpessoas = 0
tot70 = 0
tot50 = 0

while True:
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))

    pessoa = [nome, peso] # Cria uma lista com os dados da pessoa
    lista_dados.append(pessoa) # Adiciona a lista de dados da pessoa à lista de dados

    r = input('Quer continuar? [S/N] ').strip().upper() # Solicita ao usuário se deseja continuar
    if r == 'S':
        totpessoas += 1 # Incrementa o contador de pessoas
        if peso >= 70: # Verifica se o peso da pessoa é maior ou igual a 70
            print(f' A pessoa {pessoa[0]}, tem peso de : {pessoa[1]} =  acima do peso.') # Imprime que a pessoa está acima do peso
            tot70 += 1 # Incrementa o contador de pessoas acima do peso
        else:
            print(f' A pessoa {pessoa[0]}, tem peso de : {pessoa[1]} =  abaixo do peso.') # Imprime que a pessoa está abaixo do peso
            tot50 += 1 # Incrementa o contador de pessoas abaixo do peso
    else:
        break

print(f'Foram cadastradas {totpessoas} pessoas.') # Imprime o total de pessoas cadastradas
print(f'Pessoas acima do peso: {tot70}') # Imprime o total de pessoas acima do peso
print(f'Pessoas abaixo do peso: {tot50}') # Imprime o total de pessoas abaixo do peso

if lista_dados:
    maior = lista_dados[0]
    menor = lista_dados[0]

    for pessoa in lista_dados:
        if pessoa[1] > maior[1]:
            maior = pessoa
        if pessoa[1] < menor[1]:
            menor = pessoa

    print(f'Maior peso: {maior[0]} com {maior[1]} kg')
    print(f'Menor peso: {menor[0]} com {menor[1]} kg')

'''

'''lista_dados = []
totpar = 0
listapar = []
totimpar = 0
listaimpar = []

for i, c in enumerate(range(0,8)):
    lista_dados.append(c)
    if c % 2 == 0:
        totpar += 1
        listapar.append(c)
    else:
        totimpar += 1
        listaimpar.append(c)

  
    print(f'Foram digitados {totpar} números pares: {listapar}') # Imprime o total de números pares e a lista de números pares
    print(f'Foram digitados {totimpar} números ímpares: {listaimpar}') # Imprime o total de números ímpares e a lista de números ímpares

    print(sorted(lista_dados)) # Imprime a lista de números pares ordenada'''


'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Cria uma matriz 3x3 preenchida com zeros
somapar = 0
totpar = 0
soma3 = 0
maior2 = []

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite um valor para a posição [{i}, {j}]: ')) # Solicita ao usuário que digite um valor para cada posição da matriz
        if matriz[i][j] % 2 == 0: # Verifica se o valor digitado é par
            somapar += matriz[i][j] # Soma os valores pares
        if j == 2:
            soma3 += matriz[i][j] # Soma os valores da terceira coluna
        if i == 1:
            if not maior2 or matriz[i][j] > maior2:
                maior2 = matriz[i][j] # Atualiza o maior valor da segunda linha


print('Matriz digitada:') # Imprime a matriz digitada
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end='') # Imprime cada elemento da matriz formatado com 5 espaços e centralizado
    print() # Imprime uma nova linha após cada linha da matriz


print(f'Soma dos valores pares: {somapar}') # Imprime a soma dos valores pares
print(f'Soma dos valores da terceira coluna: {soma3}') # Imprime a soma dos valores da terceira coluna
print(f'Maior valor da segunda linha: {maior2}') # Imprime o maior valor da segunda linha'''


'''from random import randint

lista = []
jogos = []

quant = int(input('Quantos jogos você quer que eu sorteie? ')) # Solicita ao usuário quantos jogos deseja sortear
tot = 0

while tot < quant:
    cont = 0
    while True:
        num = randint(1, 60) # Gera um número aleatório entre 1 e 60
        if num not in lista: # Verifica se o número não está na lista
            lista.append(num) # Adiciona o número à lista
            cont += 1 # Incrementa o contador de números sorteados
        if cont >= 6: # Se já foram sorteados 6 números, sai do loop
            break
    jogos.append(sorted(lista)) # Adiciona o jogo à lista de jogos
    lista.clear() # Limpa a lista para o próximo jogo
    tot += 1

print(f'Os jogos gerados foram: {jogos}') # Imprime os jogos gerados
print('Boa sorte!') # Imprime 'Boa sorte!' após gerar os jogos  '''