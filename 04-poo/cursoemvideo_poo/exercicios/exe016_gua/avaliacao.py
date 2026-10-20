class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0.0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota


    #Criando Atributo Validável

    @property
    def nota(self): # Metodo getter para acessar o valor do atributo protegido _nota
        return self._nota

    @nota.setter
    def nota(self, valor): # Metodo setter para validar e definir o valor do atributo protegido _nota
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            raise ValueError("A nota deve estar entre 0 e 10.")

    @nota.deleter
    def nota(self): # Metodo deleter para remover o atributo protegido _nota
        del self._nota





