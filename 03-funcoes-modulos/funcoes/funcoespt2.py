#Ajuda Interativa - help()


'''help(input) #Exibe a documentação da função print

print(input.__doc__) #Exibe a documentação da função input'''

'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do Curso em Vídeo
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

contador(2, 10, 2)'''

'''def somar(a = 0,b = 0, c = 0):
    """
    -> Faz a soma de dois valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    Função criada por Gustavo Guanabara do Curso em Vídeo
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)'''

'''def teste():
    x = 8
    print(f'na função teste n vale {n}')
    print(f'na função teste x vale {x}') #Váriavel Local - Escopo Local

#Programa principal

n = 2 #Váriavel Global - Escopo Global 

print(f'No programa principal n vale {n}')

teste()'''

'''def somar (a = 0, b = 0, c = 0):
    s = a + b + c
    return s #armazena a soma na variável s e retorna o valor para a função

r1 = somar(3, 2, 5) #Coloca o valor retornado pela função na variável r1
r2 = somar(2, 2) #Coloca o valor retornado pela função na variável r2
r3 = somar(6) #Coloca o valor retornado pela função na variável r3

print(f'As somas deram {r1}, {r2} e {r3}')'''

'''
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número para calcular seu fatorial: '))
print(f'O fatorial de {n} é {fatorial(n)}')'''

def parouimpar (n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if parouimpar(num):
    print(f'O número {num} é PAR!')
else:
    print(f'O número {num} é ÍMPAR!')