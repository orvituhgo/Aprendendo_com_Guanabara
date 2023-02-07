n = float(input('digite o primeiro termo da PA: '))
r = float(input('digite a razão: '))
a = float(input('termo que você quer: '))
b = 0
while b != a:
    print(n + (r*b))
    b += 1
print('FIM!')
