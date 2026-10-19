class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota


    def get_nota(self): # Metodo getter para acessar o valor do atributo protegido _nota
        return self._nota

    def set_nota(self, valor): # Metodo setter para modificar o valor do atributo protegido _nota
        if 0 <= valor <= 10: # Verifica se o valor está dentro do intervalo permitido (0 a 10)
            self._nota = valor
        else:
            print("Nota inválida. A nota deve estar entre 0 e 10.")


