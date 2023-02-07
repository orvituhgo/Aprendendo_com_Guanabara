lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    SN = input('Quer continuar? [S/N]').strip().upper()
    if SN in 'Nn':
        break
for t in range(0, len(lista)):
    if lista[t] % 2 == 0:
        par.append(lista[t])
    else:
        impar.append(lista[t])
lista.sort()
impar.sort()
par.sort()
print(f'A lista digitada foi {lista}\n'
      f'sendo a lista de pares {par}\n'
      f'e a lista de impares {impar}')

