class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self._base = base
        self._altura = altura
        self._area = self._base * self._altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    @property
    def medidas(self):
        return f"Base: {self._base}\nAltura: {self._altura}\nÁrea: {self.area}"

    @medidas.setter
    def medidas(self, valores):
        base, altura = valores
        self._base = base
        self._altura = altura
        self._area = self._base * self._altura

    @property
    def area(self):
        return self._base * self._altura
