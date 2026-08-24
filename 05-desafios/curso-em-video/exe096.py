#Controle de Terrenos 

def main():
    #Entrada de dados
    largura = float(input("Digite a largura do terreno (em metros): "))
    comprimento = float(input("Digite o comprimento do terreno (em metros): "))

    #Cálculo da área
    area = largura * comprimento

    #Saída de dados
    print(f"A área do terreno é: {area:.2f} metros quadrados.")

main()