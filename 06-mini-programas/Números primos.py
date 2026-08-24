n1=int(input('Qual número você quer checar?'))

totdivisores = 0

for c in range(1, n1+1):
    if n1 % c == 0:
        print (f'Esse número é dividido por {c}')
        totdivisores += 1
print(f'O número de {n1} foi divisível {totdivisores} vezes')
if totdivisores == 2:
    print ('Esse número é primo')
else:
    print ('Esse número não é primo')

