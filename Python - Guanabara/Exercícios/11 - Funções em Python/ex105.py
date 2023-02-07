def resumonota(*notas, sit=False):
    """
    -> Função que reúne as notas de determinado aluno em dicionário e determina média, maior e menor nota e quantidade
    de notas, podendo ou não fazer juízo de valor.
    :param notas: inserir argumentos posicionais ad infinitum
    :param sit: se True, poderá mostrar a situação do aluno(necessário inserção com keyword
    :return: none
    """
    boletim = dict()
    quantidade = maior = menor = media = 0
    for item in notas:
        quantidade += 1
        media += item
        if item == 0:
            maior = menor = item
        else:
            if item >= maior:
                maior = item
            if item <= menor:
                menor = item
    media = media / quantidade
    boletim['total'] = quantidade
    boletim['maior'] = maior
    boletim['menor'] = menor
    boletim['média'] = media
    if sit is True:
        if media >= 5 and media < 7:
            boletim['situacao'] = 'RECUPERAÇÃO'
        elif media >= 7:
            boletim['situacao'] = 'APROVADO'
        elif media < 5 and media >= 0:
            boletim['situacao'] = 'REPROVADO'
    return boletim


print(resumonota(10, 9, 3, 5, 4, 0, 9, 8, 9.5, sit=True))