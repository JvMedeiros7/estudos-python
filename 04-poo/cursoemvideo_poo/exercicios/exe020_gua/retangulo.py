class Retangulo:
    def __init__(self, base = 1, altura = 1):
        #Declaração de atributos privados
        self._base = None
        self._altura = None
        self._area = None
        
        #Declara de atributos públicos usando os setters para validação 
        self.base = base
        self.altura = altura
        self._area = self._base * self._altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("A base deve ser um número.")
        if valor <= 0:
            raise ValueError("A base deve ser maior que zero.")
        else:
            self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("A altura deve ser um número.")
        if valor <= 0:
            raise ValueError("A altura deve ser maior que zero.")
        else:
            self._altura = valor

    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError("A área não pode ser alterada diretamente.")

    @property
    def medidas(self):
        return f"Base: {self._base}\nAltura: {self._altura}\nÁrea: {self.area}"

    @medidas.setter
    def medidas(self, valores = tuple):
        if not isinstance(valores, tuple) or len(valores) != 2:
            raise ValueError("O valor deve ser uma tupla com dois elementos: (base, altura).")
        if isinstance(valores[0], float) or isinstance(valores[0], int):
            self.base = valores[0]
        else:
            raise TypeError("A base deve ser um número.")
        if isinstance(valores[1], float) or isinstance(valores[1], int):
            self.altura = valores[1]
        else:
            raise TypeError("A altura deve ser um número.")
        base, altura = valores
        self.base = base
        self.altura = altura
