from time import sleep

linha = 30*'-'

print(linha)
print('EMPRÉSTIMO'.center(30, '-'))
print(linha)

salário = float(input('diga seu salário'))
anos = int(input('diga em quantos anos quer pagar?'))
casa = float(input('quanto custa a casa?'))
parcela = casa/(anos*12)

sleep(2)
if parcela > 0.3*salário:
    print('Você não pode pegar empréstimo, cada \nparcela no valor de {}'.format(parcela))
elif parcela <= 0.3*salário:
    print('Você pode pegar empréstimo, cada \nparcela no valor de {}'.format(parcela))
