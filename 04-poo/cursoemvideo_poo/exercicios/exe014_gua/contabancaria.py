from rich import print
from rich import inspect

class ContaBancaria:
    """Classe que representa uma conta bancária com atributos de id, nome e saldo."""
   
    def __init__(self, id, nome, saldo = 0):
        self.id = id # Public (+): Atributos e métodos públicos podem ser acessados de qualquer lugar, tanto dentro quanto fora da classe.
        self._nome = nome # Protected (#): Atributos e métodos protegidos são indicados por um único sublinhado ( _ "Em python") e devem ser acessados apenas dentro da classe e suas subclasses. No entanto, ainda podem ser acessados fora da classe, mas é desencorajado.
        self.__saldo = saldo # Private (-): Atributos e métodos privados são indicados por dois sublinhados ( __ "Em python") e não podem ser acessados diretamente fora da classe. Eles são destinados apenas para uso interno da classe.
        print(f"\nConta criada com sucesso! \nID: {self.id} \nNome: {self._nome} \nSaldo: [bold blue]R${self.__saldo:,.2f}[/bold blue]")

    def __getstate__(self):
        return f"\nEstado : id = {self.id}, nome = {self._nome}, saldo = {self.__saldo}"

    def __str__(self):
        #return f"A conta {self.id} de {self.nome} tem saldo de R${self.saldo:,.2f}"
        return f"Estado atual da conta :{self.__dict__}"


    def depositar(self, valor):
        valor = abs(valor)  # Garante que o valor seja positivo
        self.__saldo += valor
        print(f"Depósito de R${valor:,.2f} realizado com sucesso. Novo saldo: R${self.__saldo:,.2f}")
        pass

    def sacar(self, valor):
        valor = abs(valor)  # Garante que o valor seja positivo
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"\nSaque de R${valor:,.2f} realizado com sucesso. \nNovo saldo: R${self.__saldo:,.2f}")
        else:
            print("\nSaldo insuficiente para saque.")
        pass
    
