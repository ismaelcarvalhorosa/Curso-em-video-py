# aula 8 importação de bibliotecas


#import PIL
import math
import random
from datetime import date
from time import sleep
import os

print('\033[0;32;m           Aula 8 utilizando modulos ')

# ________________ menu ________________

print('Exercicios ', '\n' * 2)
print('16 = numero inteiro ')
print('17 = teorema de pitagoras')
print('18 = seno cosseno e tangente')
print('19 = sorteio de aluno')
print('20 = sorteio apresentação')

print()

# _______________ corpo ________________


menu = input('menu:')

if menu == '00':
    print('\n      cores de texto \n')
    print('\033[0;32;0m cor de texto = amarelo')
    print('\033[1;32;0m cor de texto = amarelo')
    print('\033[4;32;0m cor de texto = amarelo')
    print('\033[7;32;0m faixa amarela texto preto')
    print('\033[0;31;0m cor de texto = vermelho')
    print('\033[0;33;0m cor de texto = amarelo queimado')
    print('\033[0;34;0m cor de texto = azul')
    print('\033[0;35;0m cor de texto = roxo')
    print('\033[0;36;0m cor de texto = verde')
    print('\033[0;37;0m cor de texto = cinza')
    print('\033[0;32;40m cor de texto')
    print('\033[0;32;41m cor de texto')
    print('\033[0;32;42m cor de texto')
    print('\033[0;32;43m cor de texto')
    print('\033[0;32;44m cor de texto')
    print('\033[0;32;45m cor de texto')
    print('\033[0;32;46m cor de texto')
    print('\033[0;32;47m cor de texto')

#     _______ numero inteiro ________

if menu == '16':
    print('numero inteiro \n')
    numero = float(input('digite um numero:'))
    print('O numero inteiro', int(numero))

#     ______ pitaguras (Hipotenusa) ________

if menu == '17':
    a = int(input('A²:'))
    b = int(input('b²:'))

    a = a * a
    b = b * b
    c = a + b

    print(' a={}\n b={}\n {}+{}\n c={}'.formato(a, b, a, b, c))
    print(' c= ¬v{}'.formato(c))
    c = c ** (1 / 2)

    print('sultado = ', c)

# __________ calculo de ângulo __________

if menu == '18':
    print('\n          Calculo de ângulo\n')

    angulo = float(input('qual é o ângulo?'))

    seno = math.sin(math.radians(angulo))
    cosseno = math.cos(math.radians(angulo))
    tangente = math.tan(math.radians(angulo))

    print('seno: {:.2f}'.formato(angulo, seno))
    print('cosseno: {:.2f}'.formato(cosseno))
    print('tangente: {:.2f}'.formato(tangente))

# _________ sorteio de aluno _____________

if menu == '19':
    alunos = ['rafael', 'teilor', 'guto', 'carol', 'alise', 'tati', 'jesica', 'gabriela', 'luana']
    print(' \n  sorteio de alunos \n ')

    item = random.choice(alunos)
    print('O aluno escolido é:', item)

# ___________ apresentação ________________

if menu == '20':
    i = 1
    alunos = ['rafael', 'teilor', 'guto', 'carol', 'alise', 'tati', 'jesica', 'gabriela', 'luana']
    print(' \n  sorteio de alunos \n a orde dos de apresentação é: \n ')

    for i in range(1, 5):
        item = random.choice(alunos)
        print('', i, '°', item)

        alunos.remove(item)

# ____________ nome completo _______________

if menu == '22':
    nome = input('digite um nome:')
    print(nome.upper())
    print(nome.lower())
    print(len(''.join(nome.split())))

# _________ casas de decimais ________
if menu == '23':
    listaNumero = ['Unidade', 'Dezena', 'Centena', 'Milhar', 'Milhão 🌽  ', 'Muitos milhão 🌽  ', '']
    n = 0
    contador = 1

    print('-' * 35)
    print('    Mostra as casas Decimais')
    print('-' * 35) 
    numero = input('\ndigite um numero:')
    for i in numero:
        if n > 5:
            print(i , ' = ', listaNumero[5], end='') 
            for e in range(0 , contador):
                print('🌽', end='')
            print()

            n = 5
            contador +=1    

        elif n <= 5 :    
            print(i, ' = ', listaNumero[n])
        n +=1
      


# ________________ cidade ____________________
if menu == '24':
    cidade = input('cidade:')
    cidade = cidade.strip()
    print('santo', 'santo' in cidade[0:5])

# ________________ pesquisar um nome ____________
if menu == '25':
    frase = input('digite uma frese ou texto: \n    ')
    nome = input('digite um nome de pesquisa:')

    print('pesquisa:', nome in frase)

# _________________ pesquisa de texto _____________
if menu == '26':
    texto = input('digite um texto: ')
    pesquisa = input('pesquisa:')
    print('o correncias de ', pesquisa, '=', texto.count(pesquisa))
    print('a primeira ocorrencia de', pesquisa, ' na posição=', texto.find(pesquisa) + 1)
    print('a última ocorrencia de', pesquisa, ' na posição=', texto.rfind(pesquisa) + 1)

# ___________________ nome completo ________________
if menu == '27':
    nome = input('nome completo:').strip()
    nome = nome.split()

    print('o primeiro nome é ', nome[0])
    print('o último nome é ', nome[len(nome) - 1])

# _________________ Adivenhe um numero ______________
if menu == '28':

    numero = random.randint(0, 5)

    resposta = int(input('qual numero estou pensando?'))

    if resposta == numero:
        print('você acertou :)')
        print('numero certo é :', numero)

    else:
        print('errooo!!!')
        print('numero certo é :', numero)

