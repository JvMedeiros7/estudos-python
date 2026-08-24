#Listas em Python

''' frutas = [ "Laranja" , "Maça" , "Uva"]
print(frutas)
print(frutas[0])
print(frutas[-1])

frutas = []
print(frutas)

letras = list("Python")
print(letras)
print(letras[0])
print(letras[-1])

numeros = list(range(10))
print(numeros)
print(numeros[0])
print(numeros[-1])

carro = [ "Ferrari" , "F8" , 42000 , 2020 , 2900 , "São Paulo" , True ]
print(carro)
print(carro[0])
print(carro[-1]) ''' 

#Matriz em Python

'''
 matriz = [
    [1, "a" , 2],
    ["b" , 3 , 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print([0][-1])
print([-1][-1]) '''

''' lista = ["p" , "y" , "t" , "h" , "o" , "n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

['t', 'h', 'o', 'n']
['p', 'y']
['y', 't']
['p', 't']
['p', 'y', 't', 'h', 'o', 'n']
['n', 'o', 'h', 't', 'y', 'p'] ''' 

#Forma de mostrar os elementos da lista padrão 

''' carros = ["Gol" , "Celta" , "Palio"]

for carro in carros:
    print(carro) ''' 

# Quando for necessário saber qual o índice do objeto dentro do laço FOR - Usamos a função Enumerate

''' carros = ["Gol" , "Celta" , "Palio"]

for indice, carro in  enumerate(carros):
    print(f"{indice} : {carro}") ''' 

#Compreensao de Listas - Criar nova lista com base nos valores de uma lista existente

''' numeros = [1, 30 , 21 ,2 , 9 , 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares) '''

#Compreensao de Listas - Versão Python

''' numeros = [1, 30 , 21 ,2 , 9 , 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares) ''' 

#Modificando valores - v1

''' numeros = [1, 30, 21 ,2 ,9 , 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2) ''' 


#Modificando valores - Versão Python

''' numeros = [1, 30, 21 ,2 ,9 , 65, 34]
quadrado = [ numero ** 2 for numero in numeros]

print(f"O número {numeros[0]} ao quadrado é {quadrado[0]}") ''' 


#Metodo para adicionar novo elemento na lista - []. Append

''' lista = []
lista.append(1)
lista.append("Python")
lista.append([40,30,20])

print(lista)
[1, 'Python', [40, 30, 20]] ''' 


#Metodo para limpar a lista - [].clear

''' lista = [1, "Python" , [40, 30, 20]]

print(lista)
[1, 'Python', [40, 30, 20]]

lista.clear()

print(lista)
[] ''' 

#Para copiar uma lista 

''' lista = [1, "Python" , [40, 30, 20]]

l2 = lista.copy()

print(lista)

print(id(l2) , id(lista))

l2[0] = 2 

#Conseguimos uma copia com os mesmos valores, mas podemos modificar sem alterar a lista original.

print(l2)
print(lista) ''' 

#Para contar a quantiadade que um objeto aparece na lista = [].count

''' cores = ["Vermelho" , "Azul" , "Verde" , "Azul"]
       
print(cores.count("Vermelho")) - 1 
print(cores.count("Azul")) - 2 ''' 

#Para passar uma 2a lista e juntar ela com a 1a = [].extend

''' linguagens = ["Python" , "Js" , "c"]

print(linguagens)
['Python', 'Js', 'c']

linguagens.extend(["Java" , "C"])

print(linguagens)
['Python', 'Js', 'c', 'Java', 'C'] ''' 

#Para saber onde é a 1a ocorrência do objeto - primeira vez onde ele vai aparecer = [].index

''' linguagens = ["Python" , "js" , "c" , "Java" , "csharp"]

print(linguagens.index("Java"))
print(linguagens.index("Python")) ''' 

#Tira o último elemento adicionado na lista = [].pop

''' linguagens = ["Python" , "Js" , "C" , "Java" , "csharp"]

print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())

#Pode-se usar para tirar elementos nos indices especificados
print(linguagens.pop(0))

print(linguagens) ''' 

# Remover elementos de uma lista = [].remove

''' linguagens = ["Python" , "Js" , "C" , "Java" , "Csharp"]

linguagens.remove("Python")

print(linguagens) ''' 

