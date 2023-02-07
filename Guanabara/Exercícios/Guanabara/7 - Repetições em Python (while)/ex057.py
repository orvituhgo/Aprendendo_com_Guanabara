sexo = input('Informe o sexo [F/M]: ').strip().upper()[0]
#while sexo != 'F' and sexo != 'M':
while sexo not in 'MmFf':
    sexo = input('Informe o sexo [F/M]: ').strip().upper()[0]
print(sexo)