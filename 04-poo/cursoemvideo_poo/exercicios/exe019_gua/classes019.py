# Hash é embaralhar algo = bagunçar algo = arquivo criptografado 

# Hash é uma função que transforma um conjunto de dados em uma sequência de caracteres de tamanho fixo, geralmente para fins de segurança, como armazenamento de senhas. É uma forma de "embaralhar" os dados, tornando-os irreversíveis e protegendo informações sensíveis.

# Exemplo de hash em Python usando a biblioteca hashlib:
# import hashlib

# Tratamento SHA-256 é um algoritmo de hash que gera uma sequência de 256 bits (32 bytes) a partir de uma entrada de dados. Ele é amplamente utilizado para garantir a integridade e a segurança das informações, como senhas e arquivos.

from hashlib import sha256

class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        if len(chave) > 0:
            # Gera o hash da senha usando SHA-256
            self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        #elif len(chave) < 9:
        #   raise ValueError("A senha deve ter pelo menos 8 caracteres.")
        else:
            raise ValueError("A senha não pode ser vazia.")


    def validar_senha(self, chave):
        # Aqui você pode implementar a lógica para validar a senha fornecida
        # comparando-a com o hash armazenado.
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            print("Senha válida!")
            return True
        else:
            print("Senha inválida!")
            return False