# Deixar a lista ao contrário do ÚLTIMO INDICE para o primeiro = [].reverse

''' linguagens = ["Python" , "Js" , "C" , "Java" , "Csharp"]

linguagens.rever()

print(linguagens) ''' 

# Ordena a lista em ordem alfabêtica

''' linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

#Ordena por tamanho da palavra :

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)


linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens) ''' 

# Para ver o tamanho dos objetos = [].len

''' linguagens = ["Python" , "Js" , "c" , "Java" , "csharp"]

print(len(linguagens)) # 5   
print(len(linguagens[0])) #6 ''' 
 
# Serve para ordenar iteráveis = [].sorted

''' linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"] ''' 




#Livro Python

'''z = [15 , 8 , 9]

print(z[0])

z[0] = 7 

print(z[0])'''

#Programa 6.2: Cálculo da média com notas digitadas

'''notas = [0, 0, 0, 0, 0, 0]
soma = 0 
x = 0 

while x < 6:
    notas[x] = float(input(f"Nota {x}:"))
    soma += notas[x]
    x += 1

x = 0 

while x > 6:
    print(f"Nota {x} : {notas[x]:6.2f}")
    x +=1 
 
print(f"media: {soma / len(notas):.2f}")'''

#Programa 6.3: Apresentação de Números

'''numeros = [0, 0, 0, 0, 0]
x = 0

while x < 5:
    numeros[x] = int(input(f"Números {x+1}:"))
    x += 1
while True:
    escolhido = int(input("Que posição você quer imprimir(0 para sair):"))
    if escolhido == 0:
        break
    print (f"Você escolheu o número: {numeros[escolhido - 1]}")'''

#Função Len

'''lista = [ 1 , 2 ,3 , 4, 5, 6 ]

print(len[lista])'''

#Podemos Usar a função len para controlar o limite dos índices:

'''L = [ 1 , 2 , 3 , 4 , 5 , 6 ]
x = 0 

while x < len(L):
    print(L[x])
    x += 1 
'''
#Função L.append[valor]

'''L = []

L.append("a")

print(L)'''


#Programa 6.6: Adição de elementos a lista

'''L = []
s = 0
while True:
    n = int(input("Digite um número(0 sai):"))
    if n == 0:
        break
    s += n 
    L.append(n)

x = 0 
while x < len(L):
    print(f"O números digitado fora na rodada {x+1} foi:" , L[x])
    x += 1 

print(f"A soma de todos os números foi: {s}")'''

#Podemos adicionar listas com + 

'''L = []

L = L + [1]

print(L)'''

#Expressão For = a cada repetição, o próximo elemento da lista se repete.

'''L = [1, 2, 3, 4, 5]
pos1 = []
for x in L:
    print(x)
    pos1.append(x)

print(pos1)'''

#Função Enumerate

'''L = [ 5, 9 , 13]
X = 0

for e in L:
    print(f"[{X+1}] {e}")
    X +=1'''

'''L = [ 5, 9 , 13]
for x, e in enumerate(L):
    print(f"[{x} {e}]")'''

'''L = [5, 9, 13]

for z in enumerate(L):
    # 'z' é a tupla, ex: (0, 5)
    # Aqui ocorre o desempacotamento:
    x, e = z 
    
    # x recebe a posição, e recebe o dado real
    print(f"Índice [{x}] contém o valor {e}")
    print(z)'''


#Impressão de uma lsita de string, letra a letra
'''
L = ["maças", "peras" , "Kiwis"]
for s in L:
    print(s)
    for letra in s:
        print(letra)
        if letra == "a":
            print("Você achou A")
'''
#Para acessar as listas

'''produto1 = ["maça", 10, 0.30]
produto2 = ["pera" , 5, 0.75]
produto3 = ["kiwi" , 4 , 0.98]
compras = [produto1 , produto2 , produto3]

print(compras[1][2]) #Acessar o 0.75 - preço do produto 2

for e in compras:
    print(e)
    print(f"Produto : {e[0]}")
    print(f"Quantidade : {e[1]}")
    print(f"Preço : {e[2]:5.2f}")'''

#Programa 6.19 

