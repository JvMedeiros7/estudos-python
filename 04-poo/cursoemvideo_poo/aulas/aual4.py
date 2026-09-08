"""
Tipos de armazenamento de variáveis
------------------------------------
Este arquivo mostra a EVOLUÇÃO de uma mesma ideia (dados de um Estado e seu
orçamento) passando por diferentes formas de armazenar/organizar dados em
Python, até chegar em Programação Orientada a Objetos (POO).
"""

# ============================================================
# 1) FORMA ANTIGA: listas + dicionários (variáveis compostas/estruturas)
# ------------------------------------------------------------
# Aqui os dados (nome do estado, orçamento) ficam separados da lógica
# (cálculos, prints). Tudo solto, sem nenhum "pacote" unindo dado + ação.
# ============================================================
'''
estados = ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Bahia"]

estados_orçamento = {
    "São Paulo": 150000,
    "Rio de Janeiro": 80000,
    "Minas Gerais": 60000,
    "Bahia": 40000}

for i, estado in enumerate(estados):
    print(f"{i+1} - {estado}")


escolha = int(input("Escolha um estado pelo número: "))

if 1 <= escolha <= len(estados):
    estado_escolhido = estados[escolha - 1]
    print(f"Você escolheu: {estado_escolhido}")
else:
    print("Escolha inválida. Por favor, selecione um número válido.")

print(f"vamos fazer uma programação para o ESTADO: {estado_escolhido}")


print(f"Orçamento para {estado_escolhido}: R$ {estados_orçamento[estado_escolhido]:.2f}")


orcamento = float(input("Digite o valor do orçamento: R$ "))
if orcamento > 100000:
    print("Orçamento alto, podemos investir em grandes projetos.")
elif orcamento > 50000:
    print("Orçamento médio, podemos investir em projetos de médio porte.")
elif orcamento >= 10000:
    print("Orçamento baixo, devemos focar em projetos menores.")
'''

# ============================================================
# 2) POR QUE EVOLUIR PARA POO?
# ------------------------------------------------------------
# - As variáveis foram evoluindo ao longo do tempo: simples -> compostas
#   -> estruturas -> objetos (POO).
# - A maior dificuldade nesse ponto é entender a diferença entre
#   variáveis simples, compostas e estruturas.
# - Com o paradigma de objetos, juntamos DADOS + FUNÇÕES em uma única
#   unidade: o objeto.
# - Uma variável comum só guarda dado. Um OBJETO guarda dado E também
#   executa funcionalidades (métodos) sobre esse dado.
# ============================================================


# ============================================================
# 3) CLASSE: o molde para criar objetos "Estado"
# ------------------------------------------------------------
# A classe define QUAIS atributos (dados) e QUAIS métodos (ações)
# todo objeto criado a partir dela vai ter.
# ============================================================
class Estado:

    # Método construtor (__init__): roda automaticamente sempre que um
    # novo objeto Estado é criado. É aqui que os atributos são definidos.
    # "self" representa o próprio objeto que está sendo criado.
    def __init__(self, nome, orcamento):
        # Atributos: dados que cada objeto Estado vai guardar
        # (cada objeto terá seu próprio nome e orçamento, independentes)
        self.nome = nome
        self.orcamento = orcamento

    # Método: ação que o objeto sabe executar, usando seus próprios atributos
    def exibir_orcamento(self):
        print(f"Orçamento para {self.nome}: R$ {self.orcamento:.2f}")

    # Método: analisa o atributo orcamento e classifica o resultado
    def avaliar_orcamento(self):
        if self.orcamento > 100000:
            print("Orçamento alto, podemos investir em grandes projetos.")
        elif self.orcamento > 50000:
            print("Orçamento médio, podemos investir em projetos de médio porte.")
        elif self.orcamento >= 10000:
            print("Orçamento baixo, devemos focar em projetos menores.")


# ============================================================
# 4) OBJETOS: instâncias criadas a partir do molde Estado
# ------------------------------------------------------------
# Cada objeto abaixo preenche os atributos definidos no __init__ e passa
# a ter seus próprios dados, independentes dos outros objetos.
# ============================================================
estado1 = Estado("São Paulo", 150000)
estado1.exibir_orcamento()     # usa o método com os dados de estado1
estado1.avaliar_orcamento()

estado2 = Estado("Amazonas", 20000)
estado2.exibir_orcamento()     # usa o método com os dados de estado2 (diferente de estado1)
estado2.avaliar_orcamento()

#O momento de instaciação é o momento de chamar o metodo construtor, que é o __init__ e ele vai receber os parametros que foram definidos no metodo construtor.

