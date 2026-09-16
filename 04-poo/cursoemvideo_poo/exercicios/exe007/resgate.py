from missao import Missao


class Resgate(Missao):                                  # SUBCLASSE - herda de Missao
    def __init__(self, codigo, agente, local, refem, veiculo_fuga):
        super().__init__(codigo, agente, local)         # Reaproveita o construtor da SUPERCLASSE
        self.refem = refem                              # Atributos NOVOS, só de Resgate
        self.veiculo_fuga = veiculo_fuga

    def resgatar(self):                                 # Método NOVO, só Resgate tem
        return f"{self.agente} resgatou {self.refem} e fugiu de {self.veiculo_fuga}."

    def briefing(self):                                 # SOBRESCRITA do briefing genérico
        return super().briefing() + f" | Refém: {self.refem} | Fuga: {self.veiculo_fuga}"
