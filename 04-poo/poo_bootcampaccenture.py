#Programação Orientada a Objetos - Bootcamp Accenture

# ============================================================

#Um paradigma é um modelo ou padrão que serve como referência para a construção de algo. Na programação, um paradigma é um estilo ou abordagem de programação que orienta a forma como os programadores escrevem código e organizam seus programas.
#A Programação Orientada a Objetos (POO) é um paradigma de programação que se baseia no conceito de "objetos", que são instâncias de classes. A POO permite que os programadores criem estruturas de dados complexas e organizem o código de forma mais modular e reutilizável.

# ============================================================

#Problema : Beber Água

# Solução 1: Usar um copo para beber água

# Solução 2: Usar uma garrafa para beber água

# ============================================================

#Tipos de Paradigmas de Programação:

# - Programação Procedural: Foca na criação de procedimentos ou rotinas que operam em dados. O código é organizado em funções e procedimentos, e os dados são passados como argumentos para essas funções.
# - Programação Orientada a Objetos (POO): Foca na criação de objetos que encapsulam dados e comportamentos relacionados. O código é organizado em classes e objetos, e os dados e comportamentos são agrupados dentro dessas classes.
# - Programação Funcional: Foca na criação de funções puras que não têm efeitos colaterais e que operam em dados imutáveis. O código é organizado em funções de ordem superior e expressões, e os dados são transformados por meio de funções.

# ============================================================

#Programação Orientada a objetos : Ele abstraindo problemas do mundo real em objetos de software, que possuem atributos (dados) e métodos (comportamentos). Isso permite que os programadores criem sistemas mais complexos e organizados, facilitando a manutenção e a reutilização do código.

#Dois Conceitos Fundamentais da POO:

# - Classe: É um modelo ou molde que define as características e comportamentos de um tipo específico de objeto. Ela serve como uma "fábrica" para criar objetos. A classe define os atributos (variáveis) e métodos (funções) que os objetos criados a partir dela terão.

# - Objeto: É uma instância de uma classe. Ele representa um elemento específico do mundo real ou do domínio do problema. O objeto possui seus próprios valores para os atributos definidos na classe e pode executar os métodos definidos na classe.


# =============================================================

#Classes e Objetos

#1.1 Definição de Classe e Criação de Objetos

# Uma classe define as características e comportamentos de um tipo específico de objeto.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando objetos a partir da classe Pessoa
pessoa1 = Pessoa("João", 25)
pessoa1.apresentar()    
pessoa2 = Pessoa("Maria", 30)
pessoa2.apresentar()



