import os

# time agora guarda diretamente os dicionários dos jogadores (antes era lista de listas,
# pois cadastro_jogador.clear() reaproveitava a mesma lista a cada iteração)
time = []

while True:
    nome = input("Digite o nome do jogador: ")
    qtde_partidas = int(input(f"Digite a quantidade de partidas jogadas por {nome}: "))
    gols_partidas = []
    for i in range(qtde_partidas):
        gols_por_partida = int(input(f"Digite a quantidade de gols na partida {i + 1}: "))
        gols_partidas.append(gols_por_partida)  # guarda o gol de cada partida (antes só somava o total)
        tot_gols = sum(gols_partidas)  # total de gols do jogador (antes era acumulado a cada iteração)
    time.append({'nome': nome, 'gols': gols_partidas, 'total': tot_gols})
    while True:
        resp = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
        if resp in 'SN':
            break
        print("ERRO! Responda apenas S ou N.")
    if resp == 'N':
        break

os.system('cls' if os.name == 'nt' else 'clear')

# --- NOVO: tabela com código do jogador (índice) + uma coluna para cada chave do dict ---
print("-=" * 30)
print('cod ', end='')
for chave in time[0].keys():  # cabeçalho: nomes das chaves do dicionário (nome, gols)
    print(f'{chave:<15}', end='')
print()
print("-=" * 30)

for indice, jogador in enumerate(time):  # cada linha: índice = código do jogador
    print(f'{indice:<4}', end='')
    for valor in jogador.values():
        print(f'{str(valor):<15}', end='')
    print()

print("-=" * 30)

# --- NOVO: permite escolher um jogador pelo código para ver o detalhamento ---
while True:
    escolha = int(input("Mostrar dados de qual jogador? (999 para encerrar) "))
    if escolha == 999:
        break
    if escolha < 0 or escolha >= len(time):
        print("ERRO! Código de jogador inválido.")
        continue
    jogador = time[escolha]
    print(f'-- LEVANTAMENTO DO JOGADOR {jogador["nome"]} --')
    for numero_partida, gols in enumerate(jogador['gols']):
        print(f'No jogo {numero_partida + 1} fez {gols} gols.')

