cidade = str(input('Em que cidade você nasceu?')).strip()

resultado = cidade[:5].upper() == 'SANTO'

print(f'O nome da sua cidade começa com "Santo" ? {resultado}')