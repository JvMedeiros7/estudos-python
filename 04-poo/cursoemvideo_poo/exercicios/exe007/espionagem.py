from missao import Missao


class Espionagem(Missao):                               # SUBCLASSE - o "(Missao)" é a HERANÇA
    def __init__(self, codigo, agente, local, alvo, disfarce):  # Recebe os do pai (codigo, agente, local) + os próprios
        super().__init__(codigo, agente, local)         # super() chama o __init__ da SUPERCLASSE -> cria codigo, agente, local e status
        self.alvo = alvo                                # Atributos NOVOS, existem só em Espionagem (especialização)
        self.disfarce = disfarce

    def infiltrar(self):                                # Método NOVO, só Espionagem tem
        return f"{self.agente} se infiltrou disfarçado de {self.disfarce} para vigiar {self.alvo}."

    def briefing(self):                                 # SOBRESCRITA: mesmo nome do método do pai, mas resposta própria
        return super().briefing() + f" | Alvo: {self.alvo} | Disfarce: {self.disfarce}"
        # super().briefing() reaproveita o texto genérico do pai e a subclasse só COMPLETA
