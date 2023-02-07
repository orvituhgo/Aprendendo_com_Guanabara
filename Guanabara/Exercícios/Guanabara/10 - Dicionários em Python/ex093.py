dados = dict()
gols = list()
gol = soma = 0

dados['nome'] = str(input('Qual é o jogador? '))
j = int(input('Quantos jogos jogou? '))
for t in range(0, j):
    gol = (int(input(f'Quantos gols realizou na partida {t + 1}? ')))
    soma += gol #poderia ser sum(gols) la em baixo fora desse laço
    gols.append(gol)
dados['gols'] = gols
print(f'O jogador {dados["nome"]} jogou {j} jogos.')
for t in range(0, j):
    print(f'   => Na partida {t + 1}, fez {dados["gols"][t]}.')
print(f'Foi um total de {soma} gols.')
