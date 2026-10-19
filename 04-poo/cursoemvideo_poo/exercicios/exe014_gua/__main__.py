from contabancaria import ContaBancaria

def main():

    c1 = ContaBancaria(111, "João", 5000)
    c1.depositar(1000)
    c1.sacar(-500)
    print(c1)
    

if __name__ == "__main__":
    main()