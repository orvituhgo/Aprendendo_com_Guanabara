def performancefutebol(jog, totgols):
    """
    função para tratar erro e printar nome de jogador e quantidade de jogos
    :param jog: nome do jogador
    :param totgols: total de gols realizados pelo jogador
    :return: none
    """
    if jog == '':
        nome = '<desconhecido>'
    else:
        nome = jog
    if totgols == '':
        gols = 0
    else:
        gols = totgols

    print(f'O jogador {nome} marcou {gols} gols')

jogador = str(input('Insira o nome do jogador: '))
try:
    total = int(input('Insira o total de gols marcados por ele: '))
except:
    total = 0

performancefutebol(jogador, total)
