
def resumo(preco=0, taxa_aum=10, taxa_dim=5):
    
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))

    def aumentar(preco=0, taxa=0, formato=False):
        res = preco + (preco * taxa / 100)
        return res if formato is False else moeda(res)

    def diminuir(preco=0, taxa=0, formato=False):
        res = preco - (preco * taxa / 100)
        return res if formato is False else moeda(res)

    def dobro(preco=0, formato=False):
        res = preco * 2
        return res if not formato else moeda(res)

    def metade(preco=0, formato=False):
        res = preco / 2
        return res if not formato else moeda(res)

    def moeda(preco=0, moeda='R$'):
        return f'{moeda}{preco:>.2f}'.replace('.', ',')

    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa_aum}% de aumento: \t{aumentar(preco, taxa_aum, True)}')
    print(f'{taxa_dim}% de redução: \t{diminuir(preco, taxa_dim, True)}')

    print('-' * 30) 

