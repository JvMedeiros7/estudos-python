#Polimorfismo é a capacidade que um objeto tem de se comportar de diferentes formas, dependendo do contexto em que é utilizado. Em Python, o polimorfismo é frequentemente implementado através de métodos e classes, permitindo que diferentes objetos respondam a mesma mensagem (método) de maneiras distintas.

##Exemplo de polimorfismo com classes e métodos:

## Definindo uma classe base chamada Animal
'''
class Animal:
    def fazer_som(self):
        raise NotImplementedError("Subclasses devem implementar este método.")'''

## Definindo subclasses que herdam da classe Animal

'''
class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

## Função que demonstra o polimorfismo
def emitir_som(animal):
    print(animal.fazer_som())

## Exemplo de uso
cachorro = Cachorro()
gato = Gato()

emitir_som(cachorro)  # Saída: Au Au!
emitir_som(gato)      # Saída: Miau!''' # Um único nome, mas comportamentos diferentes.

#Python faz polimorfismo sem a necessidade de herança explícita, permitindo que diferentes tipos de objetos sejam tratados de forma uniforme, desde que implementem os métodos esperados.

#Polimorfismo é a propriedade ou estado daquilo que se apresenta e/ou se comporta de várias formas, dependendo do contexto em que é utilizado. Em Python, o polimorfismo é frequentemente implementado através de métodos e classes, permitindo que diferentes objetos respondam a mesma mensagem (método) de maneiras distintas.

# Um único nome, mas comportamentos diferentes.

class Animal:
    def fazer_som(self):
        raise NotImplementedError("Subclasses devem implementar este método.")
    

class Pato(Animal):
    def fazer_som(self):
        return "Quack!"

    def locomover(self, meio):
        if meio == "água":
            return "Nadando"
        elif meio == "terra":
            return "Caminhando"
        else:
            return "Voando"


        


print("Exemplo de polimorfismo com a classe Pato:")
pato1 = Pato()

print(pato1.fazer_som())
print(pato1.locomover("água"))  # Saída: Nadando
print(pato1.locomover("terra"))  # Saída: Caminhando
print(pato1.locomover("ar"))    # Saída: Voando

#Function Overloading (Sobrecarga de Funções) é um conceito relacionado ao polimorfismo, onde uma função ou método pode ter diferentes comportamentos dependendo do número ou tipo de argumentos passados para ela. Em Python, a sobrecarga de funções não é suportada da mesma forma que em algumas outras linguagens, mas podemos simular esse comportamento usando argumentos padrão ou verificando o tipo dos argumentos dentro da função.
 