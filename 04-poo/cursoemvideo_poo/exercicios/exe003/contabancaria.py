class ContaBancaria:
    """Classe que representa uma conta bancária com atributos de id, nome e saldo."""

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def __getstate__(self):
        return f"\nEstado : id = {self.id}, nome = {self.nome}, saldo = {self.saldo}"

    def __str__(self):
        return f"A conta {self.id} de {self.nome} tem saldo de R${self.saldo:,.2f}"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} realizado com sucesso. Novo saldo: R${self.saldo:,.2f}")
        pass

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} realizado com sucesso. \nNovo saldo: R${self.saldo:,.2f}")
        else:
            print("Saldo insuficiente para saque.")
        pass
    

c1 = ContaBancaria(1012, "João", 60000)

print(c1.__getstate__())  # Acesso ao estado do objeto c1 usando o método __getstate__

x = float(input("Digite o valor a ser depositado: "))
c1.depositar(x)

c1.sacar(float(input("Digite o valor a ser sacado: "))) #Aqui declara-se o valor a ser sacado, que será passado como argumento para o método sacar da classe ContaBancaria.

print(c1)
print(c1.__doc__)  # Acesso à documentação da classe ContaBancaria (docstring) #Dunder Attribute

