#Exe - 6.2

'''L1 = []
x = 0 

while True:
    n = float(input(f"({x+1}). DIGITE O VALOR GASTO PARA A LISTA 1 R$ (0 PARA SAIR):  "))
    x += 1
    if n == 0:
        break
    L1.append(n)

L2 = []
x = 0

while True:
    n = float(input(f"({x+1}). DIGITE O VALOR GASTO PARA A LISTA 2 R$ (0 PARA SAIR):  "))
    x += 1
    if n == 0:
        break
    L2.append(n)

#Somamos os elementos
S = L1 + L2
print(S)


#Somamos a lista como 1 elemento
L1.append(L2)

print(L1) '''


#Exe - 6.3

'''L1 = []
x = 0 

while True:
    n = float(input(f"({x+1}). DIGITE O VALOR PARA A LISTA 1 (0 PARA SAIR):  "))
    x += 1
    if n == 0:
        break
    L1.append(n)

L2 = []
x = 0

while True:
    n = float(input(f"({x+1}). DIGITE O VALOR PARA A LISTA 2 (0 PARA SAIR): "))
    x += 1
    if n == 0:
        break
    L2.append(n)
    
L3 = []

for x in L1:
    if x not in L3:
        L3.append(x)

for y in L2:
    if y not in L3:
        L3.append(y)

print(L3)'''

#Instrução del 

'''L = list(range(101))

del L[1:99]

print(L)'''

#Metodo pop = .pop() = Retorna o valor do elemento e o exclui da fila

#Programa 6.7: Simulação de uma fila de banco

'''ultimo = 10
fila= list(range(1,ultimo + 1))

while True:
    print(f"\n Existem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("Ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação(F , A ou S):")
    if operacao == "A":
        if len(fila) >0:
            atendido = fila.pop(0)
            print(f"Cliente{atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender.")
    
    elif operacao == "F":
        ultimo += 1 #Incremento o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")'''


#Exe 6.5: Simulação de uma fila de banco

'''ultimo = 10
fila = list(range(1, ultimo + 1))

rodando = True

while rodando:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("Ou A para realizar o atendimento. S para sair.")
    
    # Boas práticas: o .upper() garante que, se o usuário digitar 'ffaa',
    # o sistema não quebre por ser case-sensitive.
    operacao = input("Operação(F, A ou S): ").upper()

    indice = 0 

    # Enquanto houver caracteres na string 'operacao' para ler...
    while indice < len(operacao):
        tipo = operacao[indice]
        print(f"\n--- Processando comando: {tipo} ---")
        
        # Correção 1: Uso do '==' para comparação.
        # Correção 2: Indentação perfeitamente alinhada para a estrutura if-elif-else (Aula 06).
        if tipo == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)  # Remove o primeiro da fila (índice 0)
                print(f"Cliente {atendido} atendido.")
            else:
                # Este 'else' pertence estritamente ao 'if len(fila) > 0'
                print("Fila vazia! Ninguém para ser atendido.")
                
        elif tipo == "F": 
            ultimo += 1
            fila.append(ultimo)
            print(f"Cliente {ultimo} entrou na fila.")
            
        elif tipo == "S":
            # Correção 3: Verificamos 'tipo' e alteramos a flag do loop principal.
            print("Encerrando o programa...")
            rodando = False
            break  # Interrompe o loop interno imediatamente. O loop externo não reiniciará pois rodando = False.
            
        else:
            print(f"Operação inválida ({tipo}) ignorada! Use apenas F, A ou S.")
            
        # O incremento do índice deve ficar fora das condições, para sempre avançar para a próxima letra.
        indice += 1        ''' 


#Exe 6.5: Simulação de uma fila de banco