# _________________ velocidade _____________________
if menu == '29':
    velocidade = int(input('qual a velocidade em Km?'))

    if velocidade >= 81:
        multa = velocidade - 80
        multa = multa * 7

        print('você foi multado :D \n    kkk')
        print('multa de ', multa)

    else:
        print('ta tranquilo :)')

# ________________ par ou inpar ___________________
if menu == '30':
    numero = int(input('numero:'))

    if (numero % 2 == 0):
        print('par')

    else:
        print('inpar')

# _________________ viagem ___________________________
if menu == '31':
    viagem = int(input('qual a distacia da viagem em Km?'))

    if viagem <= 200:
        print('viagem curta \n $=', viagem * 0.50)
    else:
        print('viagem longa \n $=', viagem * 0.45)

# _______________ ano bissexto? _________________
if menu == '32':
    ano = int(input('ano Bissexto?\nano:'))

    if ano == 0:
        ano = date.today().year

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('ano bissexto')

    else:
        print('não bissesto')

#  ________________ > or < ______________
if menu == '33':
    ok = 'ok'
    maior = 0
    menor = 999999999

    while ok == 'ok':

        numero = int(input('numero:'))

        if maior <= numero:
            maior = numero
            print('<', maior)

        if menor >= numero:
            menor = numero
            print('>', menor)

# ____________ almento de salario __________
if menu == '34':
    salario = int(input('salario atual?'))

    if salario >= 1260:
        almento = 10 * (salario / 100)
        salario = salario + almento
        print(' almento de 10%  \n equivalente $ ', almento)
        print(' seu salario novo ficara ', salario)

    if salario <= 1259:
        almento = 15 * (salario / 100)
        salario = salario + almento
        print(' almento de 15% \n equivalente $ ', almento)
        print(' seu salario novo ficara ', salario)

# ________________ triangulo ? __________________
if menu == '35':
    print('       triangulo ? \n')
    r1 = float(input('r1='))
    r2 = float(input('r2='))
    r3 = float(input('r3='))

    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('\n pode formar um triangulo ')

    else:
        print('\n não pode ')

# _______________  emprestimo bancario ___________
if menu == '36':
    salario = 0

    print('      emprestimo \n')
    casa = float(input('qual é o valor da casa?'))
    salario = float(input('qual é o salario?'))
    anos = int(input('em quantos anos?'))

    parcelas = casa / (anos * 12)
    vezesparcelas = anos * 12

    print('\nvalor parcelas:', parcelas)
    print('            vezes:', vezesparcelas)

    if parcelas <= 30 * (salario / 100):
        print('cretito aprovado :)')

    else:
        print('negado!')

# ______________ base numerica _______________
if menu == '37':
    print('\033[0;36;0m-' * 30)
    print('\033[0;34;0m       base numerica  ')
    print('\033[0;36;0m-' * 30)
    numero = int(input(' qual o numero?'))
    base = int(input('''qual é a base? 
    
        1- binario         10011
        2- octal           1234567
        3- hexadecimal     ea
            
    \a'''))

    if base == 1:
        print('\nbinerio:', bin(numero)[2:])

    elif base == 2:
        print('\noctal:', oct(numero)[2:])

    elif base == 3:
        print('\nhexadecimal:', hex(numero)[2:])

    else:
        print('essa opção não existe =/')

#  ___________ qual é o numero maior  _________
if menu == '38':
    continua = 's'
    n2 = 0

    print('\n    numero maior? \n')
    n2 = int(input('numero:'))
    print('1º numero')

    while continua == 's':

        n = int(input('numero:'))
        if n2 == n:
            print('\n  = \n')
            n2 = n

        elif n2 > n:
            print('\n o 1º é maior > \n')
            n2 = n

        else:
            print('\n o 2º é >  \n')
            n2 = n

        continua = input('quer continuar?')

# _____________ alistamento militar _____________
if menu == '39':
    ano = date.today().year
    print('\033[0;36;0m ')
    print('-' * 35)
    print('     alistamento militar ')
    print('-' * 35)
    anonacimento = int(input('qual ano nacimento?'))
    idade = ano - anonacimento

    print('idade:', idade)

    if idade == 18:
        print('precisa de alistar!')

    elif idade < 18:
        fata = 18 - idade
        print('ainda não meu jovem')
        print('ainda falta ', fata, 'anos')

    else:
        falta = idade - 18
        print('ja passou da idade !')
        print('esta atrasado ', falta, 'ano')

# ____________ media de nota _______________
if menu == '40':
    n1 = float(input('1º nota:'))
    n2 = float(input('2º nota:'))

    media = (n1 + n2) / 2
    print('\n nota:', media)

    if media < 5.0:
        print('\n reprovado! :(')

    elif media > 5.0 and media < 6.9:
        print('\n recuperação')

    else:
        print('\n aprovado !!!!!!!  :)')

# ______________ natação ______________
if menu == '41':
    idade = int(input('qual é a sua idade?'))

    if idade <= 9:
        print('\n mirim ')

    elif idade > 9 and idade <= 14:
        print('\n infantil')

    elif idade > 14 and idade <= 19:
        print('\n junior')

    elif idade == 20:
        print('\n senior')

    elif idade > 20:
        print('\n master')

        if idade >= 85:
            print('esta meio velho não acha ?')

    else:
        print('idade estranha !')

# _______________ tipo de triangulo _____________
if menu == '42':
    print('\n     tipos de triangulo /\_ \n')

    r1 = int(input('r1:'))
    r2 = int(input('r2:'))
    r3 = int(input('r3:'))

    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('\n pode formar um triangulo \n')

        if r1 == r2 == r3:
            print('Equilátero')

        elif r1 == r2 or r1 == r3 or r2 == r3:
            print('Isósceles')

        else:
            print('Escaleno')


    else:
        print('\n não pode formar um triangulo !')

