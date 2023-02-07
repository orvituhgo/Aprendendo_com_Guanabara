valor = vanterior = posmax = posmin = maxvalor = minvalor = 0
lista = []

for c in range(0, 5):
    lista.append(int(input(f'Digite um valor da posição {c}: ')))
maxvalor = max(lista)
minvalor = min(lista)
posmax = lista.index(maxvalor)
posmin = lista.index(minvalor)

print(f'O valor {maxvalor} é o maior e está na posição {posmax}\n'
      f'O valor {minvalor} é o menor e está na posição {posmin}')
