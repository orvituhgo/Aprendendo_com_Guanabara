print('Tuplas (),Listas []')
#tuplas são imutáveis
#listas são mutáveis

lista = ['Arroz', 'Feijão']
print(lista)
#append adiciona um item por vez no final
lista.append('Bife')
print(lista)
#insert adiciona um item em uma determinada posição um por vez
lista.insert(2, 'Ovo')
print(lista)
del lista[2]
lista.pop(2)
#remove = remove o primeiro valor da esquerda para a direita
lista.remove('Feijão')
print(lista)
lista.append('Feijão')
lista.append('Bife')
#pop() remove o ultimo item
print(lista)
#se tentar remover um item na lista q nao esteja vai dar erro entao deve:
if 'Ovo' in lista:
    lista.remove('Ovo')
else:
    print('Não tem ovo')
print('')
valores = list(range(4, 11))
print('1 ', valores)
valores = [1, 5, 3, 0, 2, 3, 9]
print('2 ', valores)
valores.sort()
print('3 ', valores)
valores.sort(reverse=True)
print('4 ', valores)
valores[2] = 10
print('5 ', valores)
for v in valores:
    print(f'{v}...',end=' ')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei {v}.')
print('Cheguei ao final da lista')
for cont in range(0, 2):
    valores.remove(int(input('Digite o valor para retirar da lista')))
valores.sort()
print(valores)
#para copiar uma lista para outra sem interligar deve:
novalista = valores[:]
novalista.pop()
print(novalista, end=' ')
