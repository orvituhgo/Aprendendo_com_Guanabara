def leiaInt(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
        except:
            print('\033[4;31m>>> ERRO <<< DIGITE UM NÚMERO INTEIRO\033[m')
        else:
            break
    return entrada


def leiaFloat(pergunta):
    while True:
        try:
            entrada = float(input(pergunta))
        except:
            print('\033[4;31m>>> ERRO <<< DIGITE UM NÚMERO REAL COM PONTO\033[m')
        else:
            break
    return entrada


i = leiaInt('Digite um número inteiro: ')
print(i)
f = leiaFloat('Digite um número real: ')
print(f)