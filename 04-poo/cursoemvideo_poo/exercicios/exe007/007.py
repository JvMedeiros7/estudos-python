from rich import print, inspect
from rich.panel import Panel
from rich.traceback import install

from espionagem import Espionagem                       # Cada classe vem do seu próprio arquivo (modularização)
from resgate import Resgate
from sabotagem import Sabotagem
from agencia import Agencia

install()

# ============================================================
#  EXERCÍCIO 007 - Cadastro de missões de espiões (HERANÇA)
# ============================================================
# Ideia: o MI6 cadastra missões. Toda missão tem codigo, agente, local
# e status -> isso fica na SUPERCLASSE Missao.
# Cada TIPO de missão adiciona só o que é dela -> SUBCLASSES.
#
#                        Missao             <- SUPERCLASSE (genérica)
#                   /       |        \
#          Espionagem    Resgate    Sabotagem   <- SUBCLASSES (específicas)
#
# A Agencia é o "cadastro": guarda as missões numa lista.


def main():
    mi6 = Agencia("MI6")                                # Cria o cadastro (ainda sem missões)

    # ---- Criando objetos a partir das SUBCLASSES ---------------------------------------------
    # codigo, agente e local -> vão para Missao (via super());  o resto -> fica na subclasse
    m1 = Espionagem("GF-001", "007 - James Bond", "Istambul", "Le Chiffre", "jogador de pôquer")
    m2 = Resgate("SF-002", "006 - Alec Trevelyan", "Sibéria", "cientista Natalya", "helicóptero")
    m3 = Sabotagem("TB-003", "007 - James Bond", "Cuba", "base de mísseis", "caneta explosiva")

    # ---- Cadastrando na agência --------------------------------------------------------------
    print(Panel("Cadastro de missões", style="bold blue"))
    print(mi6.cadastrar(m1))                            # Missão GF-001 cadastrada no MI6.
    print(mi6.cadastrar(m2))
    print(mi6.cadastrar(m3))

    # ---- Briefing: método SOBRESCRITO em cada subclasse ----------------------------------------
    # O mesmo nome briefing() responde diferente dependendo do tipo da missão.
    print(Panel("Briefings", style="bold blue"))
    for missao in mi6.missoes:
        print(missao.briefing())

    # ---- Cada objeto usa o método PRÓPRIO da subclasse + os HERDADOS de Missao ----------------
    print(Panel("Missão em campo", style="bold blue"))
    print(m1.iniciar())                                 # HERDADO de Missao   -> muda status para "Em andamento"
    print(m1.infiltrar())                               # PRÓPRIO de Espionagem
    print(m1.concluir())                                # HERDADO de Missao   -> muda status para "Concluída"

    print(m2.iniciar())                                 # HERDADO de Missao
    print(m2.resgatar())                                # PRÓPRIO de Resgate
    # m2 NÃO foi concluída -> continua "Em andamento"

    print(m3.sabotar())                                 # PRÓPRIO de Sabotagem (nem iniciou ainda -> status "Pendente")

    # ---- Consultando o cadastro --------------------------------------------------------------
    mi6.listar()                                        # Usa o __str__ herdado de Missao para cada missão

    print(Panel("Missões pendentes", style="bold yellow"))
    for missao in mi6.buscar_por_status("Pendente"):    # Filtra pelo atributo status, que TODAS herdaram
        print(f"  {missao}")

    inspect(m1, methods=True)                           # Repare: infiltrar() é de Espionagem; iniciar/concluir vieram de Missao

    # Repare: m1.resgatar() daria ERRO (AttributeError), porque resgatar() é só de Resgate.
    # A herança vai do PAI (Missao) para o FILHO, nunca entre "irmãos"
    # (Espionagem, Resgate e Sabotagem só compartilham o que veio de Missao).


if __name__ == "__main__":                              # Só roda main() se este arquivo for executado direto
    main()                                              # (se for importado por outro módulo, não executa)
