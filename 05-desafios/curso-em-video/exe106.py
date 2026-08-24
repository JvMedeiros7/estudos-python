#Sistema - Interactive Help

c = ('\033[m',  # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[0;30;46m')  # 6 - ciano

def ajuda(com):
    help(com)

def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor] + '~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')



##Programa Principal

comando = ''

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        help(comando)

titulo('ATÉ LOGO!', 1)