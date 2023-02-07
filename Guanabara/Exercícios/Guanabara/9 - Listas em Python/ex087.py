import time

matriz = list()
linha = list()
pares = 0
soma3col = 0

for i in range(0, 3):
    for j in range(0, 3):
        linha.append(int(input(f'Digite o elemento {i} {j}: ')))
    matriz.append(linha[:])
    linha.clear()
print('\n GERANDO MATRIZ\n')
time.sleep(1)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end='')
        if matriz[i][j] % 2 == 0:
            pares += matriz[i][j]
    print('\n', end='')
    time.sleep(0.2)
print(f'\nO maior valor na segunda linha é: {max(matriz[1])}')

for i in range(0, 3):
    soma3col += matriz[i][2]
print(f'A soma dos valores da terceira coluna é: {soma3col}')
print(f'E a soma de valores pares na matriz é: {pares}')