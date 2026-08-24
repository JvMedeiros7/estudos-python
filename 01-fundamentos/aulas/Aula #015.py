n = cont = 0
s = 0
while True:
    n = int(input(f'{cont}o. digite um numero: '))
    if n == 999:
        break    cont += 1
    s += n
print (f'A soma é {s}')