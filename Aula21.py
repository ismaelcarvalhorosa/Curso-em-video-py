# Aula 21 funsoes
import random
from time import sleep


def titulo(*txt):
    print('='*50)
    print(f'     Bem vindo aos exercicios da aula 21 🖖  ')
    print('='*50)
    print()

def validaNumero (texto):
    numeros=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lista=[]
    nStr = '' # string nesesaria para tranformar uma string em numero 
    n = 0

    for i in texto:
        if i in numeros:
            lista.append(i)
            junta = ''.join(lista)
            n = int(junta)
            #print('N:' n )
        else:
            print('.', i)
    return n 


# 101 _______
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Voto negado minha creança.'

    elif 16 <= idade < 18 or idade > 65:
        return f'Voto opcional.'

    else:
        return f'Voto obriagadorio.'

# 102 ________________


def fatorial(n, shuw=False):
    '''
     -> Fatorial .
      Parametro n = O número a ser calculado
      Parametro shuw = Verifica se vai mostrar o calculo inteiro
      
    '''
    f = 1
    lista = list()
    for i in range(n, 0, -1):
        if shuw == True:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(f' = ', end='')
        f *= i
    return f

# 103 ____________________
def ficha(jogador , gols):
    if jogador.strip() == '':
        jogador = 'Desconhecido'
    if gols.isnumeric():
        gols = int(gols)
        print(f'Jogador {jogador} com um total de {gols}')
    else:
        print(f'Jogador {jogador} com um total de = 0')

# 104 ____________________
def leiaint(msg):
    lista = ['Erro! isso não é um numero cara', 'Cara você é chato! ', 'Não sabe ler ? isso não é um número', 
            'Não seja teimosso!', '😠', '😤', '🤬']

    ok = False
    v = cont = i = 0 
    while True :
        n = input(msg)
        if n.isnumeric():
            v = int(n)
            ok = True
        else:
            if cont == 0:
                print('\033[0;31m Erro! isso não é um numero cara! \033[m')
            elif cont < 5:
                i = random.randint(1, 5)
                print(f'\033[0;31m {random.choice(lista)} \033[m')
            elif cont == 6 :
                for c in range(0, 3):
                    print(' 😡 ', end='')
                    sleep(0.4) 
                print('')               
            else:
                print('\033[0;31m ...  \033[m')
            cont +=1
        if ok :
            break
    return v 

# 105 ________
def nota(*n, situa=False):
    '''
        n = Receme varias notas como parametro 
        situa = recebe como parametro True ou Fase para mostrar na tela a situação do aluno
        True = mostra na tela 
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)

    if situa:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >=5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'
    return r  


# ================================================================================
#                            Programa principal
# ================================================================================
print()
titulo()
menu = input('  Menu: ')
print(f' {menu} 👀')
sleep(1)
print()

# Voto ____________________________________
if menu == '101':
    texto = input('Ano de nacimento: ').strip()
    ano = validaNumero(texto)
    print(voto(ano))

# Fatorial _________________________________
if menu == '102':
    print(fatorial(shuw=True, n=5)) # ou False para não mostrar o calculo 
    #help(fatorial)

# Nome do jogador ___________________________
if menu == '103':
    jogador = input('Nume do jogador: ')
    gols = input('Quandos gols? ')
    ficha(jogador, gols)

# Valida número _____________________________
if menu =='104':
    n = leiaint('Digite um número: ')
    print(f'"Obrigado por ter digitado um número"!👍 \n Número: {n}')

# Media mais uma vez ________________________
if menu =='105':
    resp = nota(7, 5, 6, 5, 9, 10, 8, situa=True)
    #print(resp)
    help(nota)
