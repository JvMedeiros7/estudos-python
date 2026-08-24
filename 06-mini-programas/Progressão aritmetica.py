primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('=' * 30)
print(' OS 10 PRIMEIROS TERMOS DESSA PA SÃO: ')
print('=' * 30)

for c in range(1, 11):
    termo_atual = primeiro_termo + (c - 1) * razao
    print(f'{termo_atual}', end=' -> ')
print('FIM!')