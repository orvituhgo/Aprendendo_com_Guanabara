n1 = int(input('digite um número: '))
n2 = int(input('digite um número: '))
escolha = int(input('Digite o que quer fazer com os valores:\n'
                    '[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n'
                    '[4] NOVOS VALORES\n[5] SAIR\n'))
while escolha != 5:
    if escolha == 1:
        print('A soma destes número é {}'.format(n1 + n2))
    if escolha == 2:
        print('O produto entre estes números é {}'.format(n1 * n2))
    if escolha == 3:
        if n1 > n2:
            print('O maior número é: {}'.format(n1))
        elif n2 > n1:
            print('O maior número é: {}'.format(n2))
        else:
            print('Os dois números são iguais')
    if escolha == 4:
        n1 = int(input('digite um número: '))
        n2 = int(input('digite um número: '))
    escolha = int(input('Escolha outra opção: '))
if escolha == 5:
    print('Você saiu.')
