# ============================================================
# Declaração de classe
# ============================================================
# Uma classe é um "molde" para criar objetos. Ela define quais
# atributos (dados) e métodos (comportamentos) os objetos terão.

class Gafanhoto:
    def __init__(self, n = "vazio", i = 0):  # Método Construtor
        # É chamado automaticamente sempre que um objeto é criado
        # (ex: g1 = Gafanhoto()). Serve para inicializar os
        # atributos de instância com valores padrão.

        # Atributos de instância
        # Cada objeto criado a partir da classe terá sua PRÓPRIA
        # cópia desses atributos (g1.nome é diferente de g2.nome).
        self.nome = n
        self.idade = i

    # Métodos de instância
    # Sempre recebem "self" como primeiro parâmetro, que representa
    # o próprio objeto que está chamando o método.

    def aniversario(self):
        # Método que ALTERA o estado do objeto (efeito colateral),
        # por isso não precisa de return: seu objetivo é modificar
        # self.idade, não produzir um valor para ser usado depois.
        self.idade += 1

    def __str__(self):
        # Método especial que define como o objeto será representado
        # como string (ex: quando usado em print(g1)).
        return f"\nGafanhoto(nome={self.nome}, idade={self.idade})"

    def __getstate__(self):
        # Método especial que retorna o estado interno do objeto
        # (atributos e valores) como uma string.
        return f"\nEstado : nome = {self.nome}, idade = {self.idade}"


# ============================================================
# Declaração de Objetos
# ============================================================
# Cada objeto é uma instância independente da classe Gafanhoto,
# com seus próprios valores de nome e idade.

# ---------------- Objeto 1 ----------------

g1 = Gafanhoto("Maria", 20)  # Criação do objeto g1 com nome e idade iniciais
g1.aniversario()  # Chamada do método aniversario (idade +1)

print(g1) # Chamada do método __str__ (representação como string do objeto g1)

#---------------- Objeto 2 ----------------

g2 = Gafanhoto("João", 25)  # Criação do objeto g2 com nome e idade iniciais
g2.aniversario()  # Chamada do método aniversario (idade +1)

print(g2) # Chamada do método __str__ (representação como string do objeto g2)

print(g1.__dict__)  # Acesso ao dicionário interno do objeto g1 (atributos e valores) #Dunder Attribute
print(g1.__getstate__())  # Acesso ao estado interno do objeto g1 (atributos e valores) # Metodo especial que retorna o estado interno do objeto g1 (atributos e valores) #Dunder Method
print(g1.__class__)  # Acesso à classe do objeto g1 (Gafanhoto) #Dunder Attribute




print(g2.__dict__)  # Acesso ao dicionário interno do objeto g2 (atributos e valores) #Dunder Attribute
print(g2.__getstate__())  # Acesso ao estado interno do objeto g2 (atributos e valores) # Metodo especial que retorna o estado interno do objeto g2 (atributos e valores) #Dunder Method
print(g2.__class__)  # Acesso à classe do objeto g2 (Gafanhoto) #Dunder Attribute

