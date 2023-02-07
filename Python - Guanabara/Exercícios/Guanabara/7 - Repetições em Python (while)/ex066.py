n = s = t = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    t += 1
    s += n
print(f'A soma total é {s} em {t} parcelas.')
