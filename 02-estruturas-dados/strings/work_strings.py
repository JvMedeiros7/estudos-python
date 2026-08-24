'''s = "Alo mundo "

#Transforma String em lista para poder manipular, pq strings são imutaveis
L = list(s)
print(L)

#.join transforma os elementos da lista em string
s ="".join(L)
print(s)


#Metodos startswith - Verificar se começa com uma string

nome ="Joao da Silva"

print(nome.startswith("Joao"))

#Metodos endswith - Verificar se termina com uma string

print(nome.endswith("Silva"))

#Metodo Startswitch - caractere variado 

# Opção 1: deixar tudo minúsculo para comparar

nome_lower = nome.lower()
print(nome_lower.startswith("joao"))  # True

# Opção 2: usar upper 
print(nome.upper().startswith("JOAO"))  # True

# Verificação direta

print("Silva" in nome)     # True
print("Da silva" in nome)  # False — sensível a maiúsculas

# Para ignorar capitalização, normalize antes:
print("da silva" in nome.lower())  # True
print("SILVA" in nome.upper())     # True

# Também funciona com not in
print("Pedro" not in nome)  # True

#O operador in pode ser utilizado em Listas

#PAara contar as ocorrências de uma letra ou palavra, use o metodo Count'''









