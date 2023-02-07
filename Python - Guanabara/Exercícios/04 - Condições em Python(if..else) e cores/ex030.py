n = int(input('say a number: '))
div = n % 2
# // - divisão por inteiro (resultado inteiro)
# % - resto da divisão

if div == 0:
    print('This number is "par"')
else:
    print('This number is "impar"')
