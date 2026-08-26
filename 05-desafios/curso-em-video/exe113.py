#Validação de Dados


while True:
    try:
        n_int = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Erro: Você não digitou um número inteiro. Tente novamente.")
    except KeyboardInterrupt:
        print("\nEntrada interrompida pelo usuário.")
        n_int = 0
        break
    else:
        break

while True:
    try:
        n_float = float(input("Digite um número decimal: "))
    except ValueError:
        print("Erro: Você não digitou um número decimal. Tente novamente.")
    except KeyboardInterrupt:
        print("\nEntrada interrompida pelo usuário.")
        n_float = 0
        break
    else:
        break

print(f"Você digitou o número inteiro: {n_int} e o número decimal: {n_float}")