# _________________ I M C ________________
if menu == '43':
    print('\n  ________ I M C _______ \n')
    peso = float(input('peso:'))
    altura = float(input('altura:'))

    imc = peso / (altura * altura)
    print('imc= ', imc)

    if imc < 18.5:
        print('\n você esta abaixo do peso meu carro')

    elif imc >= 18.5 and imc < 25:
        print('\npesso edeal :)')

    elif imc >= 25 and imc < 30:
        print('\nsobre peso ')

    elif imc >= 30 and imc < 40:
        print('\nobesidade! você esta gordo ')

    elif imc > 40:
        print('\ncara você esta muito gordo esta com obesidade mórbida')

# ___________ tipo de pagamento ________
if menu == '44':
    print(' - - - - ' * 5)
    print('      tipo de pagamento ')
    print(' - - - - ' * 5)

    valor = float(input('\n $ valor?'))
    pagamento = input('''tipo de pagamento?
      
      1- avista
      2- avista no cartão 
      3- em até 2x no cartão 
      4- 3x ou mais \n''')

    if pagamento == '1':
        descondo = 10 * (valor / 100)
        total = valor - descondo
        print(' 10% de descondo \n que vai ser de ', descondo)
        print('total', total)

    elif pagamento == '2':
        descondo = 5 * (valor / 100)
        print(' 5% de descondo \n que vai dar o valor ', descondo)

    elif pagamento == '3':
        print('\n preço normal, valor $:', valor)

    elif pagamento == '4':
        juros = 20 * (valor / 100)
        total = valor + juros
        print('\n 20% de juros, valor em $:', juros)
        print('total: ', total)

    else:
        print('\n opção não encontrada!')

# ____________________ Pedra Papel e Tesoura _________________
if menu == '45':
    lista = ['sair', 'ext', 'n', 'fui', 'tabom por hoje', 'ja chega']
    continua = 's'

    while continua == 's':

        item = ['', 'Pedra', 'Papel', 'Tesoura']  # menu do jogo

        maquina = random.randint(1, 3)

        jogador = int(input(''' 
           ------------------------------------     
                pedra papel e tesoura 
           ------------------------------------
                
             1 - Pedra 
             2 - Papel
             3 - Tesoura
              '''))

        print('\n Pedra ', end='')
        sleep(1)
        print(' Papel ', end='')
        sleep(1)
        print(' Tesoura ')

        print('\njogador:', item[jogador])
        print('Maquina:', item[maquina])

        if maquina == 1 and jogador == 3:  # define quem ganhou
            print('\033[0;34;0m \n  Vitoria da Maquina !!!')

        elif maquina == 2 and jogador == 1:
            print('\033[0;34;0m \n  Vitoria da Maquina !!!')

        elif maquina == 3 and jogador == 2:
            print('\033[0;34;0m \n  Vitoria da Maquina !!!')

        elif jogador == 1 and maquina == 3:
            print(' \033[0;34;0m \n Vitoria do jogador !!!')

        elif jogador == 2 and maquina == 1:
            print(' \033[0;34;0m \n Vitoria do jogador !!!')

        elif jogador == 3 and maquina == 2:
            print(' \033[0;34;0m \n Vitoria do jogador !!!')

        elif jogador != 1 and jogador != 2 and jogador != 3:
            print('\n opção incorreta \n maquina ganhou ')

        else:
            print('\n  empate ')

        i = input('\033[0;32;0m \n sair ? ')

        if i in lista:
            continua = 'n'

# _____________ contagem regreciva __________
if menu == '46':
    for i in range(10, 0, -1):
        print('* ' * 30)
        print('     fogos de artificio ')
        print('* ' * 30)
        print('\n contagem:', i)
        sleep(1)
        print('\n' * 100)

    print('  !!!!!!  FOGO !!!!!!')

# ___________ só mostra numeros par ___________
if menu == '47':
    print('\n     Só par \n')
    n = int(input('Digite um número:'))

    for i in range(1, n):

        if i % 2 == 0:
            print(i)

    print('Fim ...')

# ______________ Muntiplos de três _______________
if menu == '48':
    cont = 0
    soma = 0

    print('\n    Muntiplo de três \n')

    for i in range(1, 500):
        if i % 2 != 0:
            if i % 3 == 0:
                print(i)
                cont += 1
                soma += i

    print('A soma é :', soma)
    print('Quantidade de nÚmeros contados:', cont)

# _______________ tabuada de novo _____________
if menu == '49':
    print('\n    tabuada \n ')
    n = int(input('Digite um numero:'))

    for i in range(1, 11):
        print(n, 'x', i, '=', n * i)

# _____________ Os 6 caminhos do calculo :) __________
if menu == '50':
    cont = 6
    soma = 0

    print('             6 6 6 ')
    print('        Os seis caminhos')
    print('          do calculo ')
    print('             9 9 9 \n')

    for i in range(6):
        print('Digite o número', cont, '°', end='')
        n = int(input(':'))
        cont = cont - 1

        if n % 2 == 0:
            print('Par \n')
            soma = soma + n
        else:
            print('Impar \n')

    print('\nA soma dos numeros par é ', soma)

# _________________ Razão PA ________________
if menu == '51':
    print('\n      Razão PA \n')
    termo = int(input('1° termo :'))
    razao = int(input('Razão:'))

    decimo = termo + (10 - 1) * razao

    for i in range(termo, decimo + 1, razao):
        print(i, '→', end='')

    print(' Fim...')

# __________ Número primo _______________
if menu == '52':
    divide = 0

    print('\n     Número primo \n')
    n = int(input('Digite um número:'))

    for i in range(1, n + 1):
        if n % i == 0:
            print('\033[34m', end='')
            divide += 1

        else:
            print('\033[33m', end='')

        print(i, end='')

    if divide == 2:
        print('\n\033[33m      \n Número primo')

    else:
        print('\n\033[33m      \n Não primo')