'''ultimo1 = 10
ultimo2 = 10
fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))


rodando = True

while rodando:
    print(f"\nExistem {len(fila1)} e {len(fila2)}clientes na fila.")
    print(f"Fila 1 atual: {fila1}  - Fila 2 atual: {fila2} ")
    filadesejada = input("Você deseja atender na fila 1 (A) ou na fila 2 (B):").upper()

    if filadesejada == "A":

        print("Digite F para adicionar um cliente ao fim da fila 1,")
        print("Ou A para realizar o atendimento. S para sair.")
    
    # Boas práticas: o .upper() garante que, se o usuário digitar 'ffaa',
    # o sistema não quebre por ser case-sensitive.
        operacao1 = input("Operação(F, A ou S): ").upper()

        indice1 = 0 

    # Enquanto houver caracteres na string 'operacao' para ler...
        while indice1 < len(operacao1):
            tipo1 = operacao1[indice1]
            print(f"\n--- Processando comando: {tipo1} ---")
        
        # Correção 1: Uso do '==' para comparação.
        # Correção 2: Indentação perfeitamente alinhada para a estrutura if-elif-else (Aula 06).
            if tipo1 == "A":
                if len(fila1) > 0:
                    atendido1 = fila1.pop(0)  # Remove o primeiro da fila (índice 0)
                    print(f"Cliente {atendido1} atendido.")
                else:
                # Este 'else' pertence estritamente ao 'if len(fila) > 0'
                    print("Fila vazia! Ninguém para ser atendido.")
                
            elif tipo1 == "F": 
                ultimo1 += 1
                fila1.append(ultimo1)
                print(f"Cliente {ultimo1} entrou na fila.")
            
            elif tipo1 == "S":
            # Correção 3: Verificamos 'tipo' e alteramos a flag do loop principal.
                print("Encerrando o programa...")
                rodando = False
                break  # Interrompe o loop interno imediatamente. O loop externo não reiniciará pois rodando = False.
            
            else:
                print(f"Operação inválida ({tipo1}) ignorada! Use apenas F, A ou S.")
            
        # O incremento do índice deve ficar fora das condições, para sempre avançar para a próxima letra.
            indice1 += 1 

#Bloco fila 2 

    elif filadesejada == "B":     
        print("Digite F para adicionar um cliente ao fim da fila 1,")
        print("Ou A para realizar o atendimento. S para sair.")
    
    # Boas práticas: o .upper() garante que, se o usuário digitar 'ffaa',
    # o sistema não quebre por ser case-sensitive.
        operacao2 = input("Operação(F, A ou S): ").upper()

        indice2 = 0 

    # Enquanto houver caracteres na string 'operacao' para ler...
        while indice2 < len(operacao2):
            tipo2 = operacao2[indice2]
            print(f"\n--- Processando comando: {tipo2} ---")
        
        # Correção 1: Uso do '==' para comparação.
        # Correção 2: Indentação perfeitamente alinhada para a estrutura if-elif-else (Aula 06).
            if tipo2 == "A":
                if len(fila2) > 0:
                    atendido2 = fila2.pop(0)  # Remove o primeiro da fila (índice 0)
                    print(f"Cliente {atendido2} atendido.")
                else:
                # Este 'else' pertence estritamente ao 'if len(fila) > 0'
                    print("Fila vazia! Ninguém para ser atendido.")
                
            elif tipo2 == "F": 
                ultimo2 += 1
                fila2.append(ultimo2)
                print(f"Cliente {ultimo2} entrou na fila.")
            
            elif tipo2 == "S":
            # Correção 3: Verificamos 'tipo' e alteramos a flag do loop principal.
                print("Encerrando o programa...")
                rodando = False
                break  # Interrompe o loop interno imediatamente. O loop externo não reiniciará pois rodando = False.
            
            else:
                print(f"Operação inválida ({tipo2}) ignorada! Use apenas F, A ou S.")
            
        # O incremento do índice deve ficar fora das condições, para sempre avançar para a próxima letra.
            indice2 += 1 
'''


