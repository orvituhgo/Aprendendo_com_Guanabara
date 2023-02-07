import random
import time

njogos = numerador = int(input('How many tips do you want?'))
palpites = list()
jogo = list()
num = 0

for i in range(0, njogos):
    while len(jogo) != 6:
        num = random.randint(0, 60)
        while jogo.count(num) == 0:
            jogo.append(num)
    palpites.append(jogo[:])
    jogo.clear()
print('\n GERANDO JOGOS\n')
time.sleep(1)
for i in range(0, njogos):
    print(f'Palpite - Jogo {1+i} = {palpites[i]}')
    time.sleep(0.5)
