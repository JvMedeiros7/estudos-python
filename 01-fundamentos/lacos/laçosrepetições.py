#Exercicio 5.1 

''' x = 1 
while x <= 100:
    print(x)
    x = x + 1  ''' 

#Exercicio 5.2

''' x = 50
while x <= 100:
    print(x)
    x = x + 1  ''' 

#Exercicio 5.3

''' x = 10
while x >= 1:
    print(f" A conta regressiva está em {x} !!!!")
    x = x - 1  ''' 

#Exercicio 5.4

''' fim = int(input("Digite o último número a imprimir:"))
x = 1 
while x <= fim:
    print (x)
    x = x + 2  ''' 

#Exercicio 5.5

''' x = 3 
while x <= 30:
    print (x)
    x = x + 3 ''' 

#Exercicio 5.6.7.

''' n = int(input("Tabuada de:"))
limite = int(input("Digite o n° de até onde vai ser a tabuada?"))
x = 1 
while x <= limite:
    tabuada = n * x 
    print(f"O resultado da tabuada é {x} x {n} = {tabuada}")
    x = x + 1  ''' 

#Exercicio 5.8 

''' n1 = int(input("Digite o n1: "))
n2 = int(input("Digite o n2: "))

soma = 0  
contador = 1  


while contador <= n2:
    soma = soma + n1  
    contador = contador + 1 

print(f"O resultado de {n1} x {n2} é: {soma}") ''' 

#Exercicio 5.9 

''' dividendo = int(input("Digite o dividendo (n1): "))
divisor = int(input("Digite o divisor (n2): "))


n1 = dividendo
n2 = divisor

quociente = 0
resto = n1

# Enquanto o que sobrou for maior ou igual ao divisor...
while resto >= n2:
    resto = resto - n2  # Subtraímos o divisor
    quociente = quociente + 1  # Contamos quantas vezes subtraímos

print("-" * 30)
print(f"Dividindo {n1} por {n2}:")
print(f"Quociente (divisão inteira): {quociente}")
print(f"Resto da divisão: {resto}")  ''' 

#Exercicio 5.10

''' pontos = 0 
q = 1

while q <= 3:
    res = input(f"Resposta da questão {q}: ").strip().upper()
    
    if q == 1 and res == "B":
        pontos += 1 
    elif q == 2 and res == "A":
        pontos += 1 
    elif q == 3 and res == "C":
        pontos += 1
        
    q += 1 

print("-" * 20)
print(f"Resultado final: {pontos} ponto(s).") ''' 


#Exercicio 5.11

'''

x = 1
total = 0
jurostot = 0

dep_inicial = float(input("Qual seu deposito inicial?"))
taxa_juros = float(input("Qual a taxa de juros da sua poupança?"))

valor_juros = (taxa_juros * 0.01)

while x <= 24:
    juros = dep_inicial * valor_juros
    valor_tot1 = juros + dep_inicial
    jurostot = juros + jurostot
    print(f"MÊS {x}:")
    x = x + 1 
    total = valor_tot1 + total
    print(f"O seu total na conta esse mês é {total}")
    print(f"Você ganhou de juros até agora o valor total de: {jurostot}\n")

print("--" * 20 )
print (" --- VALORES TOTAIS ---")
print(f"Somando todos os seus ganhos foram R$ {total}")
print(f"Somando todos os seus juros foram R$ {jurostot}")

'''

#Exercicio 5.12 - Contador de Juros Compostos 

''' mes = 1
jurostot = 0

dep_inicial = float(input("Qual seu deposito inicial?"))
taxa_juros = float(input("Qual a taxa de juros da sua poupança?"))

valor_juros = (taxa_juros * 0.01)
saldo_atual = dep_inicial

while mes <= 24:
    valormes = float(input("\nQual o valor depositado no mês?\n"))
    
    saldo_atual = saldo_atual + valormes

    juros_mes = saldo_atual * valor_juros

    jurostot = juros_mes + jurostot

    saldo_atual = juros_mes + saldo_atual

    print(f"\n MÊS {mes}: \n ")
    mes = mes + 1 
    print(f"O seu total na conta esse mês é {saldo_atual:.2f}")
    print(f"Você ganhou de juros até agora o valor total de: {jurostot:.2f}\n")


print("--" * 20 )
print (" --- VALORES TOTAIS ---")
print(f"Somando todos os seus ganhos foram R$ {saldo_atual:.2f}")
print(f"Somando todos os seus juros foram R$ {jurostot:.2f}") ''' 

#Exercicio 5.13 - Contador de Dívidas com Juros

