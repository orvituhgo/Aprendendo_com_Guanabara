i = c = cf = maior = média = 0
n = sexo = nmaior =""

for c in range(1, 5):
    n = input('Qual seu nome?').strip().upper()
    i = int(input('Qual sua idade?'))
    sexo = input('Qual o sexo?[M/F]').strip().upper()[0]
    média += i
    if sexo == 'M' and i > maior:
        nmaior = n
        maior = i
    else:
        nmaior = nmaior
        maior = maior
    if sexo == 'F' and i < 20:
        cf += 1
print(f'A média é {média/(c)}')
print(f'O homem mais velho é o {nmaior}')
print(f'O número de mulheres com menos de 20 anos é {cf}')