'''#Exe 6.5: Simulação de uma fila de banco

ultimo1 = 10
ultimo2 = 10
fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))

rodando = True

while rodando:
    print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} clientes na fila 2.")
    print(f"Fila 1 atual: {list(fila1)}  -  Fila 2 atual: {list(fila2)}")
    print("\nDigite:")
    print("[F] Chegada Fila 1  | [G] Chegada Fila 2")
    print("[A] Atender Fila 1  | [B] Atender Fila 2")
    print("[S] Sair do Sistema")
    
    operacao = input("-> Operação(ões): ").upper()

    indice = 0 

    # Enquanto houver caracteres na string 'operacao' para ler...
    while indice < len(operacao):
        tipo = operacao[indice]
        print(f"\n--- Processando comando: {tipo} ---")
        
        # Correção 1: Uso do '==' para comparação.
        # Correção 2: Indentação perfeitamente alinhada para a estrutura if-elif-else (Aula 06).
        if tipo == "A":
            if len(fila1) > 0:
                atendido1 = fila1.pop(0)  # Remove o primeiro da fila (índice 0)
                print(f"Cliente {atendido1} atendido.")
            else:
                # Este 'else' pertence estritamente ao 'if len(fila) > 0'
                print("Fila vazia! Ninguém para ser atendido.")
        elif tipo == "B":
            if len(fila2) > 0:
                atendido2 = fila2.pop(0)  # Remove o primeiro da fila (índice 0)
                print(f"Cliente {atendido2} atendido.")
            else:
                # Este 'else' pertence estritamente ao 'if len(fila) > 0'
                print("Fila vazia! Ninguém para ser atendido.")
                
        elif tipo == "F": 
            ultimo1 += 1
            fila1.append(ultimo1)
            print(f"Cliente {ultimo1} entrou na fila.")
        
        elif tipo == "G": 
            ultimo2 += 1
            fila2.append(ultimo2)
            print(f"Cliente {ultimo2} entrou na fila.")

        elif tipo == "S":
            # Correção 3: Verificamos 'tipo' e alteramos a flag do loop principal.
            print("Encerrando o programa...")
            rodando = False
            break  # Interrompe o loop interno imediatamente. O loop externo não reiniciará pois rodando = False.  
        else:
            print(f"Operação inválida ({tipo}) ignorada! Use apenas F, G, A, B ou S.")
            # O incremento do índice deve ficar fora das condições, para sempre avançar para a próxima letra.
        indice += 1   '''     


'''# Programa 6.8: Pilha de Pratos

prato = 5
pilha = list(range(1, prato + 1))

while True:
    print(f"\n existem {len(pilha)} pratos na pilha.")
    print(f"Pilha atual: {pilha}")
    print("Digite E para empilhar um novo prato,")
    print("Ou D para desempilhar. S para Sair.")

    operação = input("Operação (E, D OU S): ")
    if operação == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado")
        else:
            print("Pilha Vazia! Nada para lavar.")
    elif operação == "E":
        prato += 1
        pilha.append(prato)
    elif operação == "S":
        break
    else:
       print("Operação inválida! Digite apenas E,D ou S!")'''


''' #Estrutura de dados / Leitura

expressao = "(a+b)"
x = 0

# 1. CRIANDO A ESTRUTURA DE CONTROLE
# Criamos uma lista vazia. É ela quem tem permissão para usar .append() e .pop()[cite: 1].
pilha = []

while x < len(expressao):
    # Apenas LÊ a informação na posição x. Não alteramos essa variável.
    caractere_atual = expressao[x]
    
    # --- ÁREA DA REGRA DE NEGÓCIO ---
    
    if caractere_atual == "(":
        # Achamos uma abertura. Colocamos um "prato" na nossa lista.
        pilha.append("(") 
        
    elif caractere_atual == ")":
        # Achamos um fechamento. Retiramos o último "prato" da nossa lista[cite: 1].
        pilha.pop()
        
    # --------------------------------
    
    # Motor do laço
    x += 1 

# Fim da varredura.

(()) Ok
()()(()()) Ok
()) Erro'''


'''# Expressões de teste baseadas no seu escopo
exp_1 = "(())"          # Esperado: Ok
exp_2 = "()()(()())"    # Esperado: Ok
exp_3 = "())"           # Esperado: Erro (Tenta desempilhar pilha vazia)
exp_4 = "(()"           # Esperado: Erro (Sobra elemento na pilha)

expressao = exp_3 # Troque a variável aqui para testar os outros casos

# 1. Inicializamos a nossa "Pilha" usando uma lista vazia
pilha = []

# 2. Todo 'while' precisa de uma variável de inicialização para o controle
i = 0 

# Variável de controle de estado (flag) para saber se a expressão quebrou a regra
valida = True

# 3. O 'while' repete o bloco enquanto o índice 'i' for menor que o tamanho da string
while i < len(expressao):
    caractere = expressao[i] # Acessamos o caractere na posição atual do índice
    
    if caractere == '(':
        # REGRA 1: Sempre que encontrar '(', adiciona (empilha) ao final da lista[cite: 9]
        pilha.append(caractere)
        
    elif caractere == ')':
        # REGRA 2: Encontrou ')'. Antes de dar o pop(), verificamos o tamanho da lista[cite: 9]
        # Isso previne o erro fatal de tentar desempilhar uma lista vazia.
        if len(pilha) > 0:
            pilha.pop() # Remove o último elemento inserido (desempilha)[cite: 9]
        else:
            # Se a pilha está vazia e chegou um ')', a ordem está errada.
            valida = False
            break # Interrompe o loop manualmente, pois já identificamos o erro fatal[cite: 8]
            
    # 4. Todo 'while' precisa da atualização da variável para não gerar loop infinito[cite: 8]
    i += 1 

# 5. Avaliação Fria do Estado Final
# A expressão só é correta se não quebrou a regra no meio (valida == True) 
# E se, no final de tudo, não sobrou nenhum '(' perdido (len(pilha) == 0)
if valida and len(pilha) == 0:
    print(f"A expressão '{expressao}' está: Ok")
else:
    print(f"A expressão '{expressao}' está: Erro")'''

