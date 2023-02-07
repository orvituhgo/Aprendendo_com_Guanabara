s = 0
for p in range(1,7):
    n = int(input('Digite um número: '))
    if  n % 2 == 0:
        s += n
print('A soma de números pares digitados'
      ' é: {}'.format(s))
