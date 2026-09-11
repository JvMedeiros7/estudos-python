from rich import print
from rich.panel import Panel

#Considere:
# Consumo padrão : 400g por pessoa
# Preço : R$ 82,40/kg

class Churrasco:
    def __init__(self, nome_churrasco, num_pessoas):
        self.nome_churrasco = nome_churrasco
        self.num_pessoas = num_pessoas
        self.consumo_por_pessoa = 400  # em gramas
        self.preco_por_kg = 82.40  # em reais

    def calcular_quantidade_carne(self):
        return self.num_pessoas * self.consumo_por_pessoa

    def calcular_preco_total(self):
        quantidade_carne = self.calcular_quantidade_carne()
        return (quantidade_carne / 1000) * self.preco_por_kg

    def analisar(self):
        quantidade_carne = self.calcular_quantidade_carne()
        preco_total = self.calcular_preco_total()
        print (Panel(f"Nome do Churrasco: {self.nome_churrasco}\n"
                      f"Número de Pessoas: {self.num_pessoas}\n"
                      f"Quantidade de Carne Necessária: {quantidade_carne}g\n"
                      f"Preço Total: R$ {preco_total:.2f}", 
                      title="Resumo do Churrasco", subtitle="Detalhes"))

c1 = Churrasco("Churrasco de Domingo", 10)
c1.analisar()
