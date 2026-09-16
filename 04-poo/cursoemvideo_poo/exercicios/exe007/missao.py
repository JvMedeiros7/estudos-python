# ============================================================
#  SUPERCLASSE - Missao (o que TODA missão do MI6 tem em comum)
# ============================================================
# Generalização: não importa se a missão é de espionagem, resgate ou
# sabotagem, TODAS têm codigo, agente, local e status.
# Então isso sobe para a superclasse e as subclasses só HERDAM.
#
#                        Missao             <- SUPERCLASSE (genérica)
#                   /       |        \
#          Espionagem    Resgate    Sabotagem   <- SUBCLASSES (específicas)


class Missao:                                           # SUPERCLASSE (classe pai) - o que é comum a todas
    def __init__(self, codigo, agente, local):          # Construtor da superclasse
        self.codigo = codigo                            # Atributos que TODAS as subclasses vão HERDAR
        self.agente = agente                            # Ex.: "007 - James Bond"
        self.local = local                              # Ex.: "Istambul"
        self.status = "Pendente"                        # Toda missão NASCE pendente (não vem de fora, é fixo)

    def iniciar(self):                                  # Método definido SÓ aqui...
        self.status = "Em andamento"                    # ...mas Espionagem, Resgate e Sabotagem podem usar
        return f"[{self.codigo}] {self.agente} iniciou a missão em {self.local}."

    def concluir(self):                                 # Outro método HERDÁVEL
        self.status = "Concluída"
        return f"[{self.codigo}] Missão em {self.local} concluída com sucesso."

    def briefing(self):                                 # Método GENÉRICO - as subclasses vão SOBRESCREVER
        return f"Missão {self.codigo} | Agente: {self.agente} | Local: {self.local}"

    def __str__(self):                                  # Como a missão aparece no print()
        return f"[{self.codigo}] {self.agente} -> {self.local} ({self.status})"
