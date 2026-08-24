# Set - Elimina valores duplicados numa lista 

''' lista = [1, 2, 3, 4, 5, 5 , 6, 7, 7, 8, 8 ]

print(set(lista))

letras = set("Abacaxi")
print(letras)

repetidas = set(input("Qual valor você quer?"))
print(repetidas) ''' 

#Não suportam indexação e nem fatiamento - Caso queira Acessar os seus valores é necessário converter o conjunto para lista

''' numeros = {1,2,3,2}

numeros = list(numeros)

print(numeros[0]) ''' 

#Uso do For em set

''' carros = {"Gol" , "Celta" , "Palio" }

for indice, carro in enumerate(carros):
    print(f"{indice} : {carro}"  ) ''' 

#Metodos de Classe do SET

#{}.union

''' conjunto_a = {1,2}
conjunto_b = {3,4}

print(conjunto_a.union(conjunto_b)) #{1, 2, 3, 4} ''' 

#{}.intersection

''' conjunto_a = {1,2, 3}
conjunto_b = {2, 3,4}

print(conjunto_a.intersection(conjunto_b)) ''' 

#{}.difference

''' conjunto_a = {1,2, 3}
conjunto_b = {2, 3,4}

print(conjunto_a.difference(conjunto_b)) #1
print(conjunto_b.difference(conjunto_a)) #4 ''' 

#{}.difference

''' conjunto_a = {1,2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b)) # 1 , 4 ''' 

#{}.issubset - Se todos de a tem em B = TRUE

''' conjunto_a = {1,2, 3}
conjunto_b = {1, 2, 3, 4}

print(conjunto_a.issubset(conjunto_b)) #True ''' 

#{}.issuperset- Se todos de B tem em A = FALSE 

''' conjunto_a = {1,2, 3}
conjunto_b = {1, 2, 3, 4}

print(conjunto_a.issuperset(conjunto_b)) #False ''' 

#{}..isdisjoint = Se os valores não se tocam = TRUE

''' conjunto_a = {1,2, 3, 4, 5 }
conjunto_b = {6, 7, 8, 9}
conjunto_C = {1,0}

print(conjunto_a.isdisjoint(conjunto_b)) #True ''' 

#{}.add - Posso passar um elemento se ele não existir é selecionado 

''' sorteio = {1, 23}

sorteio.add(25)

print(sorteio) ''' 

#{}.clear - Posso passar um elemento se ele não existir é selecionado 

''' sorteio = {1, 23}

sorteio.clear()

print(sorteio) ''' 


#{}.copy - Copia os elementos do set  

''' sorteio = {1, 23}

sorteio.copy()

print(sorteio) ''' 

#{}.discard - Descarta valores especifícos - Ignora erros - bom para erros que não gerem problemas maiores

''' numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros)

numeros.discard(1)
numeros.discard(45)

print(numeros) ''' 

#{}.pop - Descarta valores 1 a 1 

''' numeros = {1,2,3,4,5,6,7,8,9,0}

print(numeros)

print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())

print(numeros) ''' 

#{}.remove - Não ignora erros - KeyERROR se não tiver o elemento

''' numeros = {1,2,3,4,5,6,7,8,9,0}

print(numeros)

numeros.remove(2)

print(numeros) ''' 

#{}.len - Para tirar o tamanho do nosso conjunto 

''' numeros = {1,2,3,4,5,6,7,8,9,0}

print(len(numeros)) '''

#{}.in - Verificar se um elemento está dentro do conjunto

''' numeros = {1,2,3,4,5,6,7,8,9,0}

print(1 in numeros)
print(10 in numeros) ''' 

'''# SOLUÇÃO DEFINITIVA EM PRODUÇÃO (Itens 1 ao 4)
E = [1, 2, 6, 8]
F = [3, 6, 8, 9]

var1 = set(E)
var2 = set(F)

# 1. Valores comuns às duas (Interseção pura, não união)
comuns = var1.intersection(var2)
print(f"1. Valores comuns: {comuns}") 
# Saída IDE: {8, 6}

# 2. Valores que só existem na primeira (Diferença direta)
dif1 = var1.difference(var2)
print(f"2. Só na primeira: {dif1}") 
# Saída IDE: {1, 2}

# 3. Valores que só existem na segunda (Diferença direta)
dif2 = var2.difference(var1)
print(f"3. Só na segunda: {dif2}") 
# Saída IDE: {9, 3}

# 4. Lista com os elementos não repetidos das duas listas (Diferença Simétrica)
nao_repetidos = var1.symmetric_difference(var2)
print(f"4. Não repetidos nas duas: {nao_repetidos}") 
# Saída IDE: {1, 2, 3, 9}

item_5 = var1.difference(var2)
print(f"5. A primeira sem os repetidos na segunda: {item_5}")
# Saída IDE: {1, 2}'''

ANTES = [1, 2, 5, 6, 9]
DEPOIS = [1, 2, 8, 10]

conjunto_1 = set(ANTES)
conjunto_2 = set(DEPOIS)

#Elementos que estão em antes que precisam estar em depois

nao_mudou = conjunto_1.intersection(conjunto_2)
print(f"Os elementos que não mudaram foram: {nao_mudou}")

#Novos elementos 

novos = conjunto_2.difference(conjunto_1)
print(f"Os elementos novos foram: {novos}")

#Elementos que foram removidos

removidos = conjunto_1.difference(conjunto_2)
print(f"Os elementos removidos foram: {removidos}")


ANTES = [1, 2, 5, 6, 9]
DEPOIS = [1, 2, 8, 10]

conjunto_antes = set(ANTES)
conjunto_depois = set(DEPOIS)

# Conjuntos suportam o operador & para realizar a interseção, ou seja,
# A & B resulta no conjunto de elementos presentes em A e B
print(f"Antes: {ANTES}")
print(f"Depois: {DEPOIS}")
print(f"Elementos que não mudaram: {sorted(conjunto_antes & conjunto_depois)}")
print(f"Elementos novos: {sorted(conjunto_depois - conjunto_antes)}")
print(f"Elementos que foram removidos: {sorted(conjunto_antes - conjunto_depois)}")