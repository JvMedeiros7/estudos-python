#Abstração é a prática de ignorar o irrelevante e se concentrar no que é essencial.

#Principais vantagens da abstração:

#1. Maior legibilidade do código
#2. Padronização do código 
#3. Simplificação de problemas grandes
#4. Maior segurança do código (encapsulamento)

#Existe a abstração de dados e a abstração de processos.

#Abstração de dados: Acontece quando ingoramos informações desnecessárias e nos concentramos apenas nas informações relevantes para o problema em questão.
#Abstração de processos: Acontece quando ignoramos detalhes de implementação e nos concentramos apenas no que o processo faz, sem nos preocupar com como ele faz.

#Metodo abastrato: É um método que é abstrato na classe mãe, que obriga as classes filhas a implementarem esse método, caso contrário, a classe filha não poderá ser instanciada.

#Classe abstrata: É uma classe que não pode ser instanciada, mas pode ser herdada. Ela serve como um modelo para as classes filhas, que devem implementar os métodos abstratos da classe mãe.

# Don't repeat yourself (DRY): É um princípio de programação que diz que você não deve repetir código desnecessariamente. Se você perceber que está repetindo código, é um sinal de que você deve criar uma função ou método para encapsular esse código e reutilizá-lo.

#Ao definir um conjunto de métodos abstratos, dizemos que estamos criando a interface pública da classe.

#Uma classe abstrata pode ter métodos abstratos que deverão ser obrigatoriamente implementados nas subclasse, mas pode ter métodos concretos se eles funcionarem para todas as subclasses. Ou seja, uma classe abstrata pode ter métodos concretos e métodos abstratos.

# Nomes de classe usam CamelCase (PEP 8)

class ControleRemoto:
    def __init__(self, cor, tamanho, marca):
        self.cor = cor
        self.tamanho = tamanho
        self.marca = marca
        # O estado fica em um único atributo booleano. Antes, "ligar" e "desligar"
        # eram atributos com o mesmo nome dos métodos, e o atributo de instância
        # escondia o método (c1.ligar() virava True(), causando TypeError).
        self.ligado = False

    # Os métodos ficam na classe base (DRY): qualquer controle pode ligar/desligar,
    # então as filhas herdam sem precisar redefinir.
    def ligar(self):
        self.ligado = True
        print("Controle remoto ligado")

    def desligar(self):
        self.ligado = False
        print("Controle remoto desligado")


class ControleRemotoSmart(ControleRemoto):
    def __init__(self, cor, tamanho, marca, sistema_operacional):
        # Reaproveita o __init__ da classe mãe para os atributos comuns
        super().__init__(cor, tamanho, marca)
        # Atributo exclusivo do controle smart
        self.sistema_operacional = sistema_operacional


c1 = ControleRemotoSmart("Preto", "Pequeno", "Samsung", "Android")
c1.ligar()
c1.desligar()