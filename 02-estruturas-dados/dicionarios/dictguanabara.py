# ============================
# Estrutura Composta - Dicionário
# ============================
# Dicionário é uma estrutura de dados que armazena pares de chave e valor.

#Exemplo de dicionário
pessoa = {'nome': 'Gustavo', 'idade': 22, 'sexo': 'M'}

#Adicionando elementos ao dicionário
pessoa['altura'] = 1.75

#Acessando elementos do dicionário
print(pessoa['nome'])  # Saída: Gustavo

del pessoa['idade']  # Removendo um elemento do dicionário

# ============================
# Métodos de dicionário: values(), keys(), items()
# ============================
filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'
         }

print(filme.values())  # Saída: dict_values(['Star Wars', 1977, 'George Lucas']) - Sai os valores do dicionário

print(filme.keys())  # Saída: dict_keys(['titulo', 'ano', 'diretor']) - Sai as chaves do dicionário

print(filme.items())  # Saída: dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])

for k, v in filme.items():
    print(f'O {k} é {v}')  # Saída: O titulo é Star Wars, O ano é 1977, O diretor é George Lucas


# ============================
# Lista de dicionários
# ============================
locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
            {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},
            {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}]


print(locadora[0]['titulo'])  # Saída: Star Wars
print(locadora[1]['ano'])  # Saída: 2012
print(locadora[2]['diretor'])  # Saída: Wachowski

for filme in locadora:
    print(filme)
    print(f'O filme {filme["titulo"]} foi lançado em {filme["ano"]} e dirigido por {filme["diretor"]}.')

# ============================
# Exercício: cadastro de pessoas via input
# ============================
pessoas = []

while True:
    x = str(input('Nome: '))
    if x.strip().lower() == 'sair':
        break
    y = str(input('Sexo: '))
    z = int(input('Idade: '))
    pessoas.append({'nome': x, 'sexo': y, 'idade': z})

print(pessoas)  # Saída: [{'nome': 'Nome do usuário', 'sexo': 'Sexo do usuário', 'idade': Idade do usuário}, ...]

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

pessoas ['idade'] = 23  # Alterando o valor da chave 'idade'

pessoas['peso'] = 75.5  # Adicionando uma nova chave 'peso'

#Não precisa dar append para adicionar no dicionário 

brasil = []

#Criando dicionários para representar estados brasileiros

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

#Adicionando os dicionários estado1 e estado2 à lista brasil

brasil.append(estado1)
brasil.append(estado2)

print(brasil)  # Saída: [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]

while True:
    estado = {}
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print(brasil)  # Saída: [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}, ...]


estado = dict()

brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  # Usando copy() para criar uma cópia do dicionário estado
    #Dicionário não pode fazer fatiamento 

for e in brasil: #Tecnica para demonstrar os elementos do dicionário dentro da lista
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')  # Saída: O campo uf tem valor Rio de Janeiro, O campo sigla tem valor RJ, etc.  

for e in brasil:
    for v in e.values():
        print(v, end=' ') 
        print('\n')  
print('\n')
print(brasil)  



