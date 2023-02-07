linha = 20*'-'

print(linha)
print('TABUADA'.center(20, '-'))
print(linha)

n = int(input('Digite o número que quer a tabudada:\n'))

for t in range(1, 11):
    print('{} x {} = {}'.format(n, t, t*n))
