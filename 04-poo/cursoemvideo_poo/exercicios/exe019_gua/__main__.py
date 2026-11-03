from classes019 import Credencial

def main():

    c = Credencial()
    c.senha = str(input("Digite sua senha: "))  # Solicita ao usuário que digite a senha
    print("Hash da senha:", c.senha)  # Exibe o hash da senha

    # Valida a senha
    c.validar_senha(input("Digite sua senha novamente: "))  # Deve retornar "Senha válida!"

if __name__ == "__main__":
    main()
