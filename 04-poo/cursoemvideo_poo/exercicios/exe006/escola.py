from rich import print
from rich.panel import Panel
from rich.traceback import install

install()

# ============================================================
#  EXEMPLO - Uma SUPERCLASSE, várias SUBCLASSES (Escola)
# ============================================================
# Aqui a generalização fica clara: Aluno, Professor e Funcionario têm
# nome e idade em comum -> isso sobe para a superclasse Escola.
# Cada subclasse adiciona o que é SÓ dela (especialização).
#
#                        Escola             <- SUPERCLASSE (genérica)
#                   /       |        \
#              Aluno    Professor   Funcionario   <- SUBCLASSES (específicas)

# Criando objetos a partir das SUBCLASSES


class Escola:                                           # SUPERCLASSE (classe pai) - o que é comum a todos
    def __init__(self, nome, idade):                    # Construtor da superclasse
        self.nome = nome                                # Atributos que TODAS as subclasses vão HERDAR
        self.idade = idade

    def fazer_aniversario(self):                        # Método definido SÓ aqui...
        self.idade += 1                                 # ...mas Aluno, Professor e Funcionario podem usar
        return f"{self.nome} agora tem {self.idade} anos."









