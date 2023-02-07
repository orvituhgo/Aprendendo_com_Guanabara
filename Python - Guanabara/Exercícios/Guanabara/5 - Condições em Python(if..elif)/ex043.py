altura = float(input('Insira sua altura em  metros: '))
peso = float(input('Insira seu peso em  kg: '))
imc = peso / altura ** 2
print('o seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está em sobrepeso!')
elif 30 <= imc < 40:
    print('Você está obeso!')
else:
    print('Você está com obesidade mórbida.')
