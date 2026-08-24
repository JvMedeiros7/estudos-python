n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print ('A sua média foi {:.1f}'.format (m))

if m >= 7.0:
    print ('Aprovado')
elif m <= 6.9 and m >= 5.0:
    print ('Recuperação')
else:
    print ('Reprovado')





