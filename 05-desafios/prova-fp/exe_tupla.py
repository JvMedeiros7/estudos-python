#Desafio 072

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input("Digite um número entre 0 e 20: "))
    if 0 <= n <= 20:
        break
    print("Tente novamente. ", end="")
print(f"Você digitou o número {numero[n]}")


#Desafio 073

tabela = ('Atlético-MG', 'Flamengo', 'Internacional', 'Fluminense', 'Corinthians', 'São Paulo', 'Bahia', 'Vasco da Gama', 'Atlético-PR', 'Sport Recife', 'Fortaleza', 'Ceará SC', 'Botafogo', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí', 'Grêmio', 'Palmeiras', 'Santos')

print("Os 5 primeiros colocados são: ")
for c in range(0, 5):
    print(f"{c + 1}º {tabela[c]}")
print("\nOs 4 últimos colocados são: ")
for c in range(16, 20):
    print(f"{c + 1}º {tabela[c]}")
print("\nOs times em ordem alfabética são: ")
print(sorted(tabela))

print(f"\nO time Chapecoense está na {tabela.index('Chapecoense') + 1}ª posição.")