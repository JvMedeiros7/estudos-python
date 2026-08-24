print ('-=' * 20)

r1= float(input('Primeiro segmento: '))
r2= float(input('Segundo segmento: '))
r3= float(input('Terceiro segmento: '))

if (r1+r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print ('Os segmento acima podem formar um triangulo')
    else:
        print ('Os segmentos acima não pode formar um triangulo')

    if r1 == r2 == r3:
        print ('Esse triangulo pode ser Equilatero')
    elif r1 != r2 != r3 != r1:
        print ('Esse triangulo pode ser Escaleno')
    else:
        print ('Esse triangulo é Isósceles')

