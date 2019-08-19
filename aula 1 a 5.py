#   teste de sistema célular




print ('Ola ')
nome=input('Qual é o seu nome ?')

print ('Ola ' + nome, 'tudo bem?')


pregunta=input ('qual é a seu nome', nome, ' ?')

if nome == pregunta:
    print ('estava só te testando para ver se você esta ligado ;)')
    print()
    print (nome, 'vou precisar de alguns dados seus')
    dia = input('dia que naseu?')
    mes = input('mẽs do nacimento ?')
    ano = input('ano de nacimento?')
    print ('você naceu no dia', dia, 'do maês', mes, 'no anus de....')
    print ('opa !')
    print ('quer dizer ano ', ano)

elif nome != pregunta:
    print ('i! cara você não sabe seu nome!')
    print ('abandone. ')

pregunta_numero=input('quer fazer alguma soma?')
if pregunta_numero =='sim':
    suma=0
    numero=int(input('primeiro numero:'))
    numero2=int(input('segundo numero:'))

    soma=numero+numero2
    print ('=', soma)

elif pregunta_numero != 'sim':
    print ('ate mais então ')