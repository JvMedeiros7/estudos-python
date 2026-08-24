#Exercicio 4.5 

''' idade = int(input("Digite a idade de seu carro:"))

if idade <= 3:
    print("Seu carro é novo.")
else:
    print("Seu carro é velho.") '''

#Exercicio 4.6

''' distkm = float(input("Qual distância você deseja percorrer em Km?")) 

if distkm <= 200:
    passagem = distkm * 0.50
    print(f" O valor da sua passagem é: R$ {passagem}")
else:
    passagem = distkm * 0.45
    print(f" O valor da sua passagem é: R$ {passagem}") ''' 

#Exercicio 4.3.7 

''' n1 = float(input("Digite n1:"))
n2 = float(input("Digite n2:"))
n3 = float(input("Digite n3:"))

if n1 > n3 and n1 > n2:
    print("N1 É O MAIOR DE TODOS!!")
if n2 > n3 and n2 > n1:
    print("N2 É O MAIOR DE TODOS!!")
else:
    print ("N3 É O MAIOR!!") ''' 

#Exercicio 4.8 

''' plano = input("Qual seu plano de celular?")
if plano == "falopouco":
    minutos_no_plano= 100
    extra = 0.20
    preco = 50
if plano == "falomuito":
    minutos_no_plano= 500
    extra = 0.15
    preco = 99
else: 
    print("Não conheço este plano")

if plano == "falopouco" or plano == "falomuito":
    minutos_consumidos = int(input("Quantos minutos você consumiu?"))
    print(f"Você vai pagar: PREÇO DO PLANO / R$ {preco} " )
    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
    print(f"Suplemento     R$ {suplemento:10.2f}")
    print(f"Total          R$ {preco + suplemento:10.2f}") ''' 

#Exercicio 4.10 

''' n1 = float(input("Digite n1:"))
n2 = float(input("Digite n2:"))

escolha = int(input("Você quer somar (1), subtrair (2), multiplicar (3) ou dividir (4)?"))

if escolha == 1:
    soma = n1 + n2 
    print(f" A soma de  {n1} + {n2} é igual a: {soma}")
elif escolha == 2:
    if n1 >= n2:
        subtrair = n1 - n2
        print(f" A subtração de  {n1} - {n2} é igual a: {subtrair:10.2f}")
    else:
        subtrair = n2 - n1
        print(f" A subtração de {n2} - {n1} é igual a: {subtrair:10.2f}")

elif escolha == 3:
    multiplicar = n1 * n2 
    print(f" A multiplicação de {n1} * {n2} é igual a {multiplicar:10.2f}")

elif escolha == 4:
    dividir = n1/n2 
    print (f"A divisão de {n1} / {n2} é igual a {dividir:10.2f}")
    
else:
    print("Opção inválida! Escolha entre 1 e 4.") ''' 

#Exercicio 4.11

''' valor_da_casa = float(input("Qual o valor da casa que você deseja comprar?"))
salario = float(input("Qual o valor do seu salário?"))
anos = float(input("Em quantos anos você deseja parcelar?"))

meses = anos * 12 

parcela = valor_da_casa / meses

sal30 = salario * 0.3

if parcela > sal30:
    print(f"Indisponível o parcelamento da sua compra, visto que 30 porcento do seu salário é {sal30:.2f} e o valor da parcela é {parcela:.2f}")
else:
    print(f"O valor da sua casa é {valor_da_casa} e parcelado em {meses} meses, fica: R$  {parcela:.2f}") ''' 

#Exercicio 4.12

''' qtdekw = float(input("Qual a quantidade de kWh consumido?"))
instal = input("Qual o tipo de instalação? R - RESIDÊNCIA / I - INDUSTRIAS / C - COMÉRCIOS ")

preco1 = 0 

if instal == "R" :
    if qtdekw <= 500:
        preco1 = qtdekw * 0.40
        print(f"A sua conta deu {preco1}")
    elif qtdekw > 500:
        preco1 = qtdekw * 0.65
        print(f"A sua conta deu {preco1}")

elif instal == "C" :
    if qtdekw <= 1000:
        preco1 = qtdekw * 0.55
        print(f"A sua conta deu {preco1}")
    elif qtdekw > 1000:
        preco1 = qtdekw * 0.60
        print(f"A sua conta deu {preco1}")

elif instal == "I" :
    if qtdekw <= 5000:
        preco1 = qtdekw * 0.55
        print(f"A sua conta deu {preco1}")
    elif qtdekw > 5000:
        preco1 = qtdekw * 0.60
        print(f"A sua conta deu {preco1}")

else:
    print("Dados invalidos, tente um das 3 opções") ''' 

#Exercicio 4.13

''' a = int(input("Digite o seu n1:"))
b = int(input("Digite o seu n2:"))

if b > a :
    print("B é Maior que A")
else: 
    print("A é maior que B") ''' 

#Exercicio 4.14

''' a = int(input("Qual o valor de (A) ? "))

if a < 10:
    print("A é menor que 10.")

elif a >= 10 and a < 20:
    print("A é maior que 10 e menor que 20.")

else: 
    print("A é maior que 20.") ''' 

#Exercicio 4.15

''' hora = int(input("Digite a hora atual:"))

if hora < 12:
    print("Bom dia!")
elif hora >= 12 and hora <= 18:
    print("Boa tarde!")
else:
    print("Boa noite!") ''' 

#Exercicio 4.16

''' media = float(input("Qual a sua média?"))

if media >= 7:
    print("Você passou de ano!!")

elif media < 7 and media > 4:
    print("Você está de recuperação!")

else:
    print("Você está reprovado!") ''' 