#Metodos úteis da Classe String

''' curso = "PyThOn"

print(curso.upper())
#Python

print(curso.lower())
#python

print (curso.title())
#Python

curso1 = " Python "

print(curso1.strip())
#Python

print(curso1.lstrip())
#"Python   "

print(curso1.rstrip())
#"   Python"


curso2 = "Python"

print(curso2.center(10, "#"))
#"##Python##"

print(".".join(curso2))
#"P.y.th.h.o.n" ''' 


#f-string

''' nome = input("Qual seu nome?")

print(f"O seu nome é : {nome.upper()} ")


alt = float(input("Qual sua altura??"))

print(f"sua altura é {alt:10.2f}")


pi = float(input("Qual valor de PI?"))

print(f"O valor de pi é: {pi:.2f}") ''' 



#Fatiamento de Strings

''' nome = "João Vitor de Medeiros"

print(nome[0]) # Passa o que estiver no indice
#"J"

print(nome[:4]) # Passa tudo que vinher da esquerda até 10 caracteres
#"João"

print(nome[13:]) # Passa tudo que vinher da direita até 10 caracteres
#" de Medeiros" 

print(nome[5:12])
#" Vitor de "

print(nome[10:16:2])
#" eM"

print(nome[:])
#"João Vitor de Medeiros"

print(nome[::-1])
#"soriedeM ed rotiV oãoJ" ''' 

#String Multiplas Linhas

''' nome = "João Vitor de Medeiros"

mensagem = f""" 
    Olá meu nome é {nome}
Eu estou aprendendo Python.
        Essa mensagem tem diferentes recuos. 
"""

print(mensagem)


print("""
    ===MENU===
      
      1 - PRODUTO 1
      2 - PRODUTO 2
      3 - PRODUTO 3
      0 - SAIR

    =========== """
      ) ''' 

''' valor_compra = int(input())

# TODO: Implemente a estrutura condicional para decidir e imprimir a mensagem correta
# Dica: Use if, elif e else para comparar o valor_compra com as faixas especificadas no enunciado.

if valor_compra >= 30 and valor_compra < 75:
  print("Obrigado por comprar conosco!")
elif valor_compra >= 75 and valor_compra < 150:
  print("Parabens! Voce ganhou um brinde!")
elif valor_compra >= 150 and valor_compra < 250:
  print("Desconto de 10 reais aplicado!")
  valor_compra = valor_compra - 10 
elif valor_compra >= 250:
  print("Desconto de 25 reais aplicado!")
  valor_compra = valor_compra - 25 ''' 


