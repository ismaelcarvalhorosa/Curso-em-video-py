# Aula 22 como importar e usar modulos caseiros
#  
import moeda

p = float(input('Digite um preço $:')) # p reprecenta preço 
print(f'Metade do valor: {moeda.metade(p, True)}')
print(f'O dobro: {moeda.dobro(p, True)}')
print(f'O aumentando 10%: {moeda.aumento(p, 10, True)}')
print(f'Reduzir 13%: {moeda.diminue(p, 13, True)} ')  