from rich import print
from rich import inspect
from hashlib import sha256

class ContaBancaria:
    """Classe que representa uma conta bancária com atributos de _id, nome e saldo."""
   
    def __init__(self, id: int, nome: str = None, saldo:float = 0, chave: str = None):
        self._id = id 
        self._nome = nome 
        self.__saldo = saldo
        if chave is None:
            chave = self.pede_senha() 
        self.__hash = sha256(chave.encode()).hexdigest()
        print(f"\nConta criada com sucesso! \nid: {self._id} \nNome: {self._nome} \nSaldo: [bold blue]R${self.__saldo:,.2f}[/bold blue]")

    def pede_senha(self):

        from pwinput import pwinput #Para aparecer com os asteristicos na hora de digitar a senha, é necessário instalar a biblioteca pwinput. Para isso, execute o seguinte comando no terminal: pip install pwinput
        while True:
            senha = pwinput("Digite uma senha: ", mask="*").strip()
            if len(senha) < 6:
                print("A senha deve ter pelo menos 6 caracteres. Tente novamente.")
            else:
                break

        return senha

    def validar_senha(self, chave):
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False


    def __str__(self):
        #return f"A conta {self._id} de {self.nome} tem saldo de R${self.saldo:,.2f}"
        return f"Estado atual da conta :{self.__dict__}"


    def depositar(self, valor):
        valor = abs(valor)  # Garante que o valor seja positivo
        self.__saldo += valor
        print(f"Depósito de R${valor:,.2f} realizado com sucesso. Novo saldo: R${self.__saldo:,.2f}")
        pass

    def sacar(self, valor, chave: str = None):
        valor = abs(valor)  # Garante que o valor seja positivo

        if chave is None:
            from pwinput import pwinput
            chave = pwinput("Digite a senha para realizar o saque: ", mask="*").strip()
        
        if self.validar_senha(chave):
            if valor <= self.__saldo:
                self.__saldo -= valor
                print(f"\nSaque de R${valor:,.2f} realizado com sucesso. \nNovo saldo: R${self.__saldo:,.2f}")
            else:
                print("\nSaldo insuficiente para saque.")
            pass
        else:
            print("\nSenha incorreta. Saque não realizado.")
    

    @property 
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        from pwinput import pwinput
        chave = pwinput("Digite a senha para mudar o nome: ", mask="*").strip()

        if self.validar_senha(chave):
            if len(novo_nome) < 5:
                print("O nome deve ter pelo menos 5 caracteres. Tente novamente.")
            else:
                self._nome = novo_nome
                print(f"Nome alterado com sucesso para {self._nome}.")