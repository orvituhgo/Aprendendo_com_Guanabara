r1 = float(input("digite uma medida para uma aresta: "))
r2 = float(input("digite uma medida para uma aresta: "))
r3 = float(input("digite uma medida para uma aresta: "))

if (r1 + r2 > r3 and r1 == r2 == r3) or (r2 + r3 > r1 and r1 == r2 == r3) or (r1 + r3 > r2 and r1 == r2 == r3):
    print('As arestas formam um triângulo EQUILÁTERO!')
elif (r1 + r2 > r3 and r1 == r2) or (r2 + r3 > r1 and r2 == r3) or (r1 + r3 > r2 and r1 == r3):
    print('As arestas formam um triângulo ISÓCELES!')
elif (r1 + r2 > r3 and r1 != r2) or (r2 + r3 > r1 and r2 != r3) or (r1 + r3 > r2 and r1 != r3):
    print('As arestas formam um triângulo ESCALENO!')
else:
    print('As arestas não formam um triângulo!')
