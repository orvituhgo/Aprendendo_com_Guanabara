lista = []
for c in range(0, 5):
    lista.append(int(input('Insira um valor:')))
print(f'O maior valor é {max(lista)} e aparece na(s) posição(ões):', end=' ')
for t in range(0, len(lista)):
    if lista.count(max(lista)) > 1:
        numero = lista[t]
        if numero == max(lista):
            print(t, end=' ')
if lista.count(max(lista)) == 1:
    print(lista.index(max(lista)), end=' ')
print(f'\nO menor valor é {min(lista)} e aparece na(s) posição(ões):', end=' ')
for v in range(0, len(lista)):
    if lista.count(min(lista)) > 1:
        numero = lista[v]
        if numero == min(lista):
            print(v, end=' ')
if lista.count(min(lista)) == 1:
    print(lista.index(min(lista)))
