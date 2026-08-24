#Desafio 72 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

'''extenso = ( "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
            "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte" )

num = int(input("Digite um número entre 1 e 20: "))
if num < 1 or num > 20:
    print("Número inválido! Digite um número entre 1 e 20."),
else:
    print(f"O número {num} por extenso é: {extenso[num - 1]}")'''


#Desafio 73 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

'''tabela = ("Flamengo", "Internacional", "Atlético-MG", "São Paulo", "Fluminense",
          "Grêmio", "Palmeiras", "Santos", "Athletico-PR", "Bragantino", "Ceará", "Corinthians", "Atlético-GO", "Bahia", "Sport Recife", "Fortaleza", "Vasco da Gama", "Goiás", "Coritiba", "Chapecoense")
print("Os 5 primeiros times são: ", tabela[0:5])
print("Os últimos 4 colocados são: ", tabela[-4:])
print("Times em ordem alfabética: ", sorted(tabela))
print("A posição do time da Chapecoense é: ", tabela.index("Chapecoense") + 1)'''

#Desafio 74 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

'''import random

numeros = tuple(random.randint(1, 10) for _ in range(5))
print(f"Os números gerados são: {numeros}")
print(f"O menor valor é: {min(numeros)}")
print(f"O maior valor é: {max(numeros)}")'''

#Desafio 75 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: a) Quantas vezes apareceu o valor 9. b) Em que posição foi digitado o primeiro valor 3. c) Quais foram os números pares.

'''#Desafio 75 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: a) Quantas vezes apareceu o valor 9. b) Em que posição foi digitado o primeiro valor 3. c) Quais foram os números pares.

# Versão TRADICIONAL com for i in range(4):
lista.append(numero)
numeros1 = tuple(lista)
lista = []
for i in range(4):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista.append(numero)

numeros1 = tuple(lista)

print(f"Os números digitados foram: {numeros1}")
print(f"O número 9 apareceu {numeros1.count(9)} vezes.")

if 3 in numeros1:
    print(f"O primeiro 3 apareceu na posição {numeros1.index(3) + 1}")
else:
    print("O valor 3 não foi digitado")

pares = [n for n in numeros1 if n % 2 == 0]
print(f"Os números pares são: {pares}")


# =====================================================================
# Versão EXPRESS com Generator Expression (mais concisa)
# =====================================================================

print("\n" + "="*60)
print("VERSÃO EXPRESS COM GENERATOR EXPRESSION")
print("="*60 + "\n")

numeros2 = tuple(int(input("Digite um número: ")) for _ in range(4))
print(f"Os números digitados foram: {numeros2}")
print(f"O número 9 apareceu {numeros2.count(9)} vezes.")

if 3 in numeros2:
    print(f"O primeiro 3 apareceu na posição {numeros2.index(3) + 1}")
else:
    print("O valor 3 não foi digitado")

pares2 = [n for n in numeros2 if n % 2 == 0]
print(f"Os números pares são: {pares2}")


# Versão COM SEU CONHECIMENTO DE TUPLAS

# Lê 4 números e cria uma tupla

numero1 = int(input("Digite o 1º número: "))
numero2 = int(input("Digite o 2º número: "))
numero3 = int(input("Digite o 3º número: "))
numero4 = int(input("Digite o 4º número: "))

numeros = (numero1, numero2, numero3, numero4)

print(f"Os números digitados foram: {numeros}")

# Métodos de TUPLA
print(f"O número 9 apareceu {numeros.count(9)} vezes.")

if 3 in numeros:
    print(f"O primeiro 3 apareceu na posição {numeros.index(3) + 1}")
else:
    print("O valor 3 não foi digitado")'''

#Desafio 76 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ("Arroz", 5.50, "Feijão", 7.30, "Macarrão", 3.20, "Óleo", 4.80, "Açúcar", 2.90)

print("=" * 40)
print("LISTAGEM DE PREÇOS")
print("=" * 40)

for i in range(0, len(produtos), 2):
    produto = produtos[i]
    preco = produtos[i + 1]
    print(f"{produto:<20} R$ {preco:>6.2f}")    