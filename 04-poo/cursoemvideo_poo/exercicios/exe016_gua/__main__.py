from avaliacao import Avaliacao
from rich import inspect, print 
from rich.panel import Panel
from rich.traceback import install

install()



def main():
    av1 = Avaliacao("João", "Matemática")
    av1.nota = -5  # Tentativa de definir uma nota inválida
       # Atualizando a nota usando o setter
    print(f"A nota atualizada de {av1.nome} em {av1.disciplina} é: {av1.nota}")

    inspect(av1, private=True, methods=True)



if __name__ == "__main__":
    main()