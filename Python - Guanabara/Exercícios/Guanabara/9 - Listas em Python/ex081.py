lista = []
c = 0
while True:
    lista.append(int(input('Digite um número: ')))
    SN = input('Quer continuar? [S/N]').strip().upper()
    c += 1
    if SN in 'Nn':
        break
if lista.count(5) != 0:
    print('Foi digitado o número 5 na lista.')
else:
    print('Não foi digitado nenhum número 5.')
lista.sort(reverse=True)
print(lista)
print(f'Foram adicionados {c} na lista')