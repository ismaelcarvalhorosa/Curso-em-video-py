import time 
import random

def titulo(*txt):
    print('='*50)
    print(txt)
    print('='*50)
    print()

def subtitulo(*txt):
    print('-'*50)
    print(f'           {txt}     ')
    print('-'*50)
    print()


# 96 __________________
def AreaQuatrada(a, b):
    area = a * b
    print('Resultado da área: ', area)

# 97 _____________
def escreva(texto):
    t = len(texto) + 2
    print(f'-'*t)
    print(f' {texto}')
    print('-'* t)

# 98 ____________________________
def contagem(inicio, fim, passo):
    if passo <0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        for i in range(inicio, fim, passo):
            print(i, end='  ')
            time.sleep(0.5)
    else:
        for i in range(inicio, -fim, -passo):
            print(i, end='  ')
            time.sleep(0.5)
    print('')

# 99 ___________
def maior(*n):
    n1 = 0
    for i in n:
        if n1 < i :
            n1 = i 
    print(f'\n Parametro {n} O maior deste parametro é :{n1}')

# 100 _____________
def sorteia(lista):
    for i in range(0, 5):
        n = random.randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        time.sleep(0.4)
    print('  Sorteado ... \n')

    
def par(lista):
    soma = 0
    for i in lista:
        if i % 2 ==0:
            soma += i
    print(f'A lista {lista} A soma dos pares: {soma} ')



# ================================================================================
#                            Programa principal 
# ================================================================================

print()
titulo('   Bem vindo aos exercicios da aula 20 🖖  ')
menu = input('  Menu: ')
print(f' {menu} 👀')

# _____________ Area quadrada ___________
if menu =='96':
    subtitulo(f' Área quadarda ')
    a = int(input('Largura(M): '))
    b = int(input('Comprimento(M): '))
    AreaQuatrada(a, b)

# ____________ Escreva __________________
if menu =='97':
    texto = input('Texto: ')
    escreva(texto)

# ________ Contagem de números _________
if menu=='98':
    inicio = fim = passo = 0
    subtitulo('        Contagem')
    inicio = 1
    fim = 11
    passo = 1
    contagem(inicio, fim, passo)
    inicio = 10
    fim = 0
    passo = 2
    contagem(inicio, fim, passo)
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passos: '))
    contagem(inicio, fim, passo)

# ________ Recebe farios parametros _______
if menu =='99':
    subtitulo('   Recebe varios parametros')
    maior(2, 4, 5, 6, 1, 6, 3, 8, 9, 2, 10)
    maior(4, 6, 8)
    maior(1)

# _________ Sorteia por função ____________
if menu =='100':
    numero = list()
    print()
    sorteia(numero)
    par(numero)
    

