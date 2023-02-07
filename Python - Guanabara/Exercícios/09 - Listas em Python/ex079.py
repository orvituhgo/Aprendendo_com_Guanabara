lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    ultimo = lista[-1]
    if lista.count(ultimo) != 1:
        lista.pop()
        print('Item duplicado, não adicionado')
    else:
        print('Item adicionado')
    SN = input('Deseja continuar? [S/N]').strip().upper()[0]
    if SN == 'N':
        break
lista.sort()
print(f'Os itens digitados foram {lista}')


