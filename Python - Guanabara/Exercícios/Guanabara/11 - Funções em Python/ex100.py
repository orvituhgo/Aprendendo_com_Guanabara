from random import randint

lista = list()
sorteio = list()

for p in range(0, randint(6, 15)):
    lista.append(randint(0, 50))
def sortear(lista1, lista2):
    for p in range(0, 5):
        lista2.append(lista1[randint(0, len(lista1)-1)])
    print('A lista "sorteio" foi criada e os seguintes números a compõem: ', end='')
    for t in range(0, len(lista2)):
        print(lista2[t], end=' ')
    print()

def somaPar(lista_a_ser_somada):
    somaPar = 0
    for t in range(0, len(lista_a_ser_somada)):
        if lista_a_ser_somada[t] % 2 == 0:
            somaPar += lista_a_ser_somada[t]
    print(f'A soma dos pares de sorteio {lista_a_ser_somada} é {somaPar}')

sortear(lista, sorteio)
somaPar(sorteio)

