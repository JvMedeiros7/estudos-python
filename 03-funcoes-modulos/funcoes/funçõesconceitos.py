#Função é um bloco de código identificado por um nome = identificador = função

#Podemos enviar parametros e ela pode retornar vários valores

#Parametros = Entrada / Retorno = Saída

'''def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"): #Se não declarar nome, por padrão vai substituir por "Anônimo"
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()

exibir_mensagem_2(nome="Guilherme") #Posso passar direto (Gui) = "Seja bem vindo Gui"

exibir_mensagem_3() #"Seja bem vindo Anônimo"

exibir_mensagem_3(nome="Chappie")'''

#Retorno de Valores = return.

'''def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    retorno = "Olá mundo"

    return retorno #Olá mundo

def func_3():
    retorno = "Olá mundo"  # = None


print(calcular_total([10, 20, 34]))  # 64

print(retorna_antecessor_e_sucessor(10))  # (9, 11)

print(func_3())'''

#Argumentos Nomeados 

'''def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

salvar_carro(marca="Fiat", modelo="Palio", ano="1999", placa="ABC-1012")

salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})'''

#Podemos combinar os parâmetros com *Args e **Kwargs
# Arg = Tupla / Kwarg = Dicionario

'''def exibir_poema(data_extenso, *args, **kwargs): 

    texto = "\n".join(args)#Todo o texto separado por virgula depois da primeira linha, pq a primeira é a data_extenso.

    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]) #Kwarg é estrutura chave valor 
    #Quando acabar o valor escrito por virgula e começar o chaveamento por chave/valor ele vai entender que o valor chegou em kwargs


    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"

    print(mensagem)


exibir_poema(
    "Terça, 05 de Maio de 2026.",
    "Beautiful is better than ugly.",
    autor="Tim Peters",
    ano=1999,
)'''

#Parâmetros especiais 

#parametros_somente_por_posicao

'''def f(pos1 , pos2,   /  , pos_or_kwd,        * ,kwd1, kwd2):
    #Positional only   Positional or Keyword       Keyword Only'''

'''def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
                #É obrigatorio pos     #Não é obrigatorio Pos pq é depois da barra 
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #Valida
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido'''

#parametros_somente_por_nome

#Se você quiser argumentos por posição ou chave = / -> Depois pode ser chave ou posição
#Se você quiser argumentos forçadamento por chave = * -> Tudo depois dela tem que ser por chave

'''def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido'''

#objetos_de_primeira_classe

'''def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação é = 20
exibir_resultado(10, 10, subtrair) # O resultado da operação é = 0 

op = somar #Variável com função

a = int(input("Digite o número 1:"))
b = int(input("Digite o número 2:"))

print(op(a, b))'''

#Escopo_local_e_global

'''salario = 2000 #Váriavel global = Na raiz do programaa


def salario_bonus(bonus):
    global salario #Salario está no escopo global 
    salario += bonus 
    return salario

x = int(input("Qual o valor do seu bonus:  "))

salario_com_bonus = salario_bonus(x)  # 2500
print(salario_com_bonus)'''

'''salario = 2000 


def salario_bonus(bonus):

    global salario  

    lista_aux = lista.copy()
    y = int(input("Digite um número:  "))
    lista_aux.append(y)
    print(f"Lista aux= {lista_aux}")

    salario += bonus 
    return salario

x = int(input("Qual o valor do seu bonus:  "))


lista = [1]
salario_com_bonus = salario_bonus(x)  
print(salario_com_bonus)
print(lista)'''