'''compras = []
rodando = True

while rodando == True:
    print("=" * 5 ,"CADASTRO DE PRODUTOS" , "=" * 5)
    produto = input("\nCADASTRE SEU PRODUTO:")
    quantidade = int(input("QUANTIDADE:"))
    preco = float(input("PREÇO DO PRODUTO: "))
    compras.append([produto , quantidade , preco])
    fim = input("QUER ENCERRAR O PROGRAMA? S / N: ")
    if fim == "S":
        rodando = False 
        break

soma = 0.0 
for e in compras:
    print(f"{e[0]:20s} x {e[1]:5d} {e[2]:5.2f} {e[1] * e[2]:6.2f}")
    soma += e[1] * e[2]

print(f"Total : {soma:7.2f}")'''

# Programa 6.20 : Ordenação pelo método de Bolhas - DESCRECENTE / CRESCENTE .

'''L = [1 , 2 , 3 , 4 , 5 ]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] < L[x + 1]: #ALTERAMOS O SINAL AQUI PARA SABERMOS SE É CRESCENTE OU DECRESCENTE 
            trocou = True
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] = temp
        x +=1
    if not trocou:
        break
    fim -= 1 
for e in L:
    print(e)
'''

'''L = [ 6, 4 , 2 , 1 , 9]
L.sort()
print(L)
sorted(L)
print(L)
'''
'''# ==============================================================================
# DEMONSTRAÇÃO PRÁTICA: .sort() vs sorted()
# ==============================================================================

# Cenário 1: Método .sort() -> Modificação In-place (Diretamente na Memória)
linguagens_projeto_a = ["python", "js", "c", "java", "csharp"]
retorno_sort = linguagens_projeto_a.sort() # Ordena a lista original

print("=== TESTANDO O MÉTODO .sort() ===")
print(f"Lista Original após .sort(): {linguagens_projeto_a}") 
print(f"O que o método retornou?: {retorno_sort}") 
# IMPACTO EM PRODUÇÃO: O retorno é estritamente None! 
# Se você fizer 'lista = lista.sort()', você destrói sua coleção de dados.

print("-" * 60)

# Cenário 2: Função sorted() -> Criação de um Novo Objeto (Imutabilidade)
linguagens_projeto_b = ["python", "js", "c", "java", "csharp"]
nova_lista_ordenada = sorted(linguagens_projeto_b) # Gera uma nova lista

print("=== TESTANDO A FUNÇÃO sorted() ===")
print(f"Lista Original após sorted(): {linguagens_projeto_b}") # Intacta!
print(f"Nova Lista Gerada: {nova_lista_ordenada}")
# IMPACTO EM PRODUÇÃO: Aloca um novo espaço de memória para a nova lista.


def insertion_sort(lista):
    # Começamos do segundo elemento (índice 1), pois o primeiro já é considerado "ordenado"
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        
        # Desloca os elementos que são maiores que a chave para uma posição à frente
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
            
        # Insere a chave na sua posição correta
        lista[j + 1] = chave
    return lista

# Execução na IDE
dados = [5, 2, 9, 1, 5, 6]
print(f"Insertion Sort Resultado: {insertion_sort(dados)}")

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
        
    # Abordagem de fatiamento (slicing) estudada na Aula 01 / [Dio] Listas
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    
    return merge(esquerda, droite=direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    
    # Compara os elementos de ambas as sublistas e os combina em ordem
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
            
    # Adiciona os elementos restantes de ambas as listas
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

# Execução na IDE
dados = [38, 27, 43, 3, 9, 82, 10]
print(f"Merge Sort Resultado: {merge_sort(dados)}")

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        # Escolha do pivô (neste caso, o elemento central)
        pivo = lista[len(lista) // 2]
        
        # Particionamento usando compreensões de lista (Aula 01 / [Dio] Listas)
        menores = [x for x in lista if x < pivo]
        iguais  = [x for x in lista if x == pivo]
        maiores = [x for x in lista if x > pivo]
        
        return quick_sort(menores) + iguais + quick_sort(maiores)

# Execução na IDE
dados = [10, 7, 8, 9, 1, 5]
print(f"Quick Sort Resultado: {quick_sort(dados)}")'''

