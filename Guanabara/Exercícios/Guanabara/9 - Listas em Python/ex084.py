lista = list()
dadosPessoa = list()
peso = list()
c = 0

while True:
    dadosPessoa.append(str(input('Digite um nome: ')))
    dadosPessoa.append(float(input('Digite o peso: ')))
    lista.append(dadosPessoa[:])
    dadosPessoa.clear()
    c += 1
    SN = str(input('Quer continuar? [S/N]'))
    if SN in 'Nn':
        break
print(30 * '=-')
print(f'\nVocê adicionou {c} pessoas')
print(f'Sendo as mais pesadas: ', end='')
for p in lista:
    peso.append(p[1])
for p in lista:
    if max(peso) == p[1]:
        print(p[0], end=' ')
print(f'\nSendo as mais leves: ', end='')
for p in lista:
    if min(peso) == p[1]:
        print(p[0], end=' ')
