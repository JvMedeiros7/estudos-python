'''sexo = str(input('digite seu sexo (M/F): ')).strip().upper()[0]'''

sexo = str(input('digite seu sexo (M/F): ').strip().upper()[0])
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. digite seu sexo (M/F): ').strip().upper()[0])
print (f'Sexo {sexo} registrado com sucesso')