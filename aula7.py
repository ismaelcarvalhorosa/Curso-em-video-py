# coding=utf-8
#    orden de presendencia
#    1=()
#    2=**
#    3=* / // %
#    4= + -

import random
import math



sim='s'
r='s'
resposta=['sim', 'ok', 's', 'yes', 'y']
nao=['nao', 'não', 'n', 'no', 'agora não', 'não valeu']

while sim in resposta:

    print('       Aula 7  calculo ')
    print()
    print()
    print('índice:')
    print ('o5 = leia um numero inteiro')
    print ('06 = mostre o dobro')
    print ('07 = calculo de media')
    print ('08 = metros cm e milimetros')
    print ('09 = tabuada')
    print ('10 = convertendo em dolares')
    print ('11 = pintura')
    print ('12 = desconto ')
    print ('13 = aumento de 15%')
    print()

    menu=input('menu:')


    #                 05- leia um numero inteiro _________________


    if menu == '05' :

        numero=0

        print ()
        numero=int(input('Digite um numero inteiro:'))

        antes = numero - 1
        depois = numero + 1

        print ()
        print(' numero anterior :{} \n numero digitado :{} \n numero posterio: {}'.formato(antes, numero, depois))


    #                  06- mostre o dobro ____________________


    if menu =='06':

        numero=0
        dobro=0
        triplo=0
        raiz=0

        print ('               06- mostre o dobro ')
        print ('\n'*2 )
        numero=int(input('digite um numero:'))

        dobro=numero*2
        triplo=numero*3
        raiz=numero**(1/2)

        print ('\n'*2 )
        print (' O dobro:{} \n O triplo:{} \n A raiz quadrada:{}' .formato(dobro, triplo, raiz))


    # _______________________  07- Media _________________


    if menu =='07':

        print ('              07- Media')
        print ('\n')
        n1=int(input('1° nota:'))
        n2=int(input('2° nota:'))

        resultado=(n1+n2)/2

        print ('media:', resultado)


    #                  08- metros cm e milimetros ______________

    if menu =='08':

        numero=0

        print ('\n              Metros em cm e cm em mm \n')

        numero=int(input('Metros:'))

        m=numero*100
        mm=numero*1000

        print (' cm:{} \n mm:{}'. formato(m, mm))


    # ________________ 09- tabuada _______________________

    if menu =='09':

        numero=0

        print ('\n           tabuada \n')

        numero=int(input('digite um numero:'))

        for i in range(11):

            tabuada=numero*i
            print ('{} x {} = {}'. formato(numero, i, tabuada))


    # ________________ 010- convertendo em dolares __________

    if menu =='10':

        numero=0

        print ('\n         convertendo dinheiro $ \n')
        numero=int(input('R$:'))

        tolar=numero/3,27

        print ('valor convertido {} $'. formato(tolar))

    # ___________________ 11- pintura _______________________

    if menu =='11':

        print ('\n     pintura  \n ')
        print ('calcular a área da parede:')
        l1=int(input('lado l1='))
        l2=int(input('lado l2='))
        a=l1*l2

        print ('Área:', a)
        tinta=int(input('quantidade de dinta em litros:'))
        tinta=tinta*2

        print ('Área pintada:', tinta)

    # ________________ 012- desconto _____________________

    if menu =='12':

        numero=0
        desconto=0

        numero=int(input('         Desconto % \n valor:'))
        desconto=int(input('Desconto %:'))

        numero=desconto*(numero/100)

        print ('desconto:', numero)

    # _________________ aumento de 15% ___________________

    if menu =='13':

        numero=0

        numero=int(input('         Aumento de 15 % \n salario:'))

        numero=15*(numero/100)

        print ('aumento:', numero)



    if menu =='teste':
        idade =70

        if idade < 12:

            print('criança')
        elif idade < 18:
            print('adolescente')
        elif idade < 60:
            print('adulto')
        else:
            print('idoso')





    # _________________ final do código ___________________




    sim=input(' \n quer continuar?')
    if sim in nao:
        sim = 'n'
        pare=input('ok ate ')

    elif sim in resposta:
        sim = 's'
        pare=input('vamos la :)')

    else:
        sim = 's'
        pare=input('não entendi :|')