# _______________ Palindromo ________________
if menu == '53':
    inverso = ''

    frase = input('Digite uma frase:').strip().upper()
    palavra = frase.split()
    junto = ''.join(palavra)

    for i in range(len(junto) - 1, -1, -1):
        inverso += junto[i]

    print(junto, inverso)

    if junto == inverso:
        print('\n Palindromo')

    else:
        print('\n Não é um palindromo')

# ___________ Sete pessoas __________
if menu == '54':
    pessoa = 1
    menor = 0
    maior = 0
    ano = date.today().year

    print('\n      Maioridade \n')

    for i in range(0, 7):
        print('Pessoa ', pessoa, '°')
        nacimento = int(input('Digite o ano de nacimenta:'))
        idade = ano - nacimento
        print('Idade: \033[0;36;0m ', idade, '\033[0;32;0m')
        pessoa += 1

        if idade >= 18:
            maior = maior + 1

        else:
            menor = menor + 1

    print('Pessoas de maior idedade:', maior)
    print('Pessoas de menor idade:', menor)

# _________________ Qual é o mais gordo? _____________
if menu == '55':
    n = 1
    peso = 0
    peso1 = 0

    for i in range(0, 5):
        print('\nPessoa', n, '°')
        nome = input('Qual é o seu nome:')
        peso = int(input('\n qual é o seu pesso?'))
        n += 1

        if peso1 <= peso:
            peso1 = peso
            nome2 = nome
            print('\n\033[0;36;0m', nome, '\033[0;32;0m é a pessoa mais gordo')

        else:
            print('\n\033[0;36;0m', nome2, '\033[0;32;0m é a pessoa mais gordo 2')

# _________________ Analise de grupo ________________
if menu == '56':
    somaidade = 0
    mediaidade = 0
    maioridade = 0
    nomemaisvelho = 'Não teve Homem na lista'
    mulher = 0
    for i in range(0, 4):
        n = 0
        falida = 1
        print('-' * 30)
        print('     Pessoas ')
        print('-' * 30)

        nome = input('Seu nome?').strip()
        idade = int(input('Sua idade?'))
        while falida == 1:
            sexo = input('Qual é o seu sexo?[M/F]').strip().upper()
            n += 1
            if sexo == 'M' or sexo == 'F':
                falida = 0
            else:
                print('Digite apenas M ou F ')

            if n > 1:
                print('Você é burro ou o que?')

        if sexo == 'M' and idade > maioridade:
            maioridade = idade
            nomemaisvelho = nome

        if sexo == 'F' and idade < 20:
            mulher += 1
        somaidade += idade

    mediaidade = somaidade / 4
    print('\nA media de idade é =', mediaidade)
    print('homen mais velho =', nomemaisvelho, '  com idade=', maioridade)
    print('Mulheres com idade menor 20 =', mulher)

# ________________ Digite um sexo _____________
if menu == '57':
    n = 0
    falida = 1
    while falida == 1:
        sexo = input('Qual é o seu sexo?[M/F]').strip().upper()
        n += 1
        if sexo == 'M' or sexo == 'F':
            falida = 0
        else:
            print('Digite apenas M ou F ')

        if n > 1:
            print('Você é burro ou o que?')

    print('Certinho ate mais!')

# _________________ Adivenhe um numero 2 ______________
if menu == '58':
    numero = random.randint(0, 10)
    falida = 1
    tentadivas = 0
    resposta = int(input('Qual é o número que estou pensando?'))

    while falida == 1:
        if resposta == numero:
            print('você acertou :)')
            print('numero certo é :', numero)
            falida = 0

        else:
            print('\n Errooo!!!')
            resposta = int(input('Qual é o número que estou pensando?'))

        tentadivas += 1

    print('\n Você precisou de \033[0;36;0m', tentadivas, '\033[0;32;0m tentadivas')

# ________________ Dois valores _______________
if menu == '59':
    continua = 1
    while continua == 1:
        print('\n    Calculo \n')
        n1 = int(input('valor 1:'))
        n2 = int(input('Valor 2:'))

        menu2 = int(input('''

              Desaja fazer o que ?

                 [1] Somar
                 [2] Muntiplicar
                 [3] Maior
                 [4] Novos números
                 [5] Sair

                >  '''))
        if menu2 == 1:
            print('\n Somar:', n1 + n2)

        if menu2 == 2:
            print(n1, 'x', n2, '=', n1 * n2)

        if menu2 == 3:
            if n1 > n2:
                print('1º valor é maior  \n   ', n1, ' > ', n2)
            else:
                print('2º valor é maior  \n   ', n1, ' < ', n2)

        if menu2 == 4:
            print('novos valores!')

        if menu2 == 5:
            continua = 0

# ___________ Fatorial ___________
if menu == '60':
    print('\n    Fatorial \n')
    n = int(input('Digite um número:'))
    soma = n
    print(n, '! = ', end='')

    while n > 0:
        n1 = n
        n -= 1
        if n > 0:
            soma = soma * n
        print(n1, end='')
        print(' x ' if n > 0 else ' = ', end='')
        print(soma if n == 0 else '', end='')

# _______________ Razão de PA 2 _____________
if menu == '61':
    cont = 0
    print('\n      Razão PA \n')
    termo = int(input('1° termo :'))
    razao = int(input('Razão:'))

    while cont <= 10:
        print(termo, '→', end='')
        termo += razao
        cont += 1

    print(' Fim...')

