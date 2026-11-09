from classes023 import Pessoa, Aluno

def main():
    p = Pessoa("Joao", 1990)

    print(f"Nome: {p.nome}, Idade: {p.idade}")

    a = Aluno("Jv", 2000, "KKKK")

    print(f"Nome: {a.nome}, Idade: {a.idade}, Curso: {a.curso}")

if __name__ == "__main__":
    main()