# Desejado


'''expressão = input("Digite a sequência de parênteses a validar:")
x = 0
pilha = []
while x < len(expressão):
    if expressão[x] == "(":
        pilha.append("(")
    if expressão[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")  # Força a mensagem de erro
            break
    x = x + 1
if len(pilha) == 0:
    print("OK")
else:
    print("Erro")'''


'''expressão = input("Digite uma palavra:").upper()
x = 0
a = 0
b =  0 
pilha = []
listaa = []
listab = []

while x < len(expressão):
    if expressão[x] == "A":                                          
        a +=1
        listaa.append(x)
    elif expressão[x] == "B":
        b += 1
        listab.append(x) 
    x = x + 1


print(f"A quantidade de vezes que você digitou a : {a} \n A quantiadade que você digitou b : {b}")
print(f"A letra a está nas posições: {listaa}")
print(f"A letra b está nas posições: {listab}")'''

'''#Programa 6.9: Pesquisa Sequencial

L = [15, 7, 27, 39, 27, 7, 8, 9, 30, 27 ]

p1 = int(input("Digite o 1o valor a procurar:"))
p2 = int(input("Digite o 2o valor a procurar:"))

p1num = 0
p1pos = []
p2num = 0
p2pos = []

x = 0 

while x < len(L):
    if L[x] != p1 and L[x] != p2:
        print(f"{p1} ou {p2} : não está na lista na posição {x}.")
    else: 
        if p1 == L[x]:
            print(f"{p1} : achado na posição {x}.")
            p1num += 1
            p1pos.append(x)  
        else:
            print(f"{p2} : achado na posição {x}.")
            p2num += 1
            p2pos.append(x)      
    x += 1

print(f"A quantidade de vezes que localizamos seu valor foi: {p1num + p2num} \n A posição em que seu valor foi econtrado foi: {p1pos + p2pos}")'''
   
'''L = []
x = 1
for v in range(x):
    x += 1
    lv = input("Digite um valor para a lista(0 para sair): ")
    if lv == "0":
        break
    L.append(lv)
print(L)'''

#Exe 6.12

'''L = [ 1, 7, 2 , 4]
min = L[0]

for e in L:
    if e < min:
        min = e

print(min)'''

'''T = [ - 10, -8, 0, 1, 2, 5, -2, -4]
valor_min = T[0]
valor_max = T[0]
soma = 0 
x = 0

for e in T:
    if e < valor_min:
        valor_min = e
    elif e > valor_max:
        valor_max = e 
    soma = soma + e
    x += 1

print(f"Nessas {x} temperaturas a média é:")
print(f" MÉDIA : {soma/x}")
print(f"A temperatura mais alta foi: {valor_max}")
print(f"A temperatura mais baixa foi: {valor_min}")'''

'''lugares_vagos = [10, 2, 1, 3, 0]

sala = int(input("Sala (0 sai): "))

lugares = int(input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos)? "))
lugares_vagos[sala - 1] -= lugares

# CORREÇÃO: Aspas fechadas no final e variável 'sala' isolada de forma limpa.
print(f"Locais sobrando na sala {sala}: {lugares_vagos[sala - 1]}")'''


#Programa 6.13:

'''lugares_vagos = [ 10, 2, 1, 3, 0]
ingressos_vendidos = [0, 0, 0, 0, 0]
salas_dispo = [1,2,3,4,5]
'''


