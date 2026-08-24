'''# ============================================================
#  LISTAS EM PYTHON — Guia passo a passo
# ============================================================

# ============================================================
#  BLOCO 1 — Operações básicas de modificação
# ============================================================

print("=" * 50)
print("BLOCO 1 -- Operacoes basicas de modificacao")
print("=" * 50)

num = [2, 5, 9, 1]
print(f"\nLista criada:              {num}")

num[2] = 3
print(f"Apos num[2] = 3:           {num}  -> substitui o indice 2 pelo valor 3")

num.append(7)
print(f"Apos append(7):            {num}  -> adiciona 7 no final")

num.sort()
print(f"Apos sort():               {num}  -> ordena em ordem crescente")

num.sort(reverse=True)
print(f"Apos sort(reverse=True):   {num}  -> ordena em ordem decrescente")

del num[2]
print(f"Apos del num[2]:           {num}  -> remove o elemento do indice 2")

num.remove(1)
print(f"Apos remove(1):            {num}  -> remove o primeiro valor 1 encontrado")

num.insert(2, 0)
print(f"Apos insert(2, 0):         {num}  -> insere 0 no indice 2")

num.pop(2)
print(f"Apos pop(2):               {num}  -> remove o elemento do indice 2")

num.pop()
print(f"Apos pop():                {num}  -> remove o ultimo elemento")

print(f"\nLista final: {num}")
print(f"Quantidade de elementos: {len(num)}")


# ============================================================
#  BLOCO 2 — Fatiamento (slicing)
# ============================================================

print("\n" + "=" * 50)
print("BLOCO 2 -- Fatiamento (slicing)")
print("=" * 50)

frutas = ['maca', 'banana', 'uva', 'pera', 'melao']
print(f"\nLista criada: {frutas}")
print(f"Indices:       0       1        2      3       4")

print(f"\nfrutas[1:3]  -> {frutas[1:3]}           -> do indice 1 ate o 2 (o 3 fica de fora)")
print(f"frutas[:2]   -> {frutas[:2]}      -> do inicio ate o indice 1")
print(f"frutas[2:]   -> {frutas[2:]}  -> do indice 2 ate o fim")
print(f"frutas[-1]   -> {frutas[-1]}               -> ultimo elemento (indice negativo)")


# ============================================================
#  BLOCO 3 — Outros métodos úteis
# ============================================================

print("\n" + "=" * 50)
print("BLOCO 3 -- Outros metodos uteis")
print("=" * 50)

print(f"\nLista atual: {frutas}")

frutas.remove('uva')
print(f"Apos remove('uva'):   {frutas}  -> remove pelo valor")

print(f"index('pera'):        {frutas.index('pera')}                    -> indice onde 'pera' esta")
print(f"'banana' in frutas:   {'banana' in frutas}                 -> verifica se existe na lista")
print(f"count('maca'):        {frutas.count('maca')}                    -> quantas vezes 'maca' aparece")

frutas.reverse()
print(f"Apos reverse():       {frutas}  -> inverte a ordem")


# ============================================================
#  BLOCO 4 — Iteração (percorrer a lista com for)
# ============================================================

print("\n" + "=" * 50)
print("BLOCO 4 -- Iteracao com for")
print("=" * 50)

print("\nPercorrendo a lista de frutas:")
for fruta in frutas:
    print(f"  - {fruta}")


# ============================================================
#  BLOCO 5 — Condicional com lista (in + remove)
# ============================================================

print("\n" + "=" * 50)
print("BLOCO 5 -- Condicional com lista (in + remove)")
print("=" * 50)

lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(f"\nLista de lanche: {lanche}")

if 'Pizza' in lanche:
    print("'Pizza' encontrada na lista -> removendo...")
    lanche.remove('Pizza')
else:
    print("'Pizza' nao esta na lista")

print(f"Lista apos remocao: {lanche}")


# ============================================================
#  BLOCO 6 — Formas de criar listas
# ============================================================

print("\n" + "=" * 50)
print("BLOCO 6 -- Formas de criar listas")
print("=" * 50)

valores = list(range(1, 11))
print(f"\nlist(range(1, 11)):   {valores}  -> cria lista de 1 a 10")

valores1 = [8, 2, 5, 4, 9, 3, 0]
print(f"Lista literal:        {valores1}")

valores.append(1)
print(f"\nApos append(1) em valores:  {valores}  -> 1 adicionado no final")

valores1.append(1)
print(f"Apos append(1) em valores1: {valores1}  -> 1 adicionado no final")

valores.sort()
print(f"\nApos sort() em valores:     {valores}")

valores1.sort()
print(f"Apos sort() em valores1:    {valores1}")


# ============================================================
#  BLOCO 7 -- Percorrendo listas e copiando listas
# ============================================================

print("\n" + "=" * 50)
print("BLOCO 7 -- Percorrendo listas e copiando listas")
print("=" * 50)

# --- Percorrendo com for simples ---
valores = [8, 2, 5, 4, 9, 3, 0]
print(f"\nLista criada: {valores}")

valores.append(1)
print(f"Apos append(1):  {valores}  -> adiciona 1 no final")

valores.append(7)
print(f"Apos append(7):  {valores}  -> adiciona 7 no final")

print("\nPercorrendo com for (end='' mantém tudo na mesma linha):")
for valor in valores:
    print(f"{valor} ", end="")
print()

# --- Coletando dados do usuario com input ---
print("\n--- Coletando 5 valores digitados pelo usuario ---")
valores = []
for cont in range(0, 5):
    valores.append(int(input(f"  Digite o valor {cont + 1}: ")))

print(f"\nLista apos input: {valores}")

# --- Percorrendo com enumerate (indice + valor) ---
print("\nPercorrendo com enumerate (mostra indice e valor juntos):")
for c, v in enumerate(valores):
    print(f"  Indice {c} : Valor {v}")

# --- Copia de lista ---
print("\n--- Diferenca entre referencia e copia ---")
a = [2, 5, 9, 1]
print(f"Lista a criada: {a}")

b = a[:]
print(f"b = a[:] cria uma COPIA independente de a: {b}")

b[2] = 8
print(f"\nApos b[2] = 8:")
print(f"  a: {a}  -> nao foi alterada (sao listas diferentes)")
print(f"  b: {b}  -> so b foi alterada")'''

