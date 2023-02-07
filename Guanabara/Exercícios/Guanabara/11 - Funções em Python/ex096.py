def area(lenght, height):
    area = lenght*height
    print(f'A área do terreno é {area} m²')
    print()

# Programa

area(float(input('Digite a largura do terreno: ')),
     float(input('Digite o comprimento do terreno: ')))