# 1. Inicializamos as listas completamente vazias
# 1. Inicializamos as listas completamente vazias[cite: 1].
'''lugares_vagos = []
ingressos_vendidos = []

# 2. Capturamos o tamanho do nosso domínio de negócio.
total_salas = int(input("Quantas salas o cinema possui? "))

# 3. Iteramos sobre o intervalo de salas.
for i in range(total_salas):
    capacidade = int(input(f"Qual a capacidade da sala {i + 1}? "))
    # Injetamos os valores dinamicamente[cite: 1].
    lugares_vagos.append(capacidade)
    ingressos_vendidos.append(0)

print("\n--- INICIALIZAÇÃO CONCLUÍDA ---")
print(f"Salas configuradas: {len(lugares_vagos)}")
print("-" * 31 + "\n")

# 4. Loop infinito para o PDV (Ponto de Venda)[cite: 8].
while True:
    # A variável 'sala_escolhida' é exclusiva para a transação atual.
    # NUNCA reutilize nomes de variáveis de estado em laços de repetição menores.
    sala_escolhida = int(input("\nSala (0 sai): "))
    
    # Condição de saída[cite: 8].
    if sala_escolhida == 0:
        print("\nEncerrando vendas...")
        break
        
    # Validação do limite da lista.
    if sala_escolhida > len(lugares_vagos) or sala_escolhida < 1:
        print("[ERRO] Sala inválida. Tente novamente.")
    # Como a contagem do índice começa do zero, subtraímos 1 da escolha do usuário[cite: 1].
    elif lugares_vagos[sala_escolhida - 1] == 0:
        print("[AVISO] Desculpe, esta sala está lotada!")
    else:
        # Acesso direto via índice para recuperar os lugares disponíveis[cite: 1].
        vagos_atuais = lugares_vagos[sala_escolhida - 1]
        lugares_desejados = int(input(f"Quantos lugares você deseja ({vagos_atuais} vagos): "))
        
        # Validações lógicas de negócio
        if lugares_desejados > vagos_atuais:
            print("[ERRO] Esse número de lugares não está disponível.")
        elif lugares_desejados <= 0:
            print("[ERRO] Número de ingressos inválido.")
        else:
            # 5. Processamento da Transação (Mutabilidade da Lista)[cite: 1]
            lugares_vagos[sala_escolhida - 1] -= lugares_desejados
            ingressos_vendidos[sala_escolhida - 1] += lugares_desejados
            
            # Correção lógica: Se a sala_escolhida foi 1, imprimimos 1. Sem "+ 1" aqui.
            print(f"[SUCESSO] {lugares_desejados} lugares vendidos para a Sala {sala_escolhida}.")
            print(f"Total de ingressos vendidos na Sala {sala_escolhida}: {ingressos_vendidos[sala_escolhida - 1]}")
    
    print("\n--- UTILIZAÇÃO ATUAL DAS SALAS ---")
    # 6. Uso correto do enumerate: saber o índice do objeto dentro do laço[cite: 1].
    # Renomeamos as variáveis do iterador para não sobrescrever 'sala_escolhida'.
    for idx_sala, qtd_vagos in enumerate(lugares_vagos):
        print(f"Sala {idx_sala + 1} - {qtd_vagos} lugar(es) vazio(s).")

print("\n--- RELATÓRIO FINAL DE VENDAS ---")
# 7. Correção Crítica do IndexError. 
# Iteramos sobre a lista de ingressos vendidos de forma limpa.
for indice, vendidos in enumerate(ingressos_vendidos):
    # Acessamos diretamente a variável 'vendidos' entregue pelo enumerate.
    print(f"Sala {indice + 1} - {vendidos} ingresso(s) vendido(s).")
'''

'''n_salas = int(input("Número de salas: "))
lugares_vagos = []
for sala in range(n_salas):
    lugares_vagos.append(int(input(f"Lugares vagos na sala {sala + 1}: ")))

vendidos = [0] * len(lugares_vagos)
while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(
            input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos):")
        )
        if lugares > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido")
        else:
            lugares_vagos[sala - 1] -= lugares
            vendidos[sala - 1] += lugares
            print(f"{lugares} lugares vendidos")

print("\nUtilização das salas")

for sala, vagos in enumerate(lugares_vagos):
    print(f"Sala {sala + 1} – {vagos} lugar(es) vazio(s)")
print("\nVendas por sala")
total_vendido = 0
for sala, vendas in enumerate(vendidos):
    print(f"Sala {sala + 1} – {vendas} ingressos vendido(s)")
    total_vendido += vendas
print(f"Total de ingressos vendidos: {total_vendido}")    '''