# ______________ Razão de PA 3 ________________
if menu == '62':
    n = 1
    cont = 0
    cont2 = 9
    print('\n      Razão PA \n')
    termo = int(input('1° termo :'))
    razao = int(input('Razão:'))

    while n > 0:
        while cont <= cont2:
            print(termo, '→', end='')
            termo += razao
            cont += 1
        n = int(input('Quantos mais?'))
        cont2 += n
    print('Total de termos:', cont2)

# ________________ Sequemcia de Fibonacci _____________
if menu == '63':
    cont = 0
    n1 = 0
    n2 = 0
    print("\n         Sequencia de Fibonacci \n")
    n = int(input('Digite um número:'))
    n1 = n
    print(n)
    print(n1)

    while cont < 10:
        n = n + n1
        n1 = n - n1
        print(n)
        cont += 1

# _____________ 999 para _____________
if menu == '64':
    cont = 1
    soma = 0
    i = 0
    while cont == 1:
        print('\n      999 Para! \n')
        n = int(input('Digite um número:'))

        print('Números digitados:', i)
        i += 1

        if n < 999:
            soma += n

        else:
            cont = 0

    print('Resultado:', soma)

# _____________ Media e > ou < _____________
if menu == '65':
    print('\n      Media e > ou < \n')
    lista = ['s', 'sim']
    lista2 = ['n', 'não', 'nao']
    cont = 's'
    soma = 0
    i = 0
    menor = 9999
    maior = 0

    while cont in lista:
        n = int(input('Número:'))
        i += 1
        soma += n

        cont = input('Quer continuar?')

        if cont in lista:
            print('.')

        elif cont in lista2:
            print('\n Finalizar!')
            cont = 'n'

        else:
            print('\n Opção errada')
            cont = 's'

        if n > maior:
            maior = n

        elif n < menor:
            menor = n

    print('\n    Resultado ')
    print('Media:', soma / i)
    print('Maior:', maior)
    print('Menor:', menor)

# _____________ 999 para 2 _____________
if menu == '66':
    cont = 1
    soma = 0
    i = 0
    while True:
        print('\n      999 Para! \n')
        n = int(input('Digite um número:'))

        print('Números digitados:', i)
        i += 1

        if n < 999:
            soma += n

        else:
            break

    print('Quntidade de números digitados:', i)
    print('Resultado:', soma)

# _______________ Tabuada 3 __________________
if menu == '67':
    print('\n    tabuada \n ')

    while True:
        print('-' * 30)
        n = int(input('Tabuada:'))
        print('-' * 30)

        for i in range(1, 11):
            print(n, 'x', i, '=', n * i)

        if n < 0:
            break

# _____________ Par ou inpar 2 ________________
if menu == '68':
    vidorias = 0
    print('\n    Par ou impar ?  \n')

    while True:
        while True:
            opcao = input('Impar (I)  ou par (P)?').upper()

            if opcao == 'I' or opcao == 'P':
                break

            else:
                print('\n Opção ivalida!  -\_(:/)_/-')

        n = int(input('Digite um numero:'))
        intem = random.randint(0, 10)
        r = n + intem

        print('\n', r)

        if r % 2 == 0:
            print('\nPar')
            if opcao == 'P':
                print(' Jogador ganhou !')
                vidorias += 1

            elif opcao != 'P':
                print('Maquina ganhou!')
                break

        else:
            print('\nImpar!')
            if opcao == 'I':
                print('Maquina ganhou!')
                break

            else:
                print('Jogador ganhou!')
                vidorias += 1

    print('\n O jogador tem um total de vidorias=', vidorias)

# _________________ Analise de cadastro _________________
if menu == '69':
    pessoa18 = 0
    pessoa20 = 0
    homes = 0
    idade = 0
    sexo = ''
    f = 0
    m = 0

    while True:
        print('-' * 30)
        print('        Cadastro ')
        print('-' * 30)

        idade = int(input('\n Idade:'))
        while True:  # ______________________________________ valida sexo
            sexo = input('Sexo:').upper()
            if sexo == 'M' or sexo == 'F':
                break

            else:
                print('Valor errado M ou F \n')

        while True:  # ______________________________________ valida continua
            continua = input('Quer continuar? (s/n)').upper()
            if continua == 'N':
                break

            elif continua == 'S':
                print('\n')
                break

            else:
                print('Valor errado S ou N \n')

        if continua == 'N':
            break

        if sexo == 'M':
            m += 1

        if idade > 18:
            pessoa18 += 1

        if sexo == 'M' and idade < 20:
            pessoa20 += 1

    print('\nPessoas com + 18: ', pessoa18)
    print('Homes :', m)
    print('Mulheres com - 20:', pessoa20)


# _________________ Produto mais barato _________________
if menu == '70':
    continua = ''
    barato = ''
    produto = ''
    p = 0
    precoB = 9999
    caro=0
    total = 0

    while True:
        print('-' * 30)
        print('        Combras  ')
        print('-' * 30)

        produto = input('\n Produto:')
        p=int(input('Preço:'))

        while True:  # ______________________________________ valida continua
            continua = input('Quer continuar? (s/n)').upper()
            if continua == 'N':
                break

            elif continua == 'S':
                print('\n')
                break

            else:
                print('Valor errado S ou N \n')

        if p < precoB:
            precoB = p
            barato = produto

        if p > 1000:
            caro +=1

        total = total + p # _________________________total

        if continua == 'N': # __________________________ Saiu do laço
            break

    print('\nTotal = ', total)
    print('Com valor acima de 1.000 = ', caro)
    print('+ Barato = ', barato, '$', precoB)

