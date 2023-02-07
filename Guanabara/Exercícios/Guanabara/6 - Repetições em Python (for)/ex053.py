'''f = str(input('Escreva uma frase: '))
n = int(len(f))
p = ''

for c in range(0, n):
    p = p + f[n - 1]
    n = n - 1
print(p)

if f.find(p) != -1:
    print('É palíndromo')
else:
    print('não é palíndromo')
'''

string = input('Digite uma frase: ')

if string == string[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')
