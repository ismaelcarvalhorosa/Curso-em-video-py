# Aula 22 como importar e usar modulos caseiros 
import moeda

p = float(input('Digite um preço $:')) # p reprecenta preço 
print(f'Metade do valor: {moeda.moedaf(moeda.metade(p))}')
print(f'O dobro: {moeda.moedaf(moeda.dobro(p))}')
print(f'O aumentando 10%: {moeda.moedaf(moeda.aumento(p, 10))}')
print(f'Reduzir 13%: {moeda.moedaf(moeda.diminue(p, 13))} ')  