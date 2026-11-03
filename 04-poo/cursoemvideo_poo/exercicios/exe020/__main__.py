from retangulo import Retangulo

def main():
    r = Retangulo(3,8)  # Cria um objeto Retangulo com base 3 e altura 8

    r.base = -10  # Altera a base do retângulo para 5
    r.altura = 4  # Altera a altura do retângulo para 4



    print(r.medidas)  # Exibe as medidas iniciais do retângulo

if __name__ == "__main__":
    main()  