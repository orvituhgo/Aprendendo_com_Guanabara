total = menor = maior1000 = cont = 0
barato = ''
while True:
    produto = str(input('NOME DO PRODUTO: '))
    valor = float(input('VALOR DO PRODUTO: R$ '))
    total += valor
    cont += 1
    if valor > 1000:
        maior1000 += 1
    if cont == 1 or valor < menor:
            menor = valor
            barato = produto
    SN = ' '
    while SN not in 'SN':
        SN = str(input('QUER ADICIONAR MAIS PRODUTOS? [S/N] ')).strip().upper()
    if SN == 'N':
        break
print(f'''Segue resumo da sua compra:
O total é {total:.2f}.
Você está comprando {maior1000:.0f} produtos com preço maior que R$1000,00
O produto mais barato é {barato} no valor de R${menor:.2f}''')