'''pessoas = [('Joao', 25), ('Maria', 30), ('Pedro', 20)]

for nome, idade in pessoas:
    print(f"Nome: {nome}, Idade: {idade}")
    dados = (nome, idade)
    print(f"Dados da pessoa: {dados}")  # tupla com nome e idade

print(f"\nLista de pessoas: {pessoas}")
print(f"Tipo da lista: {type(pessoas)}  # listas podem conter tipos misturados")

pos = int(input("Digite a posicao da pessoa que deseja acessar: "))

if 0 <= pos < len(pessoas):
    nome, idade = pessoas[pos]
    print(f"Nome: {nome}, Idade: {idade}")
else:
    print("Posicao invalida.")

nomebuscado = input("Digite o nome da pessoa para acessar os dados: ")
qualdados = int(input("Digite 0 para nome ou 1 para idade: "))

pessoa = next((p for p in pessoas if p[0].lower() == nomebuscado.lower()), None)
if pessoa:
    print(f"Dados de {pessoa[0]}: {pessoa[qualdados]}")
else:
    print(f"Pessoa '{nomebuscado}' nao encontrada.")'''


teste = list()
teste.append('gustavo')
teste.append(40)
print(f"teste criado:                    {teste}")

galera = list()
galera.append(teste)                       # referência, não cópia
print(f"galera após append(teste):       {galera}")

teste[0] = 'maria'
teste[1] = 22
print(f"teste após alteração:            {teste}")
print(f"galera mudou junto (referência): {galera}")

galera.append(teste[:])                    # cópia independente de teste neste momento
print(f"galera após append de cópia:     {galera}")

teste[0] = 'joao'
teste[1] = 23
print(f"\nteste após nova alteração:       {teste}")
print(f"galera[0] mudou (referência):    {galera[0]}")
print(f"galera[1] não mudou (cópia):     {galera[1]}")
print(f"galera completo:                 {galera}")

