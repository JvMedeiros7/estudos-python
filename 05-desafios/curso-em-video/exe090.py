alunos = []

while True:
    print('Digite o nome do aluno (ou digite 0 para sair)')
    nome = str(input('Nome: '))
    if nome.strip().lower() == '0':
        break
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    if media >= 7:
        situação = 'Aprovado'
    else:
        situação = 'Reprovado'
    alunos.append({'nome': nome, 'nota1': nota1, 'nota2': nota2, 'media': media, 'situação': situação})

for aluno in alunos:
    print(f'O aluno {aluno["nome"]} teve média {aluno["media"]:.2f} e está {aluno["situação"]}.')

