from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return f":wave: Olá sou [bold]{self.nome}[/bold], o meu setor é {self.setor}, e o meu cargo: {self.cargo}"

    def __rich__(self):  # hook que o rich procura antes de usar str()
        return str(self)  # retornando string, o rich interpreta markup e emoji

c1 = Funcionario("João", "TI", "Analista de Sistemas")
print(c1)

c2 = Funcionario("Maria", "Financeiro", "Contadora")
print(c2)
