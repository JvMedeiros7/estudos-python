# Declaração de classe

class Gafanhoto:
    def __init__(self): #Metodo Construtor
        #Atributos de instância
        self.nome = ""
        self.idade = 0

    #Métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# Declaração de Objetos

g1 = Gafanhoto()
g1.nome = input("Qual seu nome?")
g1.idade = int(input("Qual sua idade?"))
g1.aniversario() # Chamada do método aniversario

print(g1.mensagem()) # Chamada do método mensagem

print(g1.nome) # Acesso ao atributo nome
print(g1.idade) # Acesso ao atributo idade
