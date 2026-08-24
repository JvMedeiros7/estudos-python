import os

cadastro_de_pessoas = []
lista_mulheres = []

tot_pessoas = 0
tot_mulheres = 0
soma_idade = 0

while True:

    nome = input('Digite o nome da pessoa (ou "sair" para encerrar): ')
    if nome.lower() == 'sair':
        break

    idade = int(input('Digite a idade da pessoa: '))
    soma_idade += idade
    sexo = input('Digite o sexo da pessoa (M/F): ')
    sexo = sexo.upper()
    if sexo == "F":
        tot_mulheres += 1
        lista_mulheres.append({'nome': nome, 'idade': idade, 'sexo': sexo})

    cadastro_de_pessoas.append({'nome': nome, 'idade': idade, 'sexo': sexo})
    tot_pessoas += 1

os.system('cls' if os.name == 'nt' else 'clear')

print('Cadastro de Pessoas')


print(f'\nTotal de pessoas cadastradas: {tot_pessoas}')
print(f'\nTotal de mulheres cadastradas: {tot_mulheres}')

print('\nLista de mulheres cadastradas:')

for mulher in lista_mulheres:
    print(f'Nome: {mulher["nome"]}, Idade: {mulher["idade"]}, Sexo: {mulher["sexo"]}')


media_idade = soma_idade / tot_pessoas


print(f'\nMédia de idade das pessoas cadastradas: {media_idade:.2f} anos')

for pessoa in cadastro_de_pessoas:
    if pessoa['idade'] > media_idade:
        print(f'Pessoa acima da média de idade: Nome: {pessoa["nome"]}, Idade: {pessoa["idade"]}, Sexo: {pessoa["sexo"]}')




    