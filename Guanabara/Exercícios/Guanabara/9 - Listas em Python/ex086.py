import time
matriz = list()
linha = list()
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
    print()
    time.sleep(0.2)
