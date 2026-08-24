# Valor_final = 0

finalizar = "n"

while finalizar != "s":
    compra = int(input("Digite o valor da compra: "))
    valor_final = valor_final + compra
    finalizar = input("Deseja finalizar? [s/n] ")

print('Valor final: R$' , valor_final) #


