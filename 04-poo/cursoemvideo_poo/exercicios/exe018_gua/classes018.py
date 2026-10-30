from rich import print, inspect

class Diario:
    def __init__(self, senhamestra = 'CeV!@'):
        self.__segredos = []
        self.__senha = senhamestra.strip()

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())

    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError('Senha incorreta!')
        else:
            print(f"\nDIÁRIO LIBERADO!")
            print(f"Segredos armazenados: {len(self.__segredos)}")
            for segredo in self.__segredos:
                print(f"[green]{segredo}[/green]")



    @property
    def senha(self):
        raise PermissionError('Não é possível acessar a senha diretamente!')


    @senha.setter
    def senha(self, nova_senha):
        if type(nova_senha) is not str:
            raise TypeError('A senha deve ser uma string!')
        self.__senha = nova_senha.strip()