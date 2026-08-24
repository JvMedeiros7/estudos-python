#Ficha de Jogador 

def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gols no campeonato.'

n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))

print(ficha(n, g))