# ______________ Caixa de banco ____________
if menu =='71':
    nota50=0
    nota20=0
    nota10=0
    nota1=0

    print('\n   Caixa de banco \n')
    n=int(input('Valor:'))

    while True:
        if n >= 50:
            nota50 = n / 50
            n = n % 50
            print('Notas de 50:$', round(nota50))

        elif n >= 20:
            nota20 = n / 20
            n = n % 20
            print('Notas de 20:$', round(nota20))

        elif n >= 10:
            nota20 = n / 10
            n = n % 10
            print('Notas de 10:$', round(nota10))

        elif n >= 1:
            nota1 = n / 1
            n = n % 1
            print('Notas de 1:$', round(nota1))
            break

# ____________ Fala o número _____________
if menu == '72':
    n = (0, 'Zero', 1, 'Um', 2, 'Dois', 3, 'Três', 4, 'Quatro', 5, 'Sinco', 
         6, 'Seis', 7, 'Sete', 8, 'Oito', 9, 'Nove', 10, 'Dez', 11, 'Onze', 12, 'Doze',
         13, 'Treze', 14, 'Quatorze', 15, 'Quinze', 16, 'Dizeseis', 17, 'Dizesete',  18, 'Dizoito',
         19, 'Dizenova', 20, 'Vinte' )
         

    while True:
        opcao=int(input('Digite um número entre 0 e 20:'))
        if opcao >= 0 and opcao <= 20:
            break
        else:
            print('\n Entre 0 e 20! \n')
    
    item = n.index(opcao)
    item +=1
    print('\n', n[item])

# _______________ Times do Brasileirão _______________
if menu == '73':
    cont=10
    times=('', 'Athletico-PR  ', 'Botafogo  ',  'Avaí  ', 'Bahia  ', 'Atlético-MG  ', 'CSA  ', 'Ceará  ', 'Chapecoense  ', 'Corinthians  ', 
            'Cruzeiro  ', 'Flamengo  ', 'Fluminense  ', 'Fortaleza  ', 'Goiás  ', 'Grêmio  ', 'Internacional  ',
            'Palmeiras  ', 'Santos  ', 'São Paulo  ', 'Vasco  ')

    for i in range (1, len(times)):
        print(i,'° = ', times[i])

    print('\n'*2, 'Os 5 primeiros times:')
    for i2 in range(1, 6):
        print(times[i2], end='')

    print('\n'*2, 'Os 4 ultimos colocados:')
    for i3 in range(-4, 0):
        print(times[i3], end='')
        
    print('\n'*2, 'Em ordem alfabetica:')
    
    for i4, item in enumerate(sorted(times)):
        print(item, end='')
        if i4 == 10 :
            print()  

        
# ______________ Sorteio de uma tupla ___________
if menu =='74':
    n = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),random.randint(0, 10), random.randint(0, 10))

    print('Os números são:', n)
    print('Maior valor :', max(n))
    print('Menor número:', min(n))

# _______________ Copiar tuplas __________________
if menu=='75':
    n1=int(input('n1:'))
    n2=int(input('n2:'))
    n3=int(input('n3:'))
    n4=int(input('n4:'))

    tupla=(n1, n2, n3, n4)

    print(tupla)
    print('Valor nove:', tupla.count(9))
    if 3 in tupla:
        print('O valor três aparece na posição:', tupla.index(3))
    print('Os valores pares:', end='')

    for i in range(0, len(tupla)):
        if tupla[i] % 2 ==0:
            print(tupla[i], end=', ')
    
    print('...')

# ________________ Lista de conpras ____________
if menu =='76':
    i2=0
    lista=('Flango! ', 1 , 'Peneu de caminhão ', 250, 'Teclado', 25)

    print('_'*40 ,'\n')

    for i in range(0, len(lista)):
        if i % 2 ==0:
            print(f'{lista[i]:.<30}', end='$ ')
        else:
            print(lista[i])

    print('_'*40)

# _________________ Vogais _______________________
if menu =='77':
    lista=('Teologia', 'teste', 'Fisica', 'Crash')

    for posicao, palavra in enumerate(lista):
        print('\n', palavra, ': ', end='')
        for posicao2, letra in enumerate(palavra):
            if letra == 'a' or letra =='e' or letra == 'i' or letra == 'o' or letra == 'u':
                print(letra, end='. ')

    print()

# ________________ Maior e menor 3 ______________
if menu =='78':
    lista=[]
    maior = 0
    pos1 = 0
    pos2 = 0
    menor=99999

    for i in range(0, 5):
        lista.append(int(input('Digite um número: ')))

    for posicao, i in enumerate(lista):
        if i > maior :
            pos1 = posicao
            maior=i

        if i < menor :
            pos2 = posicao
            menor=i
        
    print('Lista: ', lista)
    print('Número maior', maior, 'na posição: ', pos1)
    print('Número menor', menor, 'na posição: ', pos2)

# _______________ Adicionando a lista ________________
if menu =='79':
    numeros=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sair=['s', 'sair', 'exet']
    lista=[]
    print('\nDigite s ou sair para sair ')

    while True:
        
        n=input('Número:')

        if n in sair:
            break

        elif n not in numeros:
            print('Isso não é um numero!')

        elif n in lista:
            print('Esse numero ja existe!')
        
        else:
            lista.append(n)
    lista.sort()
    print('Os numeros digitados: ', lista)

# ______________ Lista ordenada na tela ___________
if menu =='80':
    lista=[]
    i=0

    for i in range(0, 5):   
        n=int(input('Número:'))

        if i == 0 or n > lista[-1]:
            lista.append(n)

        else:
            pos = 0 
            while pos < len(lista):
                if n <= lista[pos]:
                    lista.insert(pos, n)
                    break

        print('lista : ', lista)

