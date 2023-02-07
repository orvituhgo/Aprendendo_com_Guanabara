números = (int(input('Digite um número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite o último número:')))
d = 0
if números.count(9) == 0:
    print('Não foi digitado nenhum número 9.')
else:
    print(f"Foi(ram) digitado(s) {números.count(9)} vez(es) o número 9")
print('E o número 3 aparece na(s) posição(ões):', end=' ')
for c in range(0, len(números)):
    número = números[c]
    if número == 3:
        print(c+1, end=' ')
    if número != 3:
        d += 1
if d == len(números):
    print('Nenhum...', end=' ')
d = 0
print('\nE o número(s) pare(s) digitado(s) foi(ram):', end=' ')
for c in range(0, len(números)):
    número = números[c]
    if número % 2 == 0:
        print(número, end=' ')
    if número % 2 != 0:
        d += 1
if d == len(números):
    print('Nenhum...')

