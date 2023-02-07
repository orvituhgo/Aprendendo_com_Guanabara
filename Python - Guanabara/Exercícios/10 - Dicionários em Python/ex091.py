from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)
print('-' * 30)
print(f'{"RANKING":^30}')
print('-' * 30, '\n')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #0 para keys e 1 para values
for i, v in enumerate(ranking):
    print(f'{i + 1} lugar: {v[0]} com {v[1]}')
    sleep(1)
