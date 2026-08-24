#tuplasguanabara.py

#Tuplas são estruturas de dados imutáveis em Python, ou seja, uma vez criada, não pode ser alterada.


lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for i in range(len(lanche)): #loop que percorre a tupla lanche usando o índice do Len 
    print(lanche[i]) #Aqui printa cada elemento da tupla lanche usando o índice i

for comida in lanche: #loop que percorre a tupla lanche diretamente
    print("Estas são as comidas:", comida) #Aqui printa cada elemento da tupla lanche diretamente

#variaveis compostas podem ser = () {} []

for pos, comida in enumerate(lanche): #loop que percorre a tupla lanche usando o enumerate para obter o índice e o valor
    print(f'Eu vou comer {comida} na posição {pos}') #Aqui printa cada elemento da tupla lanche e sua posição

for cont in range(len(lanche)-1, -1, -1): #loop que percorre a tupla lanche de trás para frente usando o índice do Len
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') #Aqui printa cada elemento da tupla lanche de trás para frente usando o índice cont

print(sorted(lanche)) #Aqui printa a tupla lanche em ordem alfabética usando a função sorted

print(lanche) #Aqui printa a tupla lanche original, que não foi alterada pela função sorted

a = (2, 5, 4) #Aqui cria uma tupla a com os valores 2, 5 e 4
b = (5, 8, 1, 2) #Aqui cria uma tupla b com os valores 5, 8, 1 e 2

print(a) #Aqui printa a tupla a
print(b) #Aqui printa a tupla b

c = a + b #Aqui cria uma tupla c com os valores da tupla a e b

print(c) #Aqui printa a tupla c, que é a junção das tuplas a e b

print(len(c)) #Aqui printa o tamanho da tupla c, que é a soma dos tamanhos das tuplas a e b

print(c.count(5)) #Aqui printa quantas vezes o valor 5 aparece na tupla c

print(c.index(8)) #Aqui printa o índice da primeira ocorrência do valor 8 na tupla c        

print(c.index(2, 4)) #Aqui printa o índice da primeira ocorrência do valor 2 na tupla c, começando a busca a partir do índice 4

pessoa = ('Gustavo', 39, 'M', 99.88) #Aqui cria uma tupla pessoa com os valores 'Gustavo', 39, 'M' e 99.88

#diferente de outras linguagens, em Python, tuplas podem conter diferentes tipos de dados, como strings, inteiros, floats, etc.

print(pessoa) #Aqui printa a tupla pessoa

print(pessoa[0]) #Aqui printa o primeiro elemento da tupla pessoa, que é 'Gustavo'  

#A tupla é imutavel mas podemos apagar a tupla

del(pessoa) #Aqui deleta a tupla pessoa

#print(pessoa) 
#Aqui tenta printar a tupla pessoa, mas como ela foi deletada, isso vai gerar um erro


