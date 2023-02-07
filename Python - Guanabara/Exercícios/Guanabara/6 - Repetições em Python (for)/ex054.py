from datetime import date

atual = date.today().year
maior = 0
menor = 0

for c in range(1,8):
    nasc = int(input('Diga o ano de seu nascimento: '))
    if atual - nasc >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('Há {} que atingiram e {} que não'.format(maior, menor))
