#Voto

def voto(n):
    ano_nasc = input("Digite o ano de nascimento: ")
    idade = n - int(ano_nasc)
    return idade


ano_votação = int(input("Digite o ano da eleição: "))


idade = voto(ano_votação)

if idade < 16:
    print(f"Com {idade} anos: Voto NEGADO")
elif idade >= 16 and idade < 18 or idade > 65:
    print(f"Com {idade} anos: Voto OPCIONAL")
else:   
    print(f"Com {idade} anos: Voto OBRIGATÓRIO")