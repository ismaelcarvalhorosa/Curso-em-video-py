# Aula 22 como importar e usar modulos caseiros 
import moeda
import moedaForma

p = float(input('Digite um preço $:')) # p reprecenta preço 
print(f'Metade do valor: {moeda.metade(p)}')
print(f'O dobro: {moeda.dobro(p)}')
print(f'O aumentando 10%: {moeda.aumento(p, 10)}')
print(f'Reduzir 13%: {moeda.diminue(p, 13)} ')  