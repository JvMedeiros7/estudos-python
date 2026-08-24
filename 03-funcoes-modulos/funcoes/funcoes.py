'''#Funções é um arquivo que contém funções auxiliares para o projeto.

# def palavra reservada para definir uma função

# Função para somar dois números

def somar(a, b):
    return a + b

# Função para subtrair dois números
def subtrair(a, b):
    return a - b

# Função para multiplicar dois números
def multiplicar(a, b):
    return a * b

# Função para dividir dois números
def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

while True:
    opção = input("Escolha uma operação (1.somar, 2.subtrair, 3.multiplicar, 4.dividir): ")
    if opção in ['1', '2', '3', '4']:
        if opção == '1':
            resultado = somar(num1, num2)
            print(f"O resultado da soma é: {resultado}")
        elif opção == '2':
            resultado = subtrair(num1, num2)
            print(f"O resultado da subtração é: {resultado}")
        elif opção == '3':
            resultado = multiplicar(num1, num2)
            print(f"O resultado da multiplicação é: {resultado}")
        elif opção == '4':
            resultado = dividir(num1, num2)
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Opção inválida. Por favor, escolha uma operação válida.")
    decisao_sair = input("Deseja realizar outra operação? (s/n): ")
    if decisao_sair.lower() != 's':
        print("Encerrando o programa.")
        break'''

#Funções estão vinculados a rotinas específicas, mas podem ser reutilizados em diferentes partes do código, promovendo a modularidade e a clareza do programa.

#Exemplo de função sem parametros, que apenas exibe linhas de separação no console.

'''def mostrar_linhas():
    print("===================================")
    print("\n===================================")

mostrar_linhas()

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

mostrar_linhas()

print("Escolha uma operação:")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

mostrar_linhas()'''

#Rotina programada para mostrar linhas de separação no console, melhorando a legibilidade do programa.

#Parametros é um arquivo que contém funções auxiliares para o projeto.

#Exemplo de função com parametros, que recebe um texto e exibe linhas de separação no console.

'''def titulo(txt):
    print("===================================")
    print(txt)
    print("===================================")

#Programa Principal 

titulo("Calculadora Simples")
titulo("Escolha uma operação:")
titulo("1. Somar")
titulo("2. Subtrair")
titulo("3. Multiplicar")
titulo("4. Dividir")'''

#Funções servem para códigos grandes, repetitivos, ou que precisam ser reutilizados em diferentes partes do programa, promovendo a modularidade e a clareza do código.

'''def mostrar_linhas():
    print("===================================")
    print("\n===================================")

def somar(a, b):
    print(f"Somando {a} + {b} = {a + b}")
    return a + b

def subtrair(a, b):
    print(f"Subtraindo {a} - {b} = {a - b}")
    return a - b

def multiplicar(a, b):
    print(f"Multiplicando {a} * {b} = {a * b}")
    return a * b

def dividir(a, b):
    if b == 0:
        print("Erro: Divisão por zero não é permitida.")
        return None
    print(f"Dividindo {a} / {b} = {a / b}")
    return a / b

mostrar_linhas()
somar(10,12)
mostrar_linhas()
subtrair(10,12)
mostrar_linhas()
multiplicar(10,12)
mostrar_linhas()
dividir(10,12)'''

#Se eu digo na definição da função que ela recebe parametros, então eu preciso passar esses parametros na hora de chamar a função, caso contrário, o programa vai gerar um erro.

# Se eu falar que é A, B e na hora de chamar a função eu passar C, D, o programa vai gerar um erro, pois ele não vai saber o que fazer com C e D, pois ele espera A e B.


'''def contador(*num):
    print("Ele cria tuplas com os números passados como argumentos.")
    print(num)
    for valor in num:
        print(f"{valor} ", end="")
    print("Fim!")
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números.")

contador(1, 2, 3, 4, 5)
contador(10, 20, 30)
contador(100, 200, 300, 400, 500, 600)'''


'''def dobra(lst):
    pos = 0
    for i in lst:
        print(f"Valor original: {i}, Valor dobrado: {i * 2}")
    print("Valores dobrados:", lst)

valores  = [7, 2, 5, 0, 4]
dobra(valores)'''

'''def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}")

soma(5, 2)
soma(2, 9, 4)'''

