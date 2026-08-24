nomes = ("João", "Maria", "Pedro", "Ana", "Carlos")

#Tuplas são definidas usando parênteses e os elementos são separados por vírgulas
#Tupla é imutável, ou seja, não pode ser alterada após a criação

#nomes[0] = "José" #Isso causará um erro

print(nomes[0]) #Acessando o primeiro elemento da tupla
print(nomes[1:4]) #Acessando um intervalo de elementos da tupla
print(nomes[-1]) #Acessando o último elemento da tupla
print(nomes[:3]) #Acessando os primeiros três elementos da tupla
print(nomes[-3:]) #Acessando os últimos três elementos da tupla

#Podemos usar a função len() para obter o número de elementos na tupla
print(len(nomes)) #Imprime o número de elementos na tupla

#Podemos usar a função count() para contar quantas vezes um elemento aparece na tupla
print(nomes.count("Maria")) #Imprime o número de vezes que "Maria" aparece na tupla

#Podemos usar a função index() para encontrar o índice de um elemento na tupla
print(nomes.index("Pedro")) #Imprime o índice de "Pedro" na tupla

x = 0
i = 0 

for nome in nomes:
    x += 1 #Contador para contar o número de elementos na tupla
    print(f"Indice {i}: Elemento {x}: {nome}") #Imprime cada nome na tupla usando um loop for
    i += 1 #Contador para contar o número de elementos na tupla usando um loop for

for cont in range(len(nomes)):
    print(f"Indice {cont}: Elemento {cont + 1}: {nomes[cont]}") #Imprime cada nome na tupla usando um loop for com range

for pos, nome in enumerate(nomes):
    print(f"Indice {pos}: Elemento {pos + 1}: {nome}") #Imprime cada nome na tupla usando um loop for com enumerate

lanche = ("Hambúrguer", "Batata Frita", "Refrigerante")

print(sorted(lanche)) #Imprime a tupla ordenada em ordem alfabética, mas não altera a tupla original
print(lanche) #Imprime a tupla original, que permanece inalterada


a = (2, 5, 3)
b = (5, 2, 3)
c = a + b
print(c)   #Imprime a tupla resultante da concatenação de a e b, que é (2, 5, 3, 5, 2, 3)
print(len(c)) #Imprime o número de elementos na tupla c, que é 6

print(c.count(5)) #Imprime o número de vezes que o elemento 5 aparece na tupla c, que é 2

print(c.index(3)) #Imprime o índice da primeira ocorrência do elemento 3 na tupla c, que é 2

print(c.index(5, 3)) #Imprime o índice da primeira ocorrência do elemento 5 na tupla c a partir do índice 3, que é 4

pessoa1 = ("João", 30, "Masculino")
pessoa2 = ("Maria", 25, "Feminino")

print(pessoa1) #Imprime a tupla pessoa1, que contém o nome, idade e gênero de João
print(pessoa2) #Imprime a tupla pessoa2, que contém o nome,

for pessoa in (pessoa1, pessoa2):
    print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]}, Gênero: {pessoa[2]}") #Imprime as informações de cada pessoa usando um loop for

del pessoa1 #Exclui a tupla pessoa1 da memória
# print(pessoa1) #Isso causará um erro, pois pessoa1 foi excluída da memória
#Você pode apagar uma tupla usando a palavra-chave del, mas não pode alterar os elementos de uma tupla após a criação.
  