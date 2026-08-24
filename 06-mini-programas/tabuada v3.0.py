while True:
    n = int(input('Quer ver tabuada de qual valor ? '))
    print ('_' * 20 )
    for c in range (1,33):
        if n < 0:
            break
        print (f'{n} x {c} = {n * c}')
    print('_' * 20)
print ('Programa tabuada encerrada!')