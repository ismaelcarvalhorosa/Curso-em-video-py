def metade(preco = 0, formato=False):
    '''
    Divede o preço pela metade 
    '''
    res = preco/2
    return res if formato is False else moedaf(res)

def dobro(preco = 0, formato=False):
    res = preco*2
    return res if formato is False else moedaf(res)

def aumento(preco = 0, taxa = 0, formato=False ):
    res = preco + (preco * taxa/100)
    return res if formato is False else moedaf(res)

def diminue(preco = 0, taxa = 0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moedaf(res)

def moedaf(preco = 0, moeda = 'R$', formato=False):
    return f'{moeda} {preco:>8.2f}'.replace('.', ',')

def resumo(preco=0, taxaA=10, taxaR=5):
    print('-'*40)
    print('Resomo de valores'.center(40))
    print('-'*40)
    print(f'Preço analisado: \t{moedaf(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Taxa: {taxaA}%, Aumento:\t{aumento(preco, taxaA, True)}')
    print(f'Taxa:{taxaR}% Retução:\t{diminue(preco, taxaR, True)} ')