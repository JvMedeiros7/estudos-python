# ============================================================
# Declaração de classe
# ============================================================
# Uma classe é um "molde" para criar objetos. Ela define quais
# atributos (dados) e métodos (comportamentos) os objetos terão.

class Gafanhoto:
    def __init__(self):  # Método Construtor
        # É chamado automaticamente sempre que um objeto é criado
        # (ex: g1 = Gafanhoto()). Serve para inicializar os
        # atributos de instância com valores padrão.

        # Atributos de instância
        # Cada objeto criado a partir da classe terá sua PRÓPRIA
        # cópia desses atributos (g1.nome é diferente de g2.nome).
        self.nome = ""
        self.idade = 0

    # Métodos de instância
    # Sempre recebem "self" como primeiro parâmetro, que representa
    # o próprio objeto que está chamando o método.

    def aniversario(self):
        # Método que ALTERA o estado do objeto (efeito colateral),
        # por isso não precisa de return: seu objetivo é modificar
        # self.idade, não produzir um valor para ser usado depois.
        self.idade += 1

    def mensagem(self):
        # Método que PRODUZ um valor (a mensagem) e o devolve com
        # "return" para quem chamou decidir o que fazer com ele:
        # imprimir, guardar em variável, concatenar, etc.
        #
        # Se aqui dentro fosse usado "print" em vez de "return",
        # o método imprimiria sozinho e devolveria None — quem
        # chamasse g1.mensagem() não teria mais acesso ao texto.
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."


# ============================================================
# Declaração de Objetos
# ============================================================
# Cada objeto é uma instância independente da classe Gafanhoto,
# com seus próprios valores de nome e idade.

# ---------------- Objeto 1 ----------------

g1 = Gafanhoto()
g1.nome = input("Qual seu nome? ")
g1.idade = int(input("Qual sua idade? "))

g1.aniversario()  # Chamada do método aniversario (idade +1)
print(g1.mensagem())  # Chamada do método mensagem (usa o return)

print(g1.nome)  # Acesso direto ao atributo nome
print(g1.idade)  # Acesso direto ao atributo idade


# ---------------- Objeto 2 ----------------
# g2 é totalmente independente de g1: alterar g2 não afeta g1,
# pois cada objeto tem sua própria cópia dos atributos.

g2 = Gafanhoto()
g2.nome = input("Qual seu nome? ")
g2.idade = int(input("Qual sua idade? "))

g2.aniversario()  # Chamada do método aniversario
print(g2.mensagem())  # Chamada do método mensagem

print(g2.nome)  # Acesso ao atributo nome
print(g2.idade)  # Acesso ao atributo idade


# ---------------- Objeto 3 ----------------
# Aqui não chamamos aniversario() nem preenchemos nome/idade,
# então g3 usa os valores padrão definidos no __init__: "" e 0.

g3 = Gafanhoto()
print(g3.mensagem())  # Chamada do método mensagem (com valores padrão)

print(g3.nome)  # Acesso ao atributo nome (ainda "")