# _____________ Enúmera  lista ______________
if menu =='81':
    numeros=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sair=['s', 'sair', 'exet']
    lista=[]
    print('\nDigite s ou sair para sair ')

    while True:
        
        n=input('Número:')

        if n in sair:
            break

        for i in range(0, len(n)):
            if n[i] not in numeros:
                print('Isso não é um numero!')
                break
        
        else:
            n1 = int(n)
            lista.append(n1)
    lista.sort(reverse=True)
    print('Quandos números voram digitados:', len(lista))
    print('Orden decrecente: ', lista)

    if 5 in lista:
        print('5 foi digitado')

    else:
        print('5 não foi digitado')

# ________________ Listas com pares e impares ______________
if menu =='82':
    numeros=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sair=['s', 'sair', 'exet']
    lista=[]
    par=[]
    impar=[]
    x=0
    n1=0

    while True:
            
        n=input('Número:')

        if n in sair:
            break

        for i in range(0, len(n)):
            if n[i] not in numeros:
                print('Isso não é um numero!')
                break
            
            else:
                n1 = int(n)
                lista.append(n1)
        
     

    for p in range(0, len(lista)):
        if lista[p] % 2 ==0:
            par.append(lista[p])

        else:
            impar.append(lista[p])

    print('Lista:', lista)
    print('Par: ', par)
    print('Impar:', impar)


# ______________ Expressão esta certa? ____________
if menu =='83':
    lista=[]

    n = input('Expressão: ')

    for sibolo in n:
        if sibolo == '(':
            lista.append('(')
        
        elif sibolo ==')' :
            if len(lista) > 0:
                lista.pop() 

            else:
                lista.pop()

    if len(lista) == 0:
        print('É valido ')

    else:
        print('Não é valido')   

# _____________ Guarda nome de pessoas ______________
if menu=='84':
    numeros =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sair =['s', 'sair', 'exet']
    lista = list()
    temp = list()
    acima = list()
    abaixo = list()
    pesso = n = n1 = media = valida = 0

    print('s ou sair para sair ')
    while True:
        nometemp=input('Nome:')
        if nometemp in sair:
            break
        
        valida = 0
        temp.append(nometemp)
        while valida < 1:
            n=input('Pesso da criatura? ')
            for i in range(0, len(n)):
                if n[i] not in numeros:
                    print('Isso não é um numero!')
                    break
            
            else:
                n1 = float(n)
                temp.append(n1)
                pesso += n1
                valida = 1
        
        lista.append(temp[:])
        temp.clear()

    print(f'Pessoas cadastradas: {len(lista)}')
    
    media = pesso / len(lista)
    for i in lista:
        if i[1] > media:
           acima.append(i[:])
        
        else:
            abaixo.append(i[:])
    
    print('\n Os mais gordos:')
    for item in acima:
        print(f'   {item[0]}: {item[1]} kg,  ' , end='')

    print('\n'*2, 'Os mais magrinhos | :')
    for item in abaixo:
        print(f'   {item[0]}: {item[1]} kg,  ' , end='')

    print('\n...')


# _________________ Par ou impar com listas ______________
if menu == '85':
    lista = list()
    par = list()
    impar = list()

    for i in range(0, 7):
        n = int(input('Numero: '))

        if n % 2 == 0 :
            par.append(n)

        else:
            impar.append(n)


    lista.append( par[:])
    lista.append(impar[:])
    lista[0].sort()
    lista[1].sort()
    print('\nOs numeros pares :', lista[0])   
    print('Os numeros impar : ', lista[1])
   

# ______________________ Matriz __________________
if menu == '86':
    lista = list()
    cont= 1

    for i in range(1, 10):
        lista.append(input('Numero :'))

    for i2 in range(0, 9):
            print(f'[{lista[i2]:^5}] ', end='') 
            if cont >= 3 :
                cont = 0
                print() 

            cont += 1
    print('\n ...')

# __________________ Matriz 2 _____________________
if menu =='87':
    lista = list()
    maior = par = terceira = 0
    cont= 1


    for i in range(1, 10):
        lista.append(int(input('Numero :')))

    for i2 in range(0, 9):
        print(f'[{lista[i2]:^5}] ', end='') 
        if cont >= 3 :
            cont = 0
            terceira += lista[i2]
            print() 

        if lista[i2] % 2 ==0:
            par += lista[i2]
        
        cont += 1
        
    for i3 in range(3, 6):
        if lista[i3] > maior:
            maior = lista[i3]

        
    
    print('-'*30)
    print('Soma dos pares: ', par)
    print('Soma dos valores da 3° coluna: ', terceira)
    print('Maior valor da coluna 2°: ', maior)
    print('\n ...')

# ___________________ Sorteio Mega _________________
if menu =='88':
    lista = list()
    temp = list()
    vezes = 0

    vezes = int(input('Quatidade de vezes? '))
    print('Os numeros são :')

    for i in range(0, vezes):

        n = (random.randint(1, 60), random.randint(1, 60), random.randint(1, 60), random.randint(1, 60), random.randint(1, 60), random.randint(1, 60))
        lista.append(n)

        print(lista[i])
        sleep(1)

# _________________ Notas de alunos __________________
if menu =='89':
    sair =['s', 'sair', 'exet']
    lista = list()
    nome = list()
    cont = media = 0

    print('\n         Notas dos alunos \n   ')
    
    while True :
        nometemp = input('Nome do aluno: ')
        if nometemp in sair:
            break
        
        else:
            nome.append(nometemp)
            cont +=1

        n1 = int(input('Nota 1 :'))
        n2 = int(input('Nota 2 :'))

        media = (n1 + n2 )/ 2
        nome.append(n1)
        nome.append(n2)
        nome.append(media)

        lista.append(nome[:])
        nome.clear()

        print('Lista:', lista)

    print('[ Id     Nome     Media ] ')
    print('-'*40)
    for i, item in enumerate(lista):
        print(f'{i}       {item[0]:<10}        {item[3]} ')

    while True :
        aluno = int(input('Qual aluno? '))
        if aluno == 999:
            break

        for i2 in range(0, len(lista)):
            if i2 == aluno:
                print(f'Aluno: {lista[i2][0]}   Notas: {lista[i2][1]} e {lista[i2][2]}')

