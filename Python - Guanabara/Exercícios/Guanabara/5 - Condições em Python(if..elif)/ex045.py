from random import randint
print('=' * 30)
print('{:^30}'.format('JOKENPÔ'))
print('=' * 30)
j = int(input('''Escolha uma opção
[1] PEDRA
[2] PAPEL
[3] TESOURA\n'''))
pc = randint(1,3)
pedra = 1
papel = 2
tesoura = 3
# possibilidade de empate
if pc == j:
    print('EMPATE ambos escolheram {}'.format(pc))
# possibilidades de vitória
# 1 + 2 = 3 (2) ----- 2 + 3 = 5 (3) ----- 1 + 3 = 4 (1)
elif pc + j == 3:
    if pc < j:
        print('Você ganhou. {} vence {}'.format(j, pc))
    else:
        print('Você perdeu. {} perde para {}'.format(j, pc))
elif pc + j == 5:
    if pc < j:
        print('Você ganhou. {} vence {}'.format(j, pc))
    else:
        print('Você perdeu. {} perde para {}'.format(j, pc))
elif pc + j == 4:
    if pc > j:
        print('Você ganhou. {} vence {}'.format(j, pc))
    else:
        print('Você perdeu. {} perde para {}'.format(j, pc))
print('FIM DE JOGO'.center(30, '-'))
