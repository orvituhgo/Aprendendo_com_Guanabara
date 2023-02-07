from datetime import date

atual = date.today().year
nasc = int(input('Digite o ano de seu nascimento: '))
idade = atual - nasc

if idade == 18:
    print('Você deve se alistar')
elif idade >18:
    print('Você devia se alistar há {}'.format(idade-18))
else:
    print('Você deverá se alistar em {}'.format(18-idade))
