n = int(input('Insira um número: '))
t = 0

for c in range(1, n+1):
    if n % c == 0:
        t += 1

if t == 2:
        print('{} é um número primo!'.format(n))
else:
        print('{} não é um número primero.'.format(n))

#estava errando poisnao estava pensando num
#contador