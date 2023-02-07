listagem = ('Pão', 1, 'Chinelo', 15.99, 'Pedra', 2.00, 'Janela', 900.00, 'Alçapão', 430.00, 'Computador', 20000.00)
linha = '-' * 40
print(linha)
print('TABELA DE PREÇOS'.center(40))
print(linha)
for c in range(0, len(listagem), 2):
    print(f'{listagem[c]:.<20}{"R$":.>20}{listagem[c+1]}')
