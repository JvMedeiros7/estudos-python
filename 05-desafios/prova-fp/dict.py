#Dicionários são estruturas de dados que armazenam pares de chave-valor. Eles são mutáveis, o que significa que você pode alterar seus valores após a criação. Aqui estão algumas operações comuns com dicionários em Python:

'''# Criando um dicionário
meu_dicionario = {"nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"}

# Acessando valores
print(meu_dicionario["nome"])  # Saída: Alice
# Adicionando ou atualizando valores
print(meu_dicionario["idade"])  # Saída: 30
print(meu_dicionario["cidade"])  # Saída: São Paulo
meu_dicionario["idade"] = 31  # Atualiza a idade
meu_dicionario["profissão"] = "Engenheira"  # Adiciona uma nova chave-valor
# Removendo um item
del meu_dicionario["cidade"]  # Remove a chave "cidade"
# Verificando se uma chave existe
if "cidade" in meu_dicionario:
    print("A chave 'cidade' existe.")
else:
    print("A chave 'cidade' não existe.")

#Remover dados

del meu_dicionario["profissão"]  # Remove a chave "profissão"
# Limpando o dicionário
meu_dicionario.clear()  # Remove todos os itens do dicionário

filme = {"titulo": "Inception", "diretor": "Christopher Nolan", "ano": 2010, "genero": "Sci-Fi"}

print(filme.values())  # Saída: dict_values(['Inception', 'Christopher Nolan', 2010, 'Sci-Fi'])

print(filme.keys())  # Saída: dict_keys(['titulo', 'diretor', 'ano', 'genero'])

print(filme.items())  # Saída: dict_items([('titulo', 'Inception'), ('diretor', 'Christopher Nolan'), ('ano', 2010), ('genero', 'Sci-Fi')])

for chave, valor in filme.items():
    print(f"{chave}: {valor}")

locadora = { "filme1": {"titulo": "Inception", "diretor": "Christopher Nolan", "ano": 2010, "genero": "Sci-Fi"},
    "filme2": {"titulo": "The Matrix", "diretor": "Lana Wachowski", "ano": 1999, "genero": "Sci-Fi"},
    "filme3": {"titulo": "Interstellar", "diretor": "Christopher Nolan", "ano": 2014, "genero": "Sci-Fi"}}

# Dicionários NÃO suportam acesso por índice numérico (locadora[0] causaria KeyError)
# Para acessar por posição, converta os valores para lista primeiro
lista_filmes = list(locadora.values())  # transforma os valores do dicionário em lista
print(lista_filmes[0]['ano'])  # agora o índice 0 funciona — acessa o primeiro filme

print(f" O {locadora['filme1']['titulo']} foi dirigido por {locadora['filme1']['diretor']} em {locadora['filme1']['ano']} e é do gênero {locadora['filme1']['genero']}.")

for chave, valor in locadora.items():
    print(f"{chave}: {valor['titulo']} - {valor['diretor']} ({valor['ano']}) - {valor['genero']}")

for k in locadora.keys():
    print(k)

for v in locadora.values():
    print(v)    

for k, v in locadora.items():
    print(f"{k}: {v['titulo']} - {v['diretor']} ({v['ano']}) - {v['genero']}")

'''
brasil = []
estado1 = {"nome": "São Paulo", "Sigla": "SP", "População": 45919049, "Área": 248222.362}
estado2 = {"nome": "Rio de Janeiro", "Sigla": "RJ", "População": 17264943, "Área": 43696.1}

# append() aceita apenas 1 argumento por vez — para adicionar vários itens, chame separadamente
# brasil.append(estado1, estado2) causaria TypeError
brasil.append(estado1)  # adiciona estado1 à lista
brasil.append(estado2)  # adiciona estado2 à lista
# alternativa: brasil.extend([estado1, estado2]) — adiciona múltiplos itens de uma vez

print(brasil)
