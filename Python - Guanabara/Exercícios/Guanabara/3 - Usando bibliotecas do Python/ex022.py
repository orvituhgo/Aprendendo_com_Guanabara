name = input("What's your name? ")

print('O nome todo em letra maiusculas é: {}'.format(name.upper()))
print('O nome todo em letra minusculas é: {}'.format(name.lower()))
print('O nome sem os espaços possui {} letras'.format(len(name)-name.count(' ')))
print('O primeiro nome contém: {} letras'.format(len(name.split()[0])))