# _________________ Media de um aluno _________________
if menu =='90':
    aluno = dict()

    aluno['nome'] = input('Nome do aluno ? ')
    aluno['nota'] = float(input(f'Media de {aluno["nome"]} ?'))

    if aluno['nota'] < 7 :
        print(f' {aluno["nome"]} você esta reporvado !')

    elif aluno['nota'] >= 7 :
        print(f' {aluno["nome"]}, você só fez a sua obrigação !')
        

# _________________ Jogo de dados _______________________
if menu =='91':
    from operator import itemgetter
    jogo ={ 'jogador1':random.randint(1, 6),
            'jogador2':random.randint(1, 6),
            'jogador3':random.randint(1, 6),
            'jogador4':random.randint(1, 6)}
    
    ranking = list()
    for k, v in jogo.items():
        print(f' {k} jogou = {v} ')
        sleep(1)
    
    print('-'*35)
    ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
    for n, item in enumerate(ranking):
        print(f'{n+1}° lugar {item[0]} com o valor {item[1]}.')
        sleep(1)

# ________________ Carteira de trabalho __________________
if menu =='92':
    cadastro = dict()

    cadastro['nome'] = input('Nome: ')
    nacimento = int(input('Ano de nacimento: '))
    CTPS = int(input('Carteira de trabalho (CTPS): '))
    ano = date.today().year
    cadastro['idade'] = ano - nacimento

    if CTPS != 0 :
        cadastro['contrato'] = int(input('Ano de contratação: '))
        cadastro['Salario'] = float(input('Salario $: '))
        cadastro['Aposemtadoria '] = cadastro['idade'] + (cadastro['contrato'] + 35) - ano

    else:
        print('Você não posui carateira.')

    for k, v in cadastro.items():
        print(f'{k} e tem {v}')

# ____________ Aproveitamendo de um jagador ___________
if menu =='93':
    dicionario = dict()
    partida = list()
    resultado = 0

    dicionario['nome'] = input('Nome do jogador: ')
    numeropartidas = int(input(f'Quandas partidas {dicionario["nome"]} jogador jogou? '))
    for i in range(0, numeropartidas):
        partida.append(int(input(f'Gols na {i+1}° : ')))
    dicionario['gols'] = partida[:]
    dicionario['total'] = sum(partida)
    
    print(f'O jogador {dicionario["nome"]} jogou um total de {len(dicionario["gols"])}')
    for item, v in enumerate(dicionario['gols']): # mostra as chaves e os itens 
        print(f'      Na partida {i+1} e fez {v} de gols')
    print('Com um total: ', dicionario['total'])

    
# ________________ Analise de grupo _________________
if menu =='94':
    lista = list()
    somaidade = list()
    mulher = list()
    listaSexo = list()
    pessoas = dict()
    m = soma = media = 0
    
    while True:
        pessoas.clear()
        nome = input('Nome: ') # nome 
        pessoas['nome'] = nome
        while True:                       # sexo   
            sexo = input('Sexo (F/M)? ').upper()[0] 
            if sexo == 'F' or sexo =='M':
                break
            else:
                print('F ou M')
            
        pessoas['sexo'] = sexo
        idade =int(input('Idade: ')) # idade
        soma += idade
        pessoas['idade'] = idade 
        somaidade.append(idade)
        lista.append(pessoas.copy())

        while True:
            continua = input('Quer continuar? (S/N)').upper()[0] # quer continuar ?
            if continua in 'SN':
                break
            else:
                print('S ou N')

        if continua == 'N':
            break
    
    print('-'*45)
    print('Pessoras cadastradas:', len(lista))
    media = soma / len(lista)
    print(f'Media de idade {media:5.2f}')
    for item in lista:
        if item['sexo'] in 'F':
            print(f'Mulheres no grupo: {item["nome"]}', end=', ')
    print('')
    for item in  lista:
        if item['idade'] > media:
            print('Os velhos: ', item['nome'], item['idade'], end=', ')
    print()

# ____________ Aproveitamendo de um jagador 2 ___________
if menu =='95':
    sair =['s', 'sair', 'exet']
    dicionario = dict()
    time = list()
    partida = list()
    resultado = 0
    
    while True:
        dicionario.clear()
        partida.clear()
        dicionario['nome'] = input('Nome do jogador: ')
        numeropartidas = int(input(f'Quandas partidas {dicionario["nome"]} jogador jogou? '))
        for i in range(0, numeropartidas):
            partida.append(int(input(f'Gols na {i+1}° : ')))
        dicionario['gols'] = partida[:]
        dicionario['total'] = sum(partida[:])
        time.append(dicionario.copy())  
        continua = input('Quer sair? ')
        if continua in sair:
            break             
        
    print('='*45)
    print('codgo   ', end='')
    for i in dicionario.keys():
        print(f'{i:<15}', end='')
    print()
    print('-'*45)
    for item, n in enumerate(time):
        print(f'{item:>3}      ', end='')        
        for d in n.values():
            print(f'{str(d):<15} ', end='')
        print('')
    print()
    print('-'*45)    
    while True:
        busca = int(input('Pesquisa de qual jogador(Codigo)? '))
        if busca == 999 :
            break
        if busca >= len(time):
            print('\nMolho a caminha não tem tudo isso não ...\n')
        else:
            print(f'______________ Levantamento {time[busca]["nome"]} ______________')
            for i, g in enumerate(time[busca]["gols"]):
                print(f'    No jogo: {i+1} fez {g} gols.')
            print('-'*45)
    print('...')
   # testes _______________________________
