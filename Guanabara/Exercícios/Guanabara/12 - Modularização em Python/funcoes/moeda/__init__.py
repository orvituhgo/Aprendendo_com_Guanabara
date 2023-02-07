def dobrar(num):
    '''
    - Função que retornará o dobro do número informado
    :param num: número a ser dobrado
    :return: retorna a identidade do dobro do número
    '''
    return num*2


def triplicar(num):
    '''
    - Função que retornará o triplo do número informado
    :param num: número a ser triplicado
    :return: retorna a identidade do triplo do número
    '''
    return num*3


def metade(num):
    return num*0.5


def aumentar(num, taxa):
    '''
    - Função que aumentará o número em função da porcentagem informada no segundo argumento
    :param num: número a ser aumentado
    :param taxa: percentual a ser aplicado ao número informado
    :return: retorna a identidade do número aumentado
    '''
    return num*(1+(taxa/100))


def diminuir(num, taxa):
    '''
    - Função que diminuirá o número em função da porcentagem informada no segundo argumento
    :param num: número a ser diminuído
    :param taxa: percentual a ser aplicado ao número informado
    :return: retorna a identidade do número diminuído
    '''
    return num*(1-(taxa/100))


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')

