# Aula 22 como importar e usar modulos caseiros 
import uteis.moeda
import uteis.dado

p = uteis.dado.leiaDinheiro('Digite um valor R$: ')
print(uteis.moeda.resumo(p, 10, 0))