#Listas - são estruturas de dados que armazenam múltiplos valores em uma única variável. Elas são mutáveis, o que significa que você pode alterar seus elementos após a criação. As listas podem conter diferentes tipos de dados, incluindo números, strings e até outras listas.

'''lista = [1, 2, 3, 4, 5] #Aqui cria uma lista com os valores 1, 2, 3, 4 e 5

lista.append(6) #Adiciona o valor 6 ao final da lista
print(lista) #Exibe a lista atualizada: [1, 2, 3,4, 5, 6]

lista[3] = 10 #Altera o valor do índice 3 para 10
print(lista) #Exibe a lista atualizada: [1, 2, 3, 10, 5, 6] '''

#A lista é mutável, o que significa que você pode alterar seus elementos após a criação.

#Tuplas = Imutaveis / Listas = Mutaveis


'''lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim'] #Aqui cria uma lista chamada lanche com os valores 'Hamburguer', 'Suco', 'Pizza' e 'Pudim'

print("Sua lista inicial de lanches é:", lanche) #Exibe a lista lanche: ['Hamburguer', 'Suco', 'Pizza', 'Pudim']

lanche.insert(0, 'Cachorro Quente') #Adiciona o valor 'Cachorro Quente' no índice 0 da lista lanche

lanche.append('Batata Frita') #Adiciona o valor 'Batata Frita' ao final da lista lanche 

print("Lista adicionado a partir da adição dos pedidos no sistema interno:", lanche) #Exibe a lista lanche atualizada com os valores adicionados

while True: #Inicia um loop infinito

    i = input("Digite o nome do lanche que deseja adicionar ou 'sair' para encerrar: ") #Solicita ao usuário que digite o nome de um lanche para adicionar à lista ou 'sair' para encerrar o loop

    if i == 'sair': #Verifica se o usuário digitou 'sair'
        break #Encerra o loop se o usuário digitou 'sair'
    lanche.append(i) #Adiciona o valor digitado pelo usuário ao final da lista lanche

print("Lista com os valores adicionados pelo usuário:", lanche) #Exibe a lista lanche atualizada com os valores adicionados pelo usuário

#Apagando elementos da lista

lanche.remove('Suco') #Remove o elemento/valor 'Suco' da lista lanche
print("Lista após a remoção do elemento 'Suco':", lanche) #Exibe a lista lanche atualizada após a remoção do elemento

del lanche[3] #Remove o elemento no índice 3 da lista lanche
print("Lista após a remoção do elemento no índice 3:", lanche) #Exibe a lista lanche atualizada após a remoção do elemento

lanche.pop(2) #Remove o elemento no índice 2 da lista lanche
print("Lista após a remoção do elemento no índice 2:", lanche) #Exibe a lista lanche atualizada após a remoção do elemento

while True:
    i = input("Digite o nome do lanche que deseja remover ou 'sair' para encerrar: ") #Solicita ao usuário que digite o nome de um lanche para remover da lista ou 'sair' para encerrar o loop
    if i == 'sair': #Verifica se o usuário digitou 'sair'
        break #Encerra o loop se o usuário digitou 'sair'
    if i in lanche: #Verifica se o valor digitado pelo usuário está presente na lista lanche
        lanche.remove(i) #Remove o valor digitado pelo usuário da lista lanche
    else: #Caso o valor digitado pelo usuário não esteja presente na lista lanche
        print(f"{i} não está na lista.") #Exibe uma mensagem informando que o valor não está na lista

print("Lista após as remoções feitas pelo usuário:", lanche) #Exibe a lista lanche atualizada após as remoções feitas pelo usuário

if 'Pizza' in lanche: #Verifica se o valor 'Pizza' está presente na lista lanche
    print("Pizza está na lista.") #Exibe uma mensagem informando que o valor 'Pizza' está na lista
    remove = input("Deseja remover Pizza da lista? (s/n): ") #Solicita ao usuário que informe se deseja remover o valor 'Pizza' da lista lanche
    if remove.lower() == 's': #Verifica se o usuário digitou 's'
        lanche.remove('Pizza') #Remove Pizza da lista
        print("Pizza foi removida da lista.") #Confirma a remoção
    else: #Caso o usuário não tenha digitado 's'
        print("Pizza não será removida da lista.") #Exibe uma mensagem informando que o valor 'Pizza' não será removido da lista

print("Lista final de lanches:", lanche) #Exibe a lista lanche final após todas as alterações feitas pelo usuário

valores = list(range(4, 11)) #Cria uma lista chamada valores com os números de 4 a 10

print("Lista de valores de 4 a 10:", valores) #Exibe a lista

valores = list(range(4, 11, 2)) #Cria uma lista pulando de 2 em 2, ou seja, com os números 4, 6, 8 e 10
print("Lista de valores de 4 a 10 pulando de 2 em 2:", valores) #Exibe a lista

valores.sort() #Ordena a lista valores em ordem crescente
print("Lista de valores ordenada em ordem crescente:", valores) #Exibe a lista ordenada

valores.sort(reverse=True) #Ordena a lista valores em ordem decrescente
print("Lista de valores ordenada em ordem decrescente:", valores) #Exibe a lista ordenada

print("Tamanho da lista lanche:", len(lanche)) #Exibe o tamanho da lista lanche

x = 0 

for i in lanche: #Percorre cada elemento da lista lanche

    x += 1 #Incrementa o valor de x em 1 a cada iteração do loop

    print(f"Pedido {x}: {i}") #Exibe cada elemento da lista lanche

lanche2 = lanche 

lanche2[2] = 'Sorvete' #Altera o valor do índice 2 da lista lanche2 para 'Sorvete'

print(lanche) #Exibe a lista lanche, que também foi alterada, pois lanche2 é uma referência para a mesma lista
print(lanche2) #Exibe a lista lanche2, que foi alterada para 'Sorvete' no índice 2

lanche3 = lanche[:] #Cria uma cópia da lista lanche e atribui à lista lanche3

lanche3[2] = 'Sorvete' #Altera o valor do índice 2 da lista lanche3 para 'Sorvete'

print(lanche) #Exibe a lista lanche, que não foi alterada, pois lanche3 é uma cópia da lista
print(lanche3) #Exibe a lista lanche3, que foi alterada para 'Sorvete' no índice 2
'''

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]] #Cria uma lista chamada galera, que contém sublistas com nomes e idades

