from rich import print, inspect
from rich.panel import Panel
from rich.traceback import install

from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

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

def main():
    aluno1 = Aluno("João", 20, "Matemática", "A")                       # nome e idade -> Escola; curso e turma -> Aluno
    professor1 = Professor("Maria", 35, "Física", "Avançado")           # nome e idade -> Escola; especialidade e nivel -> Professor
    funcionario1 = Funcionario("Carlos", 40, "Secretário", "Administração")  # nome e idade -> Escola; cargo e setor -> Funcionario

    # Cada objeto usa o método PRÓPRIO da sua subclasse + o método HERDADO da superclasse
    print(aluno1.matricular())                  # Método da SUBCLASSE Aluno -> João foi matriculado no curso de Matemática, turma A.
    print(aluno1.fazer_aniversario())           # Método HERDADO de Escola  -> João agora tem 21 anos.
    inspect(aluno1, methods=True)

    print(professor1.dar_aula())                # Método da SUBCLASSE Professor -> Maria está dando aula de Física, nível Avançado.
    print(professor1.fazer_aniversario())       # Método HERDADO de Escola      -> Maria agora tem 36 anos.
    inspect(professor1, methods=True)

    print(funcionario1.bater_ponto())           # Método da SUBCLASSE Funcionario -> Carlos bateu o ponto como Secretário no setor Administração.
    print(funcionario1.fazer_aniversario())     # Método HERDADO de Escola        -> Carlos agora tem 41 anos.
    inspect(funcionario1, methods=True)

# Repare: aluno1.dar_aula() daria ERRO (AttributeError), porque dar_aula() é de Professor.
# A herança vai do PAI para o FILHO, nunca entre "irmãos" (Aluno, Professor e Funcionario
# não compartilham nada entre si, só o que veio de Escola).


if __name__ == "__main__":
    main()
