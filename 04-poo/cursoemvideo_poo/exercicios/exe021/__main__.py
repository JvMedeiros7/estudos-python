from classes021 import ContaBancaria

def main():

    cc = ContaBancaria(1, "João", 1000, "jotav1")

    print(cc)
    cc.sacar(500)

    print("Tentando mudar o nome")
    cc.nome = "João Silva"

    print(cc)


if __name__ == "__main__":
    main()