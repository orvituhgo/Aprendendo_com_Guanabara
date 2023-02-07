n = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão: '))
a = float(input('Termo que você quer: '))
b = 0
c = 0
while a != 0:
    if a != b:
        print(n + (r * (b+c)))
        b += 1
    if a == b:
        c = a
        a = float(input('Quer mais algum outro termo?'))
        b = 0
print('FIM!')
