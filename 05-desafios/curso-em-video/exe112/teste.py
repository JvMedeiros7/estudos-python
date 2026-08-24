from utilidadescev import moeda
from utilidadescev import dado



p = dado.leiaDinheiro('Digite o preço: R$ ')
aumento = float(input('Digite a porcentagem de aumento: '))
diminuicao = float(input('Digite a porcentagem de diminuição: '))
moeda.resumo(p, aumento, diminuicao)   