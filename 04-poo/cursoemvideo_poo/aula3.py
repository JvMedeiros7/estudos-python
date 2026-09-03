#O que são classes e objetos?

# Classes são moldes para criar objetos. Elas definem atributos (características) e métodos (comportamentos) que os objetos terão. Objetos são instâncias de classes, ou seja, são criados a partir das classes e possuem os atributos e métodos definidos por elas.

# Objetos são entidades que possuem estado e comportamento. O estado é representado pelos atributos, enquanto o comportamento é representado pelos métodos. Cada objeto pode ter valores diferentes para seus atributos, mas todos compartilham os mesmos métodos definidos pela classe.

# Classe é um molde a ser seguido sempre que for criar um objeto, definindo a estrutura (atributos e métodos) que os objetos desse tipo terão.

# Para definir uma classe, precisa de três elementos: nome da classe, atributos e métodos. A sintaxe básica para definir uma classe em Python é a seguinte:

# class NomeDaClasse:
#     def __init__(self, atributo1, atributo2):
#         self.atributo1 = atributo1
#         self.atributo2 = atributo2

# Self é uma referência ao próprio objeto que está sendo criado. Ele é usado para acessar os atributos e métodos da classe dentro da própria classe.

# Nome Classe - Caracteristicas que vai ter e Coisas que posso fazer.

# Caracteristicas que a classe vai ter é chamada de atributos, que são variáveis que armazenam informações sobre o objeto. Eles podem ser definidos dentro do método __init__ ou fora dele, dependendo do escopo desejado.

# Coisas que posso fazer é chamado de métodos, que são funções definidas dentro da classe e que descrevem o comportamento dos objetos. Eles podem acessar e modificar os atributos da classe, além de realizar outras operações.

# Exemplo comentado:

# class Pessoa:
#     def __init__(self, nome, idade): 
#         self.nome = nome  # Atributo nome
#         self.idade = idade  # Atributo idade
#     def falar(self):  # Método falar
#         print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


# Uma instancia de uma classe é criada chamando o nome da classe como se fosse uma função, passando os argumentos necessários para o método __init__. Por exemplo:

# pessoa1 = Pessoa("João", 30)  # Cria um objeto pessoa1 da classe Pessoa
# pessoa1.falar()  # Chama o método falar do objeto pessoa1

#Um objeto é a instância de uma classe, ou seja, é uma entidade concreta que possui os atributos e métodos definidos pela classe. Cada objeto pode ter valores diferentes para seus atributos, mas todos compartilham os mesmos métodos definidos pela classe.

# O objeto é uma coisa que vem de uma classe  e por ter sido feito por essa classe ela tem comportamento e caracteristicas semelhantes a classe que a criou. Por exemplo, se temos uma classe "Carro" com atributos como "cor" e "modelo", e métodos como "acelerar" e "frear", podemos criar diferentes objetos da classe "Carro", cada um com sua própria cor e modelo, mas todos compartilhando os mesmos métodos de acelerar e frear.

# class Biscoito:
#     def __init__(self, tamanho, massa, peso, cobertura, cozido, temperatura):
#         self.tamanho = tamanho
#         self.massa = massa
#         self.peso = peso
#         self.cobertura = cobertura
#         self.cozido = cozido
#         self.temperatura = temperatura

#     def assar(self):
#         if self.cozido:
#             print("O biscoito já está assado.")
#         else:
#          print("Assando o biscoito...")



# Objetos Abstatratos 

# São objetos que não podem ser instanciados diretamente, mas servem como base para outras classes. Eles são definidos usando a palavra-chave "abstract" e podem conter métodos abstratos, que são métodos sem implementação. As classes derivadas devem implementar esses métodos abstratos.

# Exemplo de classe abstrata:

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def fazer_som(self):
#         pass

# Por que "Animal" é uma classe abstrata?
# - Ela herda de ABC (Abstract Base Class), o que impede o Python de deixar você
#   criar um objeto Animal("...") diretamente -> daria TypeError.
# - "Animal" existe só para definir um contrato: toda classe que herdar dela
#   é OBRIGADA a implementar o método fazer_som(). Faz sentido, porque "animal"
#   é um conceito genérico demais para ter um som próprio (cada espécie tem o seu).
# - O método fazer_som() tem @abstractmethod e corpo "pass": é uma promessa
#   sem implementação. Quem herdar e não implementar também não pode ser instanciado.

# Quem pode virar objeto de verdade são as subclasses concretas, que implementam
# o método abstrato:

# class Cachorro(Animal):
#     def fazer_som(self):
#         print("Au au!")

# class Gato(Animal):
#     def fazer_som(self):
#         print("Miau!")

# Aí sim dá pra criar objetos, porque Cachorro e Gato cumpriram o contrato de Animal:

# rex = Cachorro()
# rex.fazer_som()   # Au au!

# mimi = Gato()
# mimi.fazer_som()  # Miau!

# animal = Animal()  # TypeError: Can't instantiate abstract class Animal
#                     # with abstract method fazer_som


