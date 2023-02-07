par = list()
impar = list()
numeros = list()
num = c = 0

while True:
    num = int(input('Digite um número: '))
    c += 1
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    SN = str(input('Gostaria de continuar? [S/N]: '))
    if SN in 'Nn':
        break

numeros.append(par[:])
numeros.append(impar[:])

print(f'Você digitou {c} números \n sendo {numeros[0]} pares \n e {numeros[1]} ímpares')
