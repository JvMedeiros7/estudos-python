#Dicionario = Conjunto não-ordenado de pares chave:valores, onde as chaves são únicas em uma dada instância do dict.
#Dicionários são delimitados por chaves: {} - Tem que ser um valor imutável 

#1. Acesso Direto (A Sintaxe Básica)

'''aluno = {
    "nome" : "Deivinho" , 
    "idade" : 25 , 
    "linguagem" : "Python"
}

print(aluno)
print(aluno["nome"])
print(aluno.get("stack_favorita"))'''

#Iterando e Imprimindo Múltiplos Valores (O Loop for)

'''for chave in aluno:
    print(f"A chave {chave} guarda o valor: {aluno[chave]}")'''

#Opção B: Extraindo apenas os valores diretamente (Mais eficiente)

'''for valor in aluno.values():
    print(valor)'''

#Opção C: Extraindo Chave e Valor simultaneamente

'''for chave, valor in aluno.items():
    print(f"Propriedade: {chave} | Dado: {valor}")'''

#Dicionários Aninhados

''' contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone) ''' 

#Iterar sobre dicionários

'''contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor) '''

#Metodos de Classe - Dict

#{}.clear

'''contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.clear()
print(contatos)  # {}'''

#{}.copy

'''contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}'''

#{}.fromkeys

''' resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado) '''

#{}.get

'''contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)'''

#{}.items

'''contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
print(resultado)'''

#{}.keys

'''contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado) '''

#{}.pop

'''    contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

    resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
    print(resultado)

    resultado = contatos.pop("guilherme@gmail.com", {})  # {}
    print(resultado)''' 

#{}.popitem
'''
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)'''

# contatos.popitem()  # KeyError

#{}.setdefault - Quando precisar adicionar um valor, porém só os que não existam.

'''contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}'''

#{}.update - Atualiza o dicionário - adicionando

'''contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)'''

#{}.values

'''contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = (
    contatos.values()
)  # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])  # noqa
print(resultado)'''

#{}.in - Vefificar se uma chave está ou não no dicionário

'''contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = "guilherme@gmail.com" in contatos  # True
print(resultado)

resultado = "megui@gmail.com" in contatos  # False
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"]  # False
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"]  # True
print(resultado)'''

#Livro Python Nilo Ney Coutinho

'''tabela = {
    "alface" : 0.45 , 
    "batata" : 1.20 , 
    "tomate" : 2.30
}

print(tabela["batata"])

for chave in tabela:
    print(f"A chave é {chave} e o valor é {[tabela[chave]]}")
    '''

'''tabela = {
    "alface" : 0.45 , 
    "batata" : 1.20 , 
    "tomate" : 2.30 , 
    "feijão" : 1.98 
}

a = []

a = tabela.keys()

print(a)
print(tabela.keys())
print(tabela.values())
'''

'''# Criamos um dicionário simulado usando a lógica de listas aninhadas da aula
# Cada índice representa uma "vaga" ou "gaveta" na memória
estacionamento_hash = {
    411: [],
    412: [],  # Esta vaga receberá a colisão
    413: []
}

# --- ENTRADA DE DADOS (Simulando o mapeamento) ---

# Carro A chega e o cálculo aponta para a vaga 412
# Usamos o método .append() para adicionar o par [Chave, Valor]
estacionamento_hash[412].append(["Placa-XYZ", "Jeep Compass"])

# Carro B chega, o cálculo também dá vaga 412 (Colisão!)
# O sistema não apaga o primeiro; ele adiciona no final da sublista
estacionamento_hash[412].append(["Placa-ABC", "BYD Dolphin"])


# --- BUSCA DE DADOS (Como o sistema localiza) ---

placa_procurada = "Placa-ABC"
vaga_calculada = 412

# O sistema vai direto na vaga 412 e faz a varredura interna (Slide 16 - for)
for carro in estacionamento_hash[vaga_calculada]:
    if carro[0] == placa_procurada:
        print(f"Resultado da IDE -> Carro localizado na vaga {vaga_calculada}: {carro[1]}")

# Estado inicial da memória com a colisão na vaga 412
estacionamento_hash = {
    411: [],
    412: [["Placa-XYZ", "Jeep Compass"], ["Placa-ABC", "BYD Dolphin"]],
    413: []
}

# Parâmetros de entrada para o Checkout
placa_para_remover = "Placa-XYZ"
vaga_calculada = 412

print("--- ANTES DO CHECKOUT ---")
print(f"Vaga {vaga_calculada}: {estacionamento_hash[vaga_calculada]}")

# --- ENGENHARIA DA SOLUÇÃO ---

# 1. Ponteiro para guardar o objeto que será localizado
carro_alvo = None

# 2. Percorremos as sublistas da vaga (Slide 16 - for)
for carro in estacionamento_hash[vaga_calculada]:
    # carro[0] acessa a chave (Placa), carro[1] acessa o valor (Modelo)
    if carro[0] == placa_para_remover:
        carro_alvo = carro  # Capturamos a referência exata da sublista
        break               # Abortamos o loop imediatamente (otimização de CPU)

# 3. Se o ponteiro foi preenchido, executamos a remoção do bloco
if carro_alvo is not None:
    # Remove a sublista inteira correspondente (Slide 9 - remove())
    estacionamento_hash[vaga_calculada].remove(carro_alvo)
    print(f"\n[SUCESSO] Veículo {carro_alvo[1]} liberado da vaga {vaga_calculada}.")
else:
    print(f"\n[ERRO] Placa {placa_para_remover} não encontrada na vaga {vaga_calculada}.")


print("\n--- DEPOIS DO CHECKOUT ---")
print(f"Vaga {vaga_calculada}: {estacionamento_hash[vaga_calculada]}")'''

'''estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50],
}
total = 0
print("Vendas:\n")
while True:
    produto = input("Nome do produto (fim para sair):")
    if produto == "fim":
        break
    if produto in estoque:
        quantidade = int(input("Quantidade:"))
        if quantidade <= estoque[produto][0]:
            preço = estoque[produto][1]
            custo = preço * quantidade
            print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("Quantidade solicitada não disponível")
    else:
        print("Nome de produto inválido")
print(f" Custo total: {total:21.2f}\n")
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")'''


dici = {

}
palavra = input("Digite uma palavra:")

for letras in palavra:
    print(letras)
    if letras in dici:
        dici[letras] = dici[letras]+1
    else: 
        dici[letras] = 1
print(dici)









'''    while True:
        p = input("Qual produto você quer?")
        q = int(input("Qual a quantidade:"))
        sair = input("Você deseja sair? (0) PARA SAIR")
        if sair == "0":
            break
        historico_vendas = []
        historico_vendas.append([p , q ])
        print(historico_vendas)
        total = 0
        print("Vendas:\n")
        for operacao in venda:
            produto = p
            quantidade = q 
            produto, quantidade = operacao
            preço = estoque[produto][1]
            custo = preço * quantidade
            print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
            estoque[produto][0] -= quantidade
            total += custo
            print(f" Custo total: {total:21.2f} \n")
            print("Estoque:\n")
            for chave, dados in estoque.items():
                print(chave)
                print(dados)
                print("Descrição: " , chave)
                print("Quantidade: ", dados [0])
                print(f"Preço: {dados[1]:6.2f}\n")'''