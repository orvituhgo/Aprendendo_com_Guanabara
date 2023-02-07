from random import randint
números = (int(randint(0, 10)), int(randint(0, 10)),
           int(randint(0, 10)), int(randint(0, 10)),
           int(randint(0, 10)))
maior = 0
menor = 999
for c in range(0, 5):
    número = números[c]
    if maior <= número:
        maior = número
    else:
        maior = maior
    if menor >= número:
        menor = número
    else:
        menor = menor
print(f'Os números sorteados são: {números}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
