#Função contador()

def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:")
    for i in range(inicio, fim + 1, passo):
        print(i, end=' ')
    print()  # Para pular uma linha após a contagem
    if passo < 0:
        print("Contagem regressiva:")
        for i in range(inicio, fim - 1, passo):
            print(i, end=' ')
        print()  # Para pular uma linha após a contagem
    elif passo > 0:
        print("Contagem progressiva:")
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
        print()  # Para pular uma linha após a contagem
    else:
        if passo == 0:
            passo = 1  # Evita passo zero, que causaria um loop infinito

inicio = int(input("Digite o valor inicial da contagem: "))
fim = int(input("Digite o valor final da contagem: "))
passo = int(input("Digite o valor do passo da contagem: "))

contador(inicio, fim, passo)