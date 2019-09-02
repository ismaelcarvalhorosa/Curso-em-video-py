def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31m ERRO: \033[m \"{entrada}"\ não é um valor válido 😕 !')
        else:
            válido = True
            return float(entrada)