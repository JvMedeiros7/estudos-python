from rich import print, inspect
from rich.panel import Panel
from rich.traceback import install

install()

#Pilares de Programação Orientada a Objetos (POO)

#1. Abstração: A abstração é o processo de identificar os aspectos essenciais de um objeto, ignorando os detalhes irrelevantes. Em POO, isso significa criar classes que representem entidades do mundo real, focando apenas nos atributos e comportamentos relevantes.

#2. Encapsulamento: O encapsulamento é o princípio de ocultar os detalhes internos de uma classe e fornecer uma interface pública para interagir com ela. Isso ajuda a proteger os dados e a garantir que eles sejam manipulados de maneira controlada.

#3. Herança: A herança é um mecanismo que permite que uma classe (subclasse) herde atributos e métodos de outra classe (superclasse). Isso promove a reutilização de código e facilita a manutenção do software.

#4. Polimorfismo: O polimorfismo é a capacidade de diferentes classes responderem a mesma mensagem (método) de maneiras diferentes. Isso permite que objetos de diferentes classes sejam tratados de forma uniforme, aumentando a flexibilidade do código.

#Herança em Python

## A herança é um relacionamento entre itens gerais e específicos. A classe pai (superclasse) fornece atributos e métodos que podem ser herdados pelas classes filhas (subclasses). As subclasses podem adicionar novos atributos e métodos ou sobrescrever os existentes.

#Principais vantagens da herança:

#1. Reutilização de código: A herança permite que as subclasses reutilizem o código da superclasse, evitando duplicação e facilitando a manutenção.
#2. Organização hierárquica: A herança ajuda a organizar o código em uma estrutura hierárquica, tornando-o mais fácil de entender e navegar.
#3. Facilidade de manutenção: Alterações na superclasse podem ser propagadas para as subclasses, facilitando a manutenção do código.
#4. Extensibilidade: A herança permite que novas classes sejam criadas com base em classes existentes, facilitando a extensão do sistema.
#5. Suporte a polimorfismo: A herança permite que diferentes classes compartilhem a mesma interface, facilitando o uso de polimorfismo.

## Exemplo de herança em Python:


'''class Passarinho_pai:                                   # SUPERCLASSE (classe pai / classe base)
    def __init__(self, nome):                           # Construtor da superclasse
        self.nome = nome                                # Atributo que toda subclasse vai HERDAR

    def voar(self):                                     # Método definido SÓ aqui, na superclasse...
        return f"{self.nome} está voando!"              # ...mas as subclasses vão poder usá-lo

    def cantar(self):                                   # Outro método herdável
        return f" Piu Piu Piu 8) - {self.nome} está cantando!"


class Passarinho_filho(Passarinho_pai):                 # SUBCLASSE (classe filha) - o "(Passarinho_pai)" é a HERANÇA:
    def __init__(self, nome, especie):                  # Passarinho_filho recebe tudo que Passarinho_pai tem
        super().__init__(nome)                          # super() chama o __init__ da SUPERCLASSE -> cria self.nome
        self.especie = especie                          # Atributo NOVO, existe só na subclasse (especialização)

    # Repare: a subclasse NÃO define voar() nem cantar(),
    # mas mesmo assim consegue usar os dois -> isso é a HERANÇA em ação.


filhote = Passarinho_filho("Piu", "Canário")            # Objeto criado a partir da SUBCLASSE
print(filhote.voar())                                   # voar() foi HERDADO da superclasse -> Piu está voando!
print(filhote.cantar())                                 # cantar() também foi HERDADO -> Piu Piu Piu 8) - Piu está cantando!

print(f"Nome: {filhote.nome}, Espécie: {filhote.especie}")  # nome veio da SUPERCLASSE, especie da SUBCLASSE -> Nome: Piu, Espécie: Canário'''


# ============================================================
#  EXEMPLO 2 - Uma SUPERCLASSE, várias SUBCLASSES (Escola)
# ============================================================
# Aqui a generalização fica clara: Aluno, Professor e Funcionario têm
# nome e idade em comum -> isso sobe para a superclasse Escola.
# Cada subclasse adiciona o que é SÓ dela (especialização).
#
#                        Escola             <- SUPERCLASSE (genérica)
#                   /       |        \
#              Aluno    Professor   Funcionario   <- SUBCLASSES (específicas)


class Escola:                                           # SUPERCLASSE (classe pai) - o que é comum a todos
    def __init__(self, nome, idade):                    # Construtor da superclasse
        self.nome = nome                                # Atributos que TODAS as subclasses vão HERDAR
        self.idade = idade

    def fazer_aniversario(self):                        # Método definido SÓ aqui...
        self.idade += 1                                 # ...mas Aluno, Professor e Funcionario podem usar
        return f"{self.nome} agora tem {self.idade} anos."


class Aluno(Escola):                                    # SUBCLASSE - o "(Escola)" é a HERANÇA
    def __init__(self, nome, idade, curso, turma):      # Recebe os do pai (nome, idade) + os próprios (curso, turma)
        super().__init__(nome, idade)                   # super() chama o __init__ da SUPERCLASSE -> cria nome e idade
        self.curso = curso                              # Atributos NOVOS, existem só em Aluno (especialização)
        self.turma = turma

    def matricular(self):                               # Método NOVO, só Aluno tem
        return f"{self.nome} foi matriculado no curso de {self.curso}, turma {self.turma}."


class Professor(Escola):                                # SUBCLASSE - herda de Escola
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)                   # Reaproveita o construtor da SUPERCLASSE
        self.especialidade = especialidade              # Atributos NOVOS, só de Professor
        self.nivel = nivel

    def dar_aula(self):                                 # Método NOVO, só Professor tem
        return f"{self.nome} está dando aula de {self.especialidade}, nível {self.nivel}."


class Funcionario(Escola):                              # SUBCLASSE - herda de Escola
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)                   # Reaproveita o construtor da SUPERCLASSE
        self.cargo = cargo                              # Atributos NOVOS, só de Funcionario
        self.setor = setor

    def bater_ponto(self):                              # Método NOVO, só Funcionario tem
        return f"{self.nome} bateu o ponto como {self.cargo} no setor {self.setor}."


# Criando objetos a partir das SUBCLASSES
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



