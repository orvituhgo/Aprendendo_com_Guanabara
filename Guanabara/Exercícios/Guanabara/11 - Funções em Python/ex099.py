def maximo(*num):
    maior = menor = 0
    for p in range(0, len(num)):
        if num[p] == 0:
            maior = menor = num[p]
        else:
            if num[p] > maior:
                maior = num[p]
            if num[p] < menor:
                menor = num[p]
    for t in range(0 , len(num)):
        print(num[t], end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    print()


maximo(1, 3, 5, 6, 9, 21, 3, 2, 1)
maximo(3, 1, 0, -1, -2, 59, 10, 13)
maximo()
maximo(6)
