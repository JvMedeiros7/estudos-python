#Desafio 105 - notas

'''def notas():
    notas = dict()
    for i in range(0, 4):
        nota = float(input(f'Digite a {i+1}ª nota: '))
        notas[f'nota_{i+1}'] = nota
    return notas

notas = notas()
media_turma = sum(notas.values()) / len(notas)

print(f"A quantidade de notas cadastras foi {len(notas)}.")
print(f"A média das notas foi {media_turma}.")

maior_nota = max(notas.values())
menor_nota = min(notas.values())    

print(f"A maior nota foi {maior_nota} e a menor nota foi {menor_nota}.")'''


'''def notas(nota1, nota2, nota3, nota4):
    notas = dict()
    notas['nota_1'] = nota1
    notas['nota_2'] = nota2
    notas['nota_3'] = nota3
    notas['nota_4'] = nota4
    return notas

for i in range(0, 4):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    notas[f'nota_{i+1}'] = nota

notas = notas(nota1, nota2, nota3, nota4)

for k, v in notas.items():
    print(f"{k}: {v}")'''


def notas(*n, sit=False):
    """Função para analisar notas e situações de vários alunos.

    Parametros:
    n: uma ou mais notas dos alunos (aceita várias)
    sit: valor opcional, indicando se deve ou não adicionar a situação
    return: dicionário com várias informações sobre a situação da turma
    """
    notas = dict()
    notas['total'] = len(n)
    notas['maior'] = max(n)
    notas['menor'] = min(n)
    notas['media'] = sum(n) / len(n)
    if sit:
        if notas['media'] >= 7:
            notas['situação'] = 'BOA'
        elif notas['media'] >= 5:
            notas['situação'] = 'RAZOÁVEL'
        else:
            notas['situação'] = 'RUIM'
    return notas

x = float(input('Digite a 1ª nota: '))
y = float(input('Digite a 2ª nota: '))
z = float(input('Digite a 3ª nota: '))
w = float(input('Digite a 4ª nota: '))

resp = notas(x, y, z, w, sit=True)

print(resp)

help(notas)