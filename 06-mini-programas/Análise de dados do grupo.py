tot18 = tothomem = totm20 = 0

while True:
    p1 = int(input('Qual a sua idade?'))
    if p1 > 18:
        tot18 += 1
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Qual o seu sexo?(M/F)')).strip().upper()[0]
        if sexo == 'M':
            tothomem += 1
        if sexo == 'F' and p1 < 20:
            totm20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print (f'Total de pessoas com mais de 18 anos: {tot18}')
print (f'Total de {tothomem} homens cadastrados')
print (f'Total de mulheres com menos de 20 anos: {totm20}')


