r1 = float(input("digite uma medida para uma aresta: "))
r2 = float(input("digite uma medida para uma aresta: "))
r3 = float(input("digite uma medida para uma aresta: "))

if r1 + r2 > r3  or r2 + r3 > r1 or r1 + r3 > r2:
    print('TRIÂNGULO: ')
    if r1 == r2 == r3:
        print('As arestas formam um triângulo EQUILÁTERO!')
    if r1 != r2 != r3 != r1:
        print('As arestas formam um triângulo ESCALENO!')
    else:
        print('As arestas formam um triângulo ISÓCELES!')
else:
    print('As arestas não formam um triângulo!')
