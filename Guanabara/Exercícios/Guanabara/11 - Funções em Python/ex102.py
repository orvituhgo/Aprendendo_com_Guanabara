def fatorial(num, show=False):
    soma = 1
    for c in range(num, 1, -1):
        soma *= c
        if show is True:
            print(f'{c} X', end=' ')
    if show is True:
        print(f'1 = {soma}')
    else:
        print(f'O fatorial de {num} é {soma}')


try:
    numero = int(input('Digite uma número para obter o fatorial: '))
    sequencia = str(input('Deseja ver a sequência? [S/N] '))
    while sequencia not in 'SN':
        print('Por favor digite S ou N')
        sequencia = str(input('Deseja ver a sequência? [S/N] '))
    if sequencia == 'S':
        sequencia = True
    else:
        sequencia = False
except:
    print('Valor inválido')

fatorial(numero, sequencia)
