def leiaint(pergunta):
    while True:
        try:
            entrada = int(input(pergunta))
        except:
            print('\033[4;31;40m>>> ERRO <<< DIGITE UM NÚMERO INTEIRO\033[m')
        else:
            break
    return entrada


print(leiaint('Digite um número: '))
