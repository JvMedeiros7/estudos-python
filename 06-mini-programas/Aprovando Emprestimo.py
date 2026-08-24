sal = float(input('Qual o seu salario?'))
valorcasa = float(input('Qual o valor da casa?'))
anos = float(input('Quantos anos deseja pagar?'))

valormes = anos * 12
print (f' A quantidade de meses é: {valormes}')
parcelas = valorcasa / valormes
print (f' A parcela fica: {parcelas:.2f}')
saltrinta = sal * 0.30
print (f' O Seu limite de parcela é: {saltrinta}')
if parcelas > saltrinta:
    print ('\033[1;31mA parcela é maior que seu limite\033m')
else:
    print ('\033[1;33mVOCÊ FOI APROVADO, COMPRE SUA CASA!\033m')
