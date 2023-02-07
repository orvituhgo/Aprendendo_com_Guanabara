from datetime import date

atual = date.today().year
nasc = int(input('Diga o ano de seu nascimento: '))

idade = atual - nasc

if idade <= 9:
    print('Você tem {} e portanto é MIRIM'.format(idade))
elif 9 < idade <= 14:
    print('Você tem {} e portanto é INFANTIL'.format(idade))
elif 14 < idade <= 19:
    print('Você tem {} e portanto é JUVENIL'.format(idade))
elif 19 < idade <= 25:
    print("Você tem {} e portanto é SENIOR".format(idade))
elif idade > 25:
    print('Você tem {} e portanto é MASTER'.format(idade))