for p in galera: #Percorre cada sublista da lista galera
    print(f"{p[0]} tem {p[1]} anos de idade.") #Exibe o nome e a idade de cada pessoa na lista galera


galera2 = list() #Cria uma lista vazia chamada galera

dado = list() #Cria uma lista vazia chamada dado

for c in range(0, 5): #Inicia um loop que se repete 5 vezes
    dado.append(str(input("Nome: "))) #Solicita ao usuário que digite um nome e adiciona à lista dado
    dado.append(int(input("Idade: "))) #Solicita ao usuário que digite uma idade e adiciona à lista dado
    galera2.append(dado[:]) #Adiciona uma cópia da lista dado à lista galera2
    dado.clear() #Limpa a lista dado para a próxima iteração

print(galera2) #Exibe a lista galera2, que contém sublistas com nomes e idades

for p in galera2: #Percorre cada sublista da lista galera2
    if p[1] >= 21: #Verifica se a idade da pessoa é maior ou igual a 21
        print(f"{p[0]} é maior de idade.") #Exibe uma mensagem informando que a pessoa é maior de idade
        totmai += 1 #Incrementa o contador de pessoas maiores de idade
    else: #Caso a idade da pessoa seja menor que 21
        print(f"{p[0]} é menor de idade.") #Exibe uma mensagem informando que a pessoa é menor de idade
        totmen += 1 #Incrementa o contador de pessoas menores de idade

print(f"Temos {totmai} pessoas maiores de idade e {totmen} pessoas menores de idade.") #Exibe o total de pessoas maiores e menores de idade
