#Exceções - São erros que acontecem durante a execução do programa, e que podem ser tratados para evitar que o programa seja interrompido de forma inesperada.

#Exceções são uma forma de lidar com erros que podem ocorrer durante a execução do programa, permitindo que o programa continue rodando mesmo quando um erro é encontrado.

'''print(x) #NameError: name 'x' is not defined'''

'''n = input("Digite um número: ") #ValueError: invalid literal for int() with base 10: 'abc'
print(f'O número digitado foi: {int(n)}')

#Key error - ocorre quando tentamos acessar uma chave que não existe em um dicionário.
dicionario = {'nome': 'João', 'idade': 30}
print(dicionario['email']) #KeyError: 'email'

#Index error - ocorre quando tentamos acessar um índice que não existe em uma lista.
lista = [1, 2, 3]
print(lista[3]) #IndexError: list index out of range

#ZeroDivisionError - ocorre quando tentamos dividir um número por zero.
x = 10
y = 0
print(x / y) #ZeroDivisionError: division by zero

#FileNotFoundError - ocorre quando tentamos abrir um arquivo que não existe.
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read() #FileNotFoundError: [Errno 2] No such file or directory: 'arquivo.txt'

'''


##Prática exceção 

try: #Obrigatório - executa o código que pode gerar uma exceção

    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    c = a / b

except Exception as e: #Obrigatório - executa caso ocorra uma exceção

    print(f"Ocorreu um erro: {e.__class__} e o erro foi {e}") #Exibe o tipo da exceção

else: #Opcional - executa caso não ocorra nenhuma exceção

    print(f"O resultado da divisão é: {c}")

finally: #Opcional - executa sempre, independente se ocorreu ou não uma exceção

    print("Fim do programa.")


##Tratamento de erros é essencialmente importante para o programa. 
