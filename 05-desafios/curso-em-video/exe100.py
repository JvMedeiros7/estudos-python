from random import randint
numeros_sorteados = []
tot_par = 0
lista_par = []

for i in range(6):
    numeros_sorteados.append(randint(1, 10))
print(numeros_sorteados)

for c, n in enumerate(numeros_sorteados):
    print(f' O número {n} saiu na posição {c}')
    if n % 2 == 0:
        lista_par.append(n)
        tot_par += n

print(f'A soma dos números pares sorteados é {tot_par}')
print(f'Os números pares sorteados foram {lista_par}')



