n = int(input('Digite um númer que você quer saber a tabuada: '))
c = 1
while c != 11:
    if n <= 0 or n == '':
        break
    if n >= 0:
        print(f'{n} x {c} = {n*c}')
        c += 1
    if c == 11:
        n = int(input('Digite outro número para saber a tabuada: '))
        c = 1