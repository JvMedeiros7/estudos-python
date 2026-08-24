#Módulos e pacotes 

#Módulos são arquivos Python que contêm definições e instruções. Um módulo pode definir funções, classes e variáveis, e também pode incluir código executável.

#Servem para dividir um programa em partes menores e mais gerenciáveis, promovendo a reutilização de código e a organização do projeto.

#Pacotes são diretórios que contêm múltiplos módulos e um arquivo __init__.py. Os pacotes permitem organizar módulos de forma hierárquica, facilitando a manutenção e o uso do código.

def fatorial(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


num = int(input('Digite um número: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')


