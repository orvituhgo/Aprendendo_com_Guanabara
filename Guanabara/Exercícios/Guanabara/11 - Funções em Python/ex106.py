from time import sleep

def ajuda(comando):
    '''
    -> Função realizará o interactive help com a função desejada
    :param comando: inserir função que deseja conhecer
    :return: none
    '''
    print(f'\033[7;30;40m{help(comando)}\033[m')


def titulo(texto):
    '''
    -> Função para printar título com separador superior e inferior
    :param texto: Título do texto
    :return: none
    '''
    tamanho = len(texto) + 4
    print(f'\033[1;36;40m{tamanho * "^"}\033[m')
    print(f'\033[1;36;40m{texto.center(tamanho)}\033[m')
    print(f'\033[1;36;40m{tamanho * "^"}\033[m')


while True:
    titulo('Sistema PyHelp')
    sleep(1.5)
    funcao = input('\033[4;32;40mDigite a função que deseja conhecer (sem parêntese):\033[m').strip().lower()
    if funcao == 'fim':
        sleep(0.7)
        print('FINALIZANDO...')
        sleep(1)
        break
    ajuda(funcao)



