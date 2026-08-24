from pacote_uteis import fatorial, dobro, triplo, mostrar_linha

print("Calculadora de Fatorial, Dobro e Triplo")

mostrar_linha()

num = int(input("Digite um número para calcular o fatorial: "))

mostrar_linha()

fat = fatorial(num)

for i in range(num, 0, -1):
    if i == 1:
        print(f"{i} = ", end="")
    else:
        print(f"{i} x ", end="") 


print(f"O fatorial de {num} é {fat}.")
print(f"O dobro de {num} é {dobro(num)}.")
print(f"O triplo de {num} é {triplo(num)}.")

mostrar_linha()


#vantagens modularização: reaproveitamento de código, organização, manutenção mais fácil, legibilidade, colaboração em equipe, testes e depuração mais simples.

