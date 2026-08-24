#Função maior()

from random import randint

def lin():
    print('-' * 30)

def maior():
    #Geração de números
    num_final = int(input("Digite quantos números deseja gerar: "))
    lin()
    rodadas = int(input("Digite quantas rodadas deseja realizar: "))
    lin()
    for i in range(1, rodadas + 1):
        print(f"Rodada {i}")
        lin()
        numeros = [randint(1, num_final) for _ in range(rodadas)]
        print("Números gerados:", numeros)  
        lin()
        maior_numero = max(numeros)
        print(f"O maior número gerado é: {maior_numero}")


maior()