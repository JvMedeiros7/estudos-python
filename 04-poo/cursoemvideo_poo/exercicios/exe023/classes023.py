from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self.__nome = nome
        self.__nascimento = nascimento

    @property
    def nome(self):
        return self.__nome

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if 1900 <= ano <= date.today().year:
            self.__nascimento = ano
        else:
            raise ValueError(f"Ano {ano} inválido. O ano de nascimento deve estar entre 1900 e {date.today().year}.")

    @property
    def idade(self):
        return date.today().year - self.__nascimento

    @idade.setter
    def idade(self, idade):
        raise PermissionError("Não é possível alterar a idade diretamente. A idade é calculada com base no ano de nascimento.")


class Aluno(Pessoa):

    cursos_oficiais = ["Python", "Java", "C++", "JavaScript"]

    def __init__(self, nome: str, nascimento:int, curso: str):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso  

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso in self.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"Curso '{curso}' não é oficial. Cursos oficiais: {', '.join(self.cursos_oficiais)}")

    def add_curso(self, curso):
        curso = curso.strip().upper()

        if 3 <= len(curso) <= 10:
            Aluno.cursos_oficiais.append(curso) 
        else:
            raise ValueError("O curso deve ter entre 3 e 10 caracteres.")  


    