''' # --- Variáveis Iniciais ---
mes = 1
total_pago = 0
jurostot = 0

valordivida = float(input("VALOR DA DÍVIDA: "))
taxajuros = float(input("TAXA DE JUROS MENSAL (em %): "))
valorpgto = float(input("Qual valor de pagamento mensal? "))


jurosmensal_taxa = taxajuros / 100


if valorpgto <= (valordivida * jurosmensal_taxa):
    print("\n[!] Atenção: Seu pagamento é menor ou igual aos juros.")
    print("Dessa forma, a dívida nunca será paga!")
else:
    while valordivida > 0:
        # 1. Calcula o juros do mês sobre a dívida atual
        juros_do_mes = valordivida * jurosmensal_taxa
        
        # 2. Acumula o total de juros pagos para o relatório
        jurostot = jurostot + juros_do_mes
        
        # 3. A dívida aumenta com os juros
        valordivida = valordivida + juros_do_mes
        
        # 4. Verificação para o último mês (não pagar mais do que deve)
        if valorpgto > valordivida:
            pagamento_real = valordivida
        else:
            pagamento_real = valorpgto
            
        # 5. Subtrai o pagamento da dívida
        valordivida = valordivida - pagamento_real
        
        # 6. Acumula o total que saiu do seu bolso
        total_pago = total_pago + pagamento_real
        
        print(f"Mês {mes}: Dívida restante: R$ {valordivida:.2f}")
        
        mes = mes + 1

    # --- Resultados Finais ---
    print("\n" + "--" * 20)
    print(" --- RELATÓRIO DE QUITAÇÃO ---")
    print(f"Meses para pagar: {mes - 1}")
    print(f"Total pago (Dinheiro total): R$ {total_pago:.2f}")
    print(f"Total de juros pagos (Taxas): R$ {jurostot:.2f}")
    print("--" * 20) ''' 

#Exercicio 5.14 

''' s = 0
x = 0

while True:
    nint = float(input("\nDIGITE UM NÚMERO PARA SOMAR E FAZER A MÉDIA:               / (DIGITE 0 PARA SAIR)")) 
    if nint == 0:
        break
    s += nint 
    x += 1 
print(f"Soma dos números digitados {s}" )
print(f"Quantidade de números digitados {x}")

media = s/x

print(f"A media dos números digitados é {media}") ''' 


# Exercício 5.15 - Sistema de Vendas Organizado

''' s = 0        
p1, x1 = 0.50, 0
p2, x2 = 1.00, 0
p3, x3 = 4.00, 0
p5, x5 = 7.00, 0
p9, x9 = 8.00, 0

while True:
    produto = int(input("Qual produto você deseja? 1/2/3/5/9 (0 para sair): "))
    
    if produto == 0:
        break

    if produto in [1, 2, 3, 5, 9]:
        qtde = int(input(f"Quantidade do produto {produto}: "))
        
        if qtde < 0:
            print("Quantidade inválida! Use números positivos.")
            continue


        if produto == 1:
            s += p1 * qtde
            x1 += qtde
        elif produto == 2:
            s += p2 * qtde
            x2 += qtde
        elif produto == 3:
            s += p3 * qtde
            x3 += qtde
        elif produto == 5:
            s += p5 * qtde
            x5 += qtde
        elif produto == 9:
            s += p9 * qtde
            x9 += qtde
    else:
        print("Código inválido! Tente novamente.")


print("-" * 30)
print(f"FECHAMENTO DO CAIXA")
print(f"Total da compra: R$ {s:.2f}")
print(f"Quantidades: Prod 1: ({x1}) | Prod 2: ({x2}) | Prod 3: ({x3}) | Prod 5: ({x5}) | Prod 9: ({x9})")
print("-" * 30)77 ''' 

#Programa 5.1

''' valor = float(input("Digite o valor a pagar: "))
atual = 100 
apagar = valor

while apagar > 0.0001:
    cedulas = 0

    while atual <= apagar + 0.00001:
        apagar -= atual
        cedulas += 1

    if cedulas > 0:
        print(f"{cedulas} de R$ {atual:.3f}")

    if atual == 100:
        atual = 50
    elif atual == 50:
        atual = 20
    elif atual == 20:
        atual = 10
    elif atual == 10:
        atual = 5
    elif atual == 5:
        atual = 1
    elif atual == 1:
        atual = 0.50
    elif atual == 0.50:
        atual = 0.10
    elif atual == 0.10:
        atual = 0.05
    elif atual == 0.05:
        atual = 0.02
    elif atual == 0.02:
        atual = 0.01
    elif atual == 0.01:
        atual = 0.001
    else:
        apagar = 0''' 

