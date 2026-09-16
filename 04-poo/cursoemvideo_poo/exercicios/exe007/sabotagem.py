from missao import Missao


class Sabotagem(Missao):                                # SUBCLASSE - herda de Missao
    def __init__(self, codigo, agente, local, instalacao, gadget):
        super().__init__(codigo, agente, local)         # Reaproveita o construtor da SUPERCLASSE
        self.instalacao = instalacao                    # Atributos NOVOS, só de Sabotagem
        self.gadget = gadget                            # Ex.: "caneta explosiva" (cortesia do Q)

    def sabotar(self):                                  # Método NOVO, só Sabotagem tem
        return f"{self.agente} sabotou {self.instalacao} usando {self.gadget}."

    def briefing(self):                                 # SOBRESCRITA do briefing genérico
        return super().briefing() + f" | Instalação: {self.instalacao} | Gadget: {self.